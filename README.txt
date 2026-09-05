샷컷 저조도 보정 필터 세트

원클릭으로 정해진 보정값을 적용하는 세트입니다. AI 장면 분석이나
사라진 디테일 복원 기능은 아닙니다. 원본 영상에 맞춘 조정은 필요할 수 있습니다.

설치
1. ZIP 파일을 압축 해제합니다.
2. 샷컷에서 Settings > App Data Directory > Show를 누릅니다.
3. 열린 폴더의 filter-sets 폴더에 ZIP 안 filter-sets 폴더의 파일 3개를 복사합니다.
   대상 filter-sets 폴더가 없으면 만드세요. 파일에는 확장자가 없는 것이 정상입니다.
4. 프로젝트를 저장한 다음 샷컷을 종료하고 다시 실행합니다.

사용
1. 타임라인의 영상 클립을 선택합니다.
2. 전에 추가한 Brightness, Color Grading, 노이즈 제거 필터는 우선 체크를 끕니다.
   자르기, 크기 조절 등 다른 편집 필터는 그대로 두세요.
3. Filters > + > Sets에서 LowLight 2 Balanced를 선택합니다.
4. Reduce Noise: HQDN3D와 Color Grading 두 개가 추가됩니다.
5. 재생해서 확인한 뒤 Export > Export File로 출력합니다.

강도 선택
LowLight 1 Gentle: 약한 보정
LowLight 2 Balanced: 중간 보정, 먼저 시도할 값
LowLight 3 Strong: 강한 보정, 노이즈와 색 차이가 더 드러날 수 있음

세트를 겹쳐 적용하지 마세요. 강도를 바꾸려면 이전 세트가 추가한
두 필터를 제거하거나 체크를 끈 다음 다른 세트를 적용하세요.
네 개 이상의 보정 필터가 중복 적용되면 화면이 과하게 밝아질 수 있습니다.

모든 세트는 RGB에 같은 보정값을 사용하여 의도적인 색조 변경을 피합니다.
중간톤을 밝히고 흰색 출력에는 여유를 두지만, 이미 날아간 밝은 영역이나
원본에서 기록되지 않은 어두운 디테일은 복원하지 못합니다.
HQDN3D는 약한 공간/시간 노이즈 제거이며 심한 압축 손상까지 제거하지 못합니다.
움직임에 잔상이 보이면 HQDN3D의 Temporal을 낮추거나 해당 필터를 끄세요.
4K 미리보기가 느려지면 미리보기 해상도를 낮추거나 노이즈 제거를 잠시 끄세요.

기술 정보 / 검증 범위
샷컷 Filter Sets 형식, frei0r.hqdn3d와 lift_gamma_gain 서비스를 사용합니다.
Filter Sets는 Shotcut 23.05.14 이후 제공됩니다.
XML 파싱, RGB 보정값 일치, 톤 곡선의 그림자 밝기 상승/단조성/흰색 상한을 확인했습니다.
사용자 Windows 샷컷에서의 불러오기, 실제 재생과 출력은 아직 검증하지 못했습니다.
원본 동영상이 제공되지 않아 영상별 색과 노이즈 품질도 미검증입니다.

설치 방식: https://forum.shotcut.org/t/filter-sets/40787
필터 정의: https://github.com/mltframework/shotcut/tree/master/src/qml/filters/color
노이즈 정의: https://github.com/mltframework/shotcut/tree/master/src/qml/filters/hqdn3d
