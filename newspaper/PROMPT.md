# 프롬프트 모음

매일 카드 이미지를 만들 때 쓰는 프롬프트와, 사진 자리를 채울 AI 이미지 생성 프롬프트를 모아둔 문서.

---

## 1. 카드 이미지 만들기 (매일 쓰는 짧은 버전)

신문 1면 사진을 첨부하고 아래 문장만 보내면 된다. `newspaper/data/` 에 이전 파일들이
남아 있어서 형식·톤·Day 번호가 자동으로 이어진다.

```
[신문 1면 사진 첨부]

내일 N월 N일 1면이야. 늘 하던 대로 newspaper/data/YYYY-MM-DD.json 만들고
렌더링해서 이미지 보여줘. 브랜치에 커밋·푸시까지 해줘.
```

---

## 2. 카드 이미지 만들기 (전체 버전)

처음부터 다시 시키거나, 다른 도구에서 작업할 때 쓰는 전체 프롬프트.

```
너는 매일 아침 스레드에 올리는 "오늘의 1면 경제신문" 카드 이미지를 만드는 담당이야.
첨부한 신문 1면 사진을 읽고 아래 순서대로 작업해줘.

[작업 순서]
1. newspaper/data/ 의 가장 최근 JSON을 열어 형식과 톤을 그대로 따른다.
2. 그날 날짜로 newspaper/data/YYYY-MM-DD.json 을 새로 만든다.
3. `python3 render.py data/YYYY-MM-DD.json` 으로 PNG를 생성하고 결과 이미지를 보여준다.
4. JSON을 지정된 브랜치에 커밋·푸시한다. (PNG는 .gitignore 대상이라 커밋하지 않음)

[내용 채우는 규칙]
- date: "YYYY.MM.DD (요일)" / day_label: 직전 파일에서 주중(월~금) 기준으로 이어서 +1
- core_news: 1면 톱기사. title은 신문 헤드라인 그대로, bullets는 체크 5개.
  기사 본문에 실제로 나온 숫자·기업명·일정만 쓰고 추측은 넣지 말 것.
- indicators / market_index: 1면 우측 Market Index 박스의 숫자를 그대로 옮긴다.
  상승은 direction "up"(빨강 ▲), 하락은 "down"(파랑 ▼). date_label은 "N일", edition은 "N판".
  원엔·원유로는 변동폭이 없으니 change를 빈 문자열로 둔다.
- must_read: 1면에 실린 기사 5건. sub 끝에 지면 번호를 "(A3면)" 형태로 붙인다.
- headline: title/subtitle(부제 2줄, \n 구분)/body(1면 리드 문단을 3~5문장으로 압축).
- sub_articles: 1면의 2~3번째 비중 기사 2건. 사진이 없으면 icon 이모지 + color_bg 파스텔톤.
- summary: 그날 1면 전체를 관통하는 흐름을 경제 초보도 이해할 한 문장으로. 존댓말.
- tip_steps, footer, ad: 직전 파일 값을 그대로 유지.

[톤]
- 경제 공부 시작한 사람이 읽는다고 생각하고, 어려운 용어는 짧게 풀어쓴다.
- 기사에 없는 전망·해석을 지어내지 않는다. 신문에 나온 "~라는 분석이 나온다" 수준까지만.

[사진]
- assets/ 에 그날 사진 파일이 있으면 headline.image, sub_articles[].image 에 경로를 넣는다.
- 없으면 해당 필드를 비워둔다 (템플릿이 알아서 이모지 아이콘으로 대체됨).
```

---

## 3. 헤드라인 사진 AI 생성 프롬프트

`headline.image` 자리에 들어가는 큰 사진. 실제 보도사진 대신 쓰는 **연출 사진 느낌의
실사 이미지**다. (2026-07-23 헤드라인 이미지가 이 스타일)

### 스타일 고정 문구 (매번 붙여넣는 부분)

```
Photorealistic editorial press photograph, wide establishing shot,
natural available lighting, muted realistic color grading, shallow depth of field
in the foreground and sharp mid-ground, documentary news photography style,
shot on a 35mm lens. No text, no logos, no watermarks, no recognizable faces.
Aspect ratio 3:1 (or 16:9), subject centered so it survives a center crop.
```

### 쓰는 법

