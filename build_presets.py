from pathlib import Path
import math
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).parent
PRESETS = [
    ('LowLight 1 Gentle', 1.35, 0.98, 0.025, 0.040),
    ('LowLight 2 Balanced', 1.60, 0.96, 0.035, 0.055),
    ('LowLight 3 Strong', 1.95, 0.92, 0.045, 0.065),
]

def prop(node, name, value):
    ET.SubElement(node, 'property', name=name).text = str(value)

for name, gamma, gain, spatial, temporal in PRESETS:
    mlt = ET.Element('mlt', LC_NUMERIC='C', version='7.21.0', root='', parent='producer0')
    producer = ET.SubElement(mlt, 'producer', id='producer0')
    for key, value in [('resource', 'black'), ('mlt_service', 'color'),
                       ('eof', 'pause'), ('shotcut:filtersClipboard', 1)]:
        prop(producer, key, value)
    noise = ET.SubElement(producer, 'filter', id='filter0')
    for key, value in [('mlt_service', 'frei0r.hqdn3d'), ('0', spatial), ('1', temporal)]:
        prop(noise, key, value)
    color = ET.SubElement(producer, 'filter', id='filter1')
    prop(color, 'mlt_service', 'lift_gamma_gain')
    prop(color, 'shotcut:filter_version', 1)
    for channel in 'rgb':
        prop(color, 'lift_' + channel, 0)
        prop(color, 'gamma_' + channel, gamma)
        prop(color, 'gain_' + channel, gain)
    ET.indent(mlt, space='  ')
    ET.ElementTree(mlt).write(ROOT / 'filter-sets' / name, encoding='utf-8', xml_declaration=True)

# Validate the serialized values and the MLT lift/gamma/gain transfer function.
# This checks neutral color, shadow lift, monotonicity, and highlight headroom;
# it does not substitute for running Shotcut on the user's original video.
for name, *_ in PRESETS:
    tree = ET.parse(ROOT / 'filter-sets' / name)
    filters = tree.findall('./producer/filter')
    assert len(filters) == 2
    p = {x.attrib['name']: x.text for x in filters[1].findall('property')}
    gamma, gain = float(p['gamma_r']), float(p['gain_r'])
    assert all(p[f'gamma_{c}'] == p['gamma_r'] and p[f'gain_{c}'] == p['gain_r'] for c in 'rgb')
    def curve(x):
        return min(1.0, max(0.0, math.pow(math.pow(x, 1 / 2.2), 2.2 / gamma) * math.pow(gain, 1 / gamma)))
    samples = [curve(x / 255) for x in range(256)]
    assert samples[0] == 0 and samples[-1] < 1
    assert all(a <= b for a, b in zip(samples, samples[1:]))
    assert curve(0.05) > 0.05 and curve(0.2) > 0.2
    print(f'{name}: XML and neutral tone curve OK; 5% -> {curve(.05):.1%}, white -> {curve(1):.1%}')

(ROOT / 'dist').mkdir(exist_ok=True)
output = ROOT / 'dist' / 'shotcut-lowlight.zip'
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
    for file in sorted((ROOT / 'filter-sets').iterdir()):
        archive.write(file, 'filter-sets/' + file.name)
    archive.write(ROOT / 'README.txt', 'README.txt')
print(f'Created {output}')
