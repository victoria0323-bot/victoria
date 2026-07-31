# 2026-08-01 (토) 1면 카드 이미지 생성 프롬프트

ChatGPT(GPT 이미지 생성)에 **아래 블록을 그대로 복사해서** 하나씩 넣으면 됩니다.
생성된 파일은 `newspaper/assets/` 에 저장하고, `data/2026-08-01.json` 의 해당 `image` 필드에
`assets/파일명.png` 형태로 경로를 넣으면 렌더링에 반영됩니다.

## 공통 규칙 (모든 프롬프트에 이미 포함되어 있음)

- **글자를 넣지 않는다.** 이미지 생성 모델은 한글을 깨뜨립니다. 숫자·라벨이 꼭 필요하면
  영문/아라비아 숫자만 아주 짧게.
- 스타일: 플랫 벡터 에디토리얼 일러스트, 굵은 선, 종이 질감 없는 깔끔한 배경.
- 팔레트: 네이비 `#1b2a4a`, 옐로 `#ffd400`, 레드 `#e8342f`, 블루 `#2f6ce5`, 오프화이트 `#f7f8fb`.
- 비율을 꼭 지켜야 카드 안에서 잘리지 않습니다.

---

## 1. 헤드라인 대형 사진 → `headline.image`

**비율: 가로로 아주 넓은 배너 (약 1000 x 320, 3:1). ChatGPT에서는 1536x640 또는 가장 넓은 가로 옵션으로 뽑고 위아래를 잘라 쓰면 됩니다.**

```
Flat vector editorial illustration for a Korean financial newspaper front page, ultra-wide 3:1 banner composition.
Subject: a stock market index line that plunges steeply through most of the frame, then makes one dramatic vertical rocket-like surge at the far right, ending in a bold upward arrow that breaks past the top edge.
Mood: "the cruel month ends in a reversal" — dark stormy left side gradually clearing into bright optimistic light on the right.
Include small abstract elements: memory semiconductor chip shapes floating along the rising part of the line, tiny silhouettes of investors looking up at the surge.
Palette: deep navy #1b2a4a background on the left, warm teal and yellow #ffd400 on the right, the index line in red #e8342f.
Style: bold clean vector shapes, minimal shading, generous negative space, modern infographic poster look.
No text, no letters, no numbers, no watermark, no logos.
```

## 2. 보조기사 1 배너 (보완수사권 폐지) → `sub_articles[0].image`

**비율: 가로로 넓은 얇은 배너 (약 380 x 110, 3.5:1).**

```
Flat vector editorial illustration, wide thin 3.5:1 banner, for a news card about prosecution reform legislation in Korea.
Subject: the dome of a national assembly building on the left, a judicial gavel and a pair of balance scales in the center, and on the right a magnifying glass with a diagonal line lightly crossing it to suggest an investigation power being removed.
Palette: soft blush background #fdecee, navy #1b2a4a line work, one red #e8342f accent.
Style: simple flat icons on a single-color background, thick uniform strokes, evenly balanced left-to-right composition so nothing is cropped at the edges.
No text, no letters, no numbers, no flags, no real people.
```

## 3. 보조기사 2 배너 (한·미·일 환율공조) → `sub_articles[1].image`

**비율: 가로로 넓은 얇은 배너 (약 380 x 110, 3.5:1).**

```
Flat vector editorial illustration, wide thin 3.5:1 banner, about coordinated currency market intervention by three countries.
Subject: three abstract circular badges in a row connected by a linking line, each holding a simple currency symbol — won, dollar, yen. Below them a downward-sloping exchange rate line in blue, with small arrows pointing down.
Palette: pale blue background #eaf1ff, navy #1b2a4a shapes, blue #2f6ce5 accent line.
Style: clean flat vector icon set, thick uniform strokes, symmetrical composition centered in the frame with margin on all sides.
No text, no letters, no country names, no flags.
```

## 4. (선택) 핵심뉴스 카드 삽화 → `core_news.image`

**비율: 정사각형 (렌더 시 108px 폭으로 축소되므로 아주 단순하게).**

```
Flat vector spot illustration, square 1:1, tiny icon-scale simplicity.
Subject: a single bull-market rocket made from a rising red candlestick chart bar, with a small yellow spark trail underneath.
Palette: navy #1b2a4a, red #e8342f, yellow #ffd400 on a transparent or pure white background.
Style: minimal flat icon, very few shapes, must stay readable when shrunk to 100 pixels wide.
No text, no numbers, no background scenery.
```

## 5. (선택) 광고 카드 비주얼 → `ad.image`

**비율: 가로 배너 (약 4:3 ~ 16:9).**

```
Flat vector product banner illustration for a foldable smartphone advertisement.
Subject: a foldable phone shown half-open at a three-quarter angle, floating on a soft gradient backdrop, with subtle abstract AI sparkle shapes around it.
Palette: deep navy #1b2a4a to indigo gradient, white device body, small yellow #ffd400 sparkle accents.
Style: clean modern tech-ad look, soft shadow, centered composition.
No text, no brand names, no logos.
```

---

## 생성 후 적용 방법

```bash
# 1) 내려받은 이미지를 assets 로 옮긴다
mv ~/Downloads/헤드라인.png newspaper/assets/2026-08-01-headline.png

# 2) data/2026-08-01.json 의 image 필드를 채운다
#    "headline": { ..., "image": "assets/2026-08-01-headline.png" }

# 3) 다시 렌더링
cd newspaper && python3 render.py data/2026-08-01.json
```
