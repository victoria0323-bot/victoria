# 삽화·사진 생성 프롬프트 가이드

카드 이미지에 들어가는 그림은 두 가지 스타일만 쓴다.

| 자리 | 스타일 | 권장 비율 | 실제 렌더 크기 |
|---|---|---|---|
| `headline.image` | 실사 편집사진 (photojournalism) | 3:2 또는 16:9 | 976 × 320 (center crop) |
| `sub_articles[].image` | 굵은 외곽선 카툰 벡터 배너 | 3:1 | 344 × 110 (center crop) |
| `core_news.image` | 카툰 벡터, 배경 투명 | 1:1 | 108 × 108 |
| `must_read_image` | 카툰 벡터 아이콘, 배경 투명 | 1:1 | 30 × 30 |
| `summary_image` | 카툰 벡터 아이콘, 배경 투명 | 1:1 | 64 × 64 |

가로로 잘리므로 **핵심 소재는 반드시 화면 중앙 60% 안에** 두도록 프롬프트에 명시한다.

---

## 1. 헤드라인 사진 (실사) — 공통 골격

```
A photorealistic editorial news photograph, [장면 설명].
Shot on a full-frame DSLR with a 35mm lens, natural available light,
documentary photojournalism style, muted realistic color grading,
shallow depth of field on the foreground subject, sharp background context.
Korean setting, contemporary 2026. Horizontal 3:2 composition with the
main subject centered in the middle 60% of the frame.
No watermark, no logo, no visible faces of identifiable people.
```

- 한글 간판/현수막을 넣고 싶으면 마지막에 한 줄 추가:
  `A banner in the background reads exactly "여기에_한글_문구" in clean Korean Gothic type.`
- 글자가 깨지는 게 싫으면 대신: `No text or lettering anywhere in the image.`

## 2. 보조기사 배너 (카툰 벡터) — 공통 골격

```
A bold cartoon vector illustration banner, [소재 A] on the left and
[소재 B] on the right, thick dark brown outlines, glossy highlights and
soft inner shading, chunky rounded shapes, sticker-like rendering.
Flat [색상] gradient background with a soft vignette, subtle drop shadows
under each object. Wide 3:1 horizontal banner, objects centered vertically,
generous empty space between the two objects.
No text, no letters, no numbers, no watermark.
```

- 배경 색상은 카드의 `color_bg`와 맞춘다.
  - 부동산·성장 = `warm green tint` / 증시·금융 = `cool blue-grey tint`
  - 정치·사법 = `warm amber gold tint` / 경고·리스크 = `muted red tint`

---

## 2026-08-10 (월) 실제 프롬프트

### ① 헤드라인 — "300만원이라도 … '대출난민' 된 고신용자"

```
A photorealistic editorial news photograph of a Korean bank branch interior
in the late afternoon. In the foreground, over the shoulder of a customer
seated at a loan consultation desk, a rejected loan application form lies on
the counter next to a calculator and a bank teller's hands. Behind the desk,
a blurred queue of waiting customers and a numbered ticket display board.
Cool fluorescent light mixed with warm window light, muted realistic color
grading, shallow depth of field on the paperwork, documentary photojournalism
style, shot on a full-frame DSLR with a 35mm lens. Korean setting,
contemporary 2026. Horizontal 3:2 composition with the desk and paperwork
centered in the middle 60% of the frame.
No visible faces, no watermark, no logo, no text or lettering anywhere.
```

> 대안(2금융권 강조 버전): `bank branch interior` 를
> `narrow street at dusk lined with small consumer-finance and savings-bank
> storefronts, glowing signboards, a lone pedestrian walking past` 로 교체.

### ② 보조기사 1 — "하남 그린벨트 해제 검토" (`color_bg: #eafbf3`)

```
A bold cartoon vector illustration banner, a large rolled-up architectural
site plan with a green protected-land map on the left, and a cluster of
chunky pastel apartment towers with a small crane on the right. Thick dark
brown outlines, glossy highlights and soft inner shading, chunky rounded
shapes, sticker-like rendering. Flat warm green gradient background with a
soft vignette, subtle drop shadows under each object. Wide 3:1 horizontal
banner, objects centered vertically, generous empty space between them.
No text, no letters, no numbers, no watermark.
```

### ③ 보조기사 2 — "증시 진공상태 … V자 반등이냐, L자 정체냐" (`color_bg: #eaf1ff`)

```
A bold cartoon vector illustration banner, a large glossy stock chart panel
showing a sharp V-shaped rebound line on the left, and a flat L-shaped
stagnant line with a small drooping arrow on the right. Thick dark brown
outlines, glossy highlights and soft inner shading, chunky rounded shapes,
sticker-like rendering. Flat cool blue-grey gradient background with a soft
vignette, subtle drop shadows under each object. Wide 3:1 horizontal banner,
objects centered vertically, generous empty space between them.
No text, no letters, no numbers, no watermark.
```

### ④ (선택) 카드1 삽화 `core_news.image`

```
A bold cartoon vector illustration of a single glossy credit score gauge
dial with its needle pushed into the red zone, thick dark brown outlines,
chunky rounded shapes, sticker-like rendering, soft inner shading.
Centered square composition on a fully transparent background.
No text, no numbers, no watermark.
```

---

## 저장·연결 방법

1. 생성한 이미지를 `newspaper/assets/` 에 날짜-주제 규칙으로 저장한다.
   - `2026-08-10-headline.png`, `2026-08-10-greenbelt.png`, `2026-08-10-market.png`
2. `data/2026-08-10.json` 의 해당 필드에 상대경로를 넣는다.

   ```json
   "headline":      { "image": "assets/2026-08-10-headline.png" },
   "sub_articles": [ { "image": "assets/2026-08-10-greenbelt.png" },
                     { "image": "assets/2026-08-10-market.png" } ]
   ```

3. 다시 렌더링한다.

   ```bash
   python3 render.py data/2026-08-10.json --out output/2026-08-10.png
   ```

`render.py` 가 로컬 파일을 자동으로 base64 data URI로 변환하므로 경로만 넣으면 된다.
