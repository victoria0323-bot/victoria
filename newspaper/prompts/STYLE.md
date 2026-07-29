# 이미지 프롬프트 스타일 가이드

카드에 들어가는 이미지는 두 종류뿐이고, 각각 고정된 룩을 유지한다.
날짜별 프롬프트는 `prompts/<날짜>.md` 에 남긴다.

## A. 헤드라인 사진 (`headline.image`)

실제 신문 1면 사진처럼 보이는 **실사 보도사진**.

- 비율 3:2 가로, 최소 1536×1024
- 자연광 / 현장광, 다큐멘터리 톤, 과한 후보정 금지
- 인물은 뒷모습·실루엣·손만 — **알아볼 수 있는 얼굴 금지**
- 실존 기업 로고, 실제 인물, 실제 기관 간판 금지
- 앞쪽에 주제를 설명하는 소품 하나(서류, 단말기, 현수막 등)를 배치하면 1면 사진 느낌이 산다
- 한글 문구를 넣을 거면 짧은 한 줄만 (긴 문장은 글자가 깨진다)

공통 꼬리말:

```
photorealistic editorial news photograph, Korean newspaper front page,
natural available light, documentary style, 35mm lens, shallow depth of field,
no recognizable faces, no real brand logos, no watermark
--ar 3:2
```

## B. 보조기사 배너 (`sub_articles[].image`)

카드 위에 가로로 깔리는 **플랫 카툰 일러스트 배너**.

- 비율 약 21:9 가로 (렌더링 시 높이 110px로 잘리므로 세로로 긴 구도 금지)
- 두꺼운 짙은 갈색 외곽선 + 광택 있는 그라데이션 셰이딩 (스티커/게임 아이콘 느낌)
- 오브젝트는 **2개 그룹**: 왼쪽에 큰 상징물 하나, 오른쪽에 작은 오브젝트 묶음
- 가운데는 비워둔다 (배경만)
- 배경은 **따뜻한 골드~올리브 그라데이션** 고정 — 카드 색이 달라도 시리즈 통일감을 위해 유지
- **글자·숫자 절대 넣지 않기**

공통 꼬리말:

```
flat cartoon vector illustration, thick dark brown outlines, glossy gradient shading,
game icon sticker style, warm golden olive gradient background, empty space in the center,
two object groups (one large on the left, a small cluster on the right),
no text, no letters, no numbers, no watermark
--ar 21:9
```

## C. 선택 슬롯

`core_news.image`(카드1 하단 삽화), `must_read_image`(작은 뱃지), `summary_image`(작은 아이콘)은
비워두면 자동으로 이모지/플레이스홀더가 들어간다. 넣을 거면 B 스타일에 배경 투명으로 뽑는다.
