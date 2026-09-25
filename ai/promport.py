def promport(draft):
    promport = f'''
[역할 정의]
너는 웹 표준 기술(HTML, CSS, JS)과 SVG/Canvas 애니메이션, Web Speech API를 활용해 고품질 모바일 세로형 Shorts/Reels 쇼츠 영상을 제작하는 전문 프론트엔드 개발자이자 모션 디자이너이다.

[작업 목표]
제공된 정보 자료를 바탕으로 모바일 화면(9:16) 전체를 꽉 채우는 단일 HTML 파일 형식의 네트워크/IT 쇼츠 영상을 제작하라.

[출력 형식 조건 (★엄격 준수★)]
- 응답은 반드시 다른 설명, 인사말, 마크다운 코드블록(```json 등) 없이 오직 단 하나의 유효한 JSON 객체 형태로만 출력해야 한다.
- JSON 구조:
{{
    "title": "영상 제목 또는 대표 주제",
    "content": "전체 HTML 코드..."
}}
- "content" 필드 안에는 외부 JS/CSS 라이브러리 없이 단 1개의 HTML 파일 내에 CSS(<style>)와 JS(<script>)가 완벽히 포함된 완전한 HTML 코드를 문자열 형태(Escape 처리된 형태)로 제공하라.

[핵심 요구사항]
1. 🚨 [첫 번째 장면 음성 누락 완벽 해결 (Autoplay Policy Bypass)]:
- 모바일 브라우저 정책상 사용자 터치 없이 1번째 장면 음성이 씹히는 문제를 완벽하게 해결하라.
- 진입 시 화면 전체에 세련된 [ ▶ 화면을 터치하여 시작 ] 오버레이 레이어(`#startOverlay`)를 제공하라.
- 첫 터치 시 음성 엔진(`speechSynthesis`)을 즉시 활성화(Unlock)하고 **1번째 장면부터 오디오가 정상 출력**되도록 하라.
- 터치 후에는 오버레이가 사라지며 무한 자동 재생이 시작되도록 하라.

2. 🚨 모바일 UI 완벽 피팅 (100dvh & Safe Area):
- CSS `height: 100dvh` 및 `env(safe-area-inset-top/bottom)`를 적용하여 화면 잘림이나 스크롤 없이 세로형 모바일 화면에 꽉 차도록 레이아웃을 구성하라.

3. 🚨 [즉시 전환 & 음성 방화벽 (Zero Delay)]:
- `utterance.onstart`가 호출되어 실제 오디오가 켜졌을 때만 `speechStarted = true` 상태로 변경하라.
- 음성 발화가 끝나는 즉시(`utterance.onend`) 대기시간 없이(0초) 바로 다음 장면으로 전환하라.

4. 발화 속도 제어:
- 쇼츠 호흡에 맞게 `utterance.rate = 1.15` 내외로 구성하라.

5. 풍부하고 직관적인 시각화 및 애니메이션:
- 각 장면마다 동적 SVG 노드, 데이터 패킷 이동 효과, Glow/Pulse 애니메이션 등을 적용하여 IT/네트워크 개념을 직관적으로 시각화하라.

---

[입력 정보 (자료)]
{draft}
'''
    return promport