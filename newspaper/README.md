# 오늘의 1면 경제신문 이미지 템플릿

스레드(Threads)에 올리는 "오늘의 1면 경제신문" 카드 이미지를 만드는 템플릿입니다.
매일의 뉴스/지표 내용을 JSON 파일에 채워 넣으면 같은 디자인의 1080px 폭 PNG 이미지가 생성됩니다.

## 사용 흐름

1. 저녁에 신문 초판을 보고 그날의 핵심 내용을 정리한다.
2. `data/sample.json`을 복사해서 그날 날짜로 된 새 파일을 만들고 (예: `data/2026-07-14.json`) 내용을 채운다.
3. 이미지를 생성한다.

   ```bash
   pip install -r requirements.txt
   python3 render.py data/2026-07-14.json
   ```

   결과는 `output/2026-07-14.png` 에 저장됩니다. (`--out` 옵션으로 경로 지정 가능)

4. 생성된 PNG를 다음날 아침 스레드에 업로드한다. (이 템플릿은 이미지 생성까지만 담당하며, 스레드 자동 게시는 포함하지 않습니다.)

## data JSON 구조

`data/sample.json` 을 참고하세요. 주요 필드:

| 필드 | 설명 |
|---|---|
| `date`, `day_label` | 상단 날짜 배지, "Day 00N" |
| `hook_text` | 노란 밑줄 문구 |
| `core_news` | 좌측 카드 1 "오늘의 핵심 뉴스" (title + bullets) |
| `indicators`, `indicators_time` | 좌측 카드 2 "주요 지표" 리스트 (icon/label/value/change/direction) |
| `must_read` | 좌측 카드 3 "오늘 꼭 봐야 할 기사" (title + sub) |
| `summary` | 좌측 카드 4 "한 줄 요약" |
| `ad` | 우측 상단 광고 카드 (brand/icon/title/datetime/note) |
| `market_index` | 우측 상단 지표 표 (rows: label/value/change/direction, badge1/2) |
| `headline` | 메인 헤드라인 기사 (title/subtitle/body/image) — `image`는 로컬 경로나 URL, 비워두면 회색 플레이스홀더 |
| `sub_articles` | 하단 2단 보조 기사 (icon/color_bg/title/body) |
| `tip_steps` | "신문 읽는 TIP" 5단계 아이콘 |
| `footer` | 하단 바 (tagline/handle) |

`direction` 은 `"up"` 또는 `"down"` 이며 각각 빨강 ▲ / 파랑 ▼ 로 표시됩니다.

## 캐릭터 / 사진 이미지

- `assets/character-woman-cat.png` — TIP 박스 옆에 항상 고정으로 나오는 캐릭터(투명 배경 PNG). 바꾸고 싶으면 이 파일을 교체하면 된다.
- `headline.image` 필드에 로컬 파일 경로(예: `assets/2026-07-22-headline.jpg`)나 URL을 넣으면 헤드라인 기사 옆 사진 자리에 들어간다. 비워두면 회색 플레이스홀더가 나온다.
- 로컬 이미지 파일은 `render.py`가 자동으로 base64로 인코딩해 넣어주므로 별도 처리가 필요 없다.

## 파일 구성

- `template.html.j2` — Jinja2 HTML/CSS 템플릿 (디자인 전체)
- `render.py` — JSON 데이터를 템플릿에 채운 뒤 헤드리스 크롬으로 PNG 스크린샷 생성
- `data/sample.json` — 예시 데이터 (첨부 이미지 내용 기반)
- `assets/` — 고정 캐릭터 이미지 등 재사용 이미지 자산
- `output/` — 생성된 PNG 저장 위치
