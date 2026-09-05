# Shotcut LowLight

샷컷에서 한 번에 적용하는 저조도 보정 필터 세트입니다. 노이즈 제거와 중간톤 밝기 보정을 묶어 약·중·강 세 가지로 제공합니다.

**AI 자동 분석 기능은 아닙니다.** 정해진 보정값을 적용하는 프리셋이며, 원본 영상에 기록되지 않은 디테일은 복원하지 못합니다.

## 다운로드와 설치

1. [Releases](https://github.com/vasafifutu896-art/shotcut-lowlight/releases/latest)에서 **shotcut-lowlight.zip**을 다운로드하고 압축을 풉니다.
2. 샷컷에서 **Settings → App Data Directory → Show**를 누릅니다.
3. 열린 폴더의 **filter-sets** 폴더에 압축 안 `filter-sets` 폴더의 파일 3개를 복사합니다. 대상 폴더가 없으면 만드세요.
4. 프로젝트를 저장한 다음 샷컷을 종료하고 다시 실행합니다.

파일 이름에 확장자가 없는 것이 정상입니다. 샷컷 23.05.14 이상이 필요합니다. 설치 절차는 [샷컷 공식 Filter Sets 안내](https://forum.shotcut.org/t/filter-sets/40787)를 따릅니다.

## 적용

1. 타임라인의 영상 클립을 선택합니다.
2. 기존 Brightness, Color Grading, 노이즈 제거 필터는 우선 체크를 끕니다. 자르기·크기 조절 등 다른 필터는 그대로 두세요.
3. **Filters → ＋ → Sets → LowLight 2 Balanced**를 선택합니다.
4. 재생해서 확인하고 **Export → Export File**로 출력합니다.

| 세트 | 용도 |
| --- | --- |
| LowLight 1 Gentle | 약한 보정 |
| LowLight 2 Balanced | 중간 보정, 먼저 시도할 값 |
| LowLight 3 Strong | 강한 보정, 노이즈와 색 차이가 더 드러날 수 있음 |

세트마다 **Reduce Noise: HQDN3D**와 **Color Grading** 두 필터가 추가됩니다. 강도를 바꿀 때는 기존 세트가 추가한 두 필터를 제거하거나 체크를 끄고 새 세트를 선택하세요. 세트를 겹쳐 적용하지 마세요.

움직임에 잔상이 보이면 HQDN3D의 Temporal을 낮추거나 해당 필터를 끄세요. 4K 미리보기가 느리면 미리보기 해상도를 낮추세요. 세부 설명은 [README.txt](README.txt)에 있습니다.

## 검증과 제한사항

- XML 파싱과 RGB 보정값 일치를 확인했습니다.
- MLT의 톤 곡선 계산식에 따라 그림자 밝기 상승, 단조성, 흰색 출력 상한을 확인했습니다.
- **Windows 샷컷에서의 불러오기·재생·출력은 아직 미검증입니다.**
- 원본 영상이 제공되지 않아 영상별 색과 노이즈 품질도 미검증입니다.
- 실제 조명을 켜고 촬영한 영상과 같은 결과를 보장하지 않습니다.

## ZIP 다시 만들기

Python 3 표준 라이브러리만 사용합니다. Windows에서는:

```powershell
py -3 build_presets.py
```

Linux/macOS에서는 `python3 build_presets.py`를 실행하세요. 생성·검증 후 `dist/shotcut-lowlight.zip`이 만들어집니다.

## 사용한 샷컷 필터

- [Color Grading 정의](https://github.com/mltframework/shotcut/tree/master/src/qml/filters/color)
- [HQDN3D 정의](https://github.com/mltframework/shotcut/tree/master/src/qml/filters/hqdn3d)
- [MLT lift/gamma/gain 구현](https://github.com/mltframework/mlt/blob/master/src/modules/plus/filter_lift_gamma_gain.c)

샷컷 본체나 영상 파일은 포함하지 않습니다.