`[장면]` 자리에 그날 톱기사의 **현장 한 장면**을 구체적인 명사로 적는다.
추상적인 개념("경제 성장", "규제 완화")이 아니라 카메라로 찍을 수 있는 장면이어야 한다.

```
[장면 한 문장] + [위 스타일 고정 문구]
```

### 2026-08-05 헤드라인 예시 (테슬라 로보택시 카메라 모듈)

```
A driverless white two-seater robotaxi with no steering wheel and no pedals,
parked under bright lighting in a clean modern automotive assembly plant;
in the sharp foreground, a gloved technician's hands hold a small black
automotive camera module with a glass lens and an orange ribbon cable;
rows of identical camera modules sit in an anti-static tray on the workbench.
Photorealistic editorial press photograph, wide establishing shot, natural
available lighting, muted realistic color grading, documentary news photography
style, shot on a 35mm lens. No text, no logos, no watermarks, no recognizable
faces. Aspect ratio 3:1, subject centered.
```

### 주의

- **실존 인물은 생성하지 않는다.** 대통령·기업인 등이 나오는 기사는 인물 대신 현장·사물
  중심 장면으로 바꿔서 프롬프트를 쓴다. (예: 국무회의 사진 → 빈 회의장 테이블과 서류)
- **브랜드 로고·상표는 넣지 않는다.** "테슬라 로고가 박힌" 대신 "무인 로보택시"처럼
  일반 명사로 묘사한다.
- 이미지 안에 한글/영문 텍스트를 넣으라고 시키면 대부분 깨져서 나온다. 꼭 필요할 때만
  짧은 한 줄로 요청한다.

---

## 4. 보조 기사 배너 AI 생성 프롬프트

`sub_articles[].image` 자리에 들어가는 가로로 긴 작은 배너. 헤드라인과 달리 **실사가
아니라 두꺼운 외곽선의 플랫 벡터 아이콘 스타일**이다. (2026-07-23 우라늄 이미지가 이 스타일)

### 스타일 고정 문구

```
Flat vector icon illustration, two or three large simple objects arranged
side by side on a soft gradient background, thick dark outlines, glossy
highlights, bold saturated single-hue color scheme, clean and friendly,
sticker-like. No text, no letters, no numbers. Wide banner composition,
aspect ratio 3:1, generous empty space on the left.
```

### 2026-08-05 보조기사 예시 1 (SK하이닉스 채권 매수)

```
Flat vector icon illustration: a tall stack of gold coins next to a rolled-up
bond certificate with a ribbon, and a memory chip wafer leaning beside them,
on a soft warm amber gradient background. Thick dark outlines, glossy
highlights, bold saturated amber and gold color scheme, sticker-like.
No text, no letters, no numbers. Wide banner, aspect ratio 3:1.
```

### 2026-08-05 보조기사 예시 2 (부동산 중개소 폐업 / 플랫폼 직거래)

```
Flat vector icon illustration: a small shuttered storefront with a closed
roller shutter on the left, and a smartphone showing a simple house icon on
the right, with a dotted line connecting them, on a soft cool blue gradient
background. Thick dark outlines, glossy highlights, bold saturated blue color
scheme, sticker-like. No text, no letters, no numbers. Wide banner,
aspect ratio 3:1.
```

### 색 고르는 기준

카드마다 색 계열을 다르게 가져가면 두 배너가 나란히 놓였을 때 구분이 잘 된다.

| 기사 성격 | 추천 색 |
|---|---|
| 돈·투자·실적 | amber / gold |
| 부동산·정책 | blue |
| 에너지·환경 | green |
| 사건·규제·리스크 | red |

---

## 5. 만든 이미지 넣는 법

1. 생성한 이미지를 `newspaper/assets/` 에 날짜를 붙여 저장한다.
   - `assets/2026-08-05-headline.png`
   - `assets/2026-08-05-hynix.png`
   - `assets/2026-08-05-realestate.png`
2. 그날 JSON의 해당 필드에 경로를 적는다.

   ```json
   "headline": { "image": "assets/2026-08-05-headline.png" }
   ```

   ```json
   "sub_articles": [
     { "image": "assets/2026-08-05-hynix.png" },
     { "image": "assets/2026-08-05-realestate.png" }
   ]
   ```
3. `python3 render.py data/2026-08-05.json` 으로 다시 렌더링한다.

로컬 파일은 `render.py` 가 자동으로 base64로 변환해 넣으므로 경로만 적으면 된다.
