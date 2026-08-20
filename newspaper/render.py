#!/usr/bin/env python3
"""
매일 발행하는 '오늘의 1면 경제신문' 이미지를 생성한다.

사용법:
    python3 render.py data/2026-07-14.json
    python3 render.py data/2026-07-14.json --out output/2026-07-14.png

data 인자를 생략하면 data/sample.json 을 사용한다.
"""
import argparse
import base64
import json
import mimetypes
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
CHROMIUM_PATH = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
DEFAULT_CHARACTER_IMAGE = "assets/character-woman-cat.png"
THEMES = ("newspaper", "magazine", "dark")
DEFAULT_THEME = "newspaper"
SERIF_FONTS = {
    "font_serif_regular": "assets/fonts/NanumMyeongjo-Regular.woff2",
    "font_serif_bold": "assets/fonts/NanumMyeongjo-Bold.woff2",
}


def resolve_image(path: str) -> str:
    """로컬 상대경로를 base64 data URI로 변환한다 (헤드리스 크롬의 file:// 접근 제한 회피)."""
    if not path:
        return ""
    if path.startswith(("http://", "https://", "data:")):
        return path
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    if not p.exists():
        return path
    mime = mimetypes.guess_type(p.name)[0] or "image/png"
    encoded = base64.b64encode(p.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def resolve_font(path: str) -> str:
    """제목용 명조 웹폰트를 base64 data URI로 변환한다."""
    p = ROOT / path
    if not p.exists():
        return ""
    encoded = base64.b64encode(p.read_bytes()).decode("ascii")
    return f"data:font/woff2;base64,{encoded}"


def render_html(data: dict, theme: str | None = None) -> str:
    data = dict(data)
    data["theme"] = theme or data.get("theme") or DEFAULT_THEME

    for key, path in SERIF_FONTS.items():
        data[key] = resolve_font(path)

    for key in ("headline", "core_news", "ad"):
        if key in data:
            data[key] = dict(data[key])
            data[key]["image"] = resolve_image(data[key].get("image", ""))

    if "sub_articles" in data:
        data["sub_articles"] = [dict(s, image=resolve_image(s.get("image", ""))) for s in data["sub_articles"]]

    data["must_read_image"] = resolve_image(data.get("must_read_image", ""))
    data["summary_image"] = resolve_image(data.get("summary_image", ""))
    data["character_image"] = resolve_image(data.get("character_image", DEFAULT_CHARACTER_IMAGE))

    env = Environment(loader=FileSystemLoader(str(ROOT)))
    template = env.get_template("template.html.j2")
    return template.render(**data)


def html_to_png(html: str, out_path: Path):
    with sync_playwright() as p:
        launch_kwargs = {}
        if Path(CHROMIUM_PATH).exists():
            launch_kwargs["executable_path"] = CHROMIUM_PATH
        browser = p.chromium.launch(**launch_kwargs)
        page = browser.new_page(viewport={"width": 1080, "height": 1200})
        page.set_content(html, wait_until="load")
        page.screenshot(path=str(out_path), full_page=True)
        browser.close()


def main():
    parser = argparse.ArgumentParser(description="1면 경제신문 이미지 생성")
    parser.add_argument("data_file", nargs="?", default="data/sample.json",
                         help="신문 데이터 JSON 파일 경로 (기본: data/sample.json)")
    parser.add_argument("--out", default=None, help="출력 PNG 경로 (기본: output/<date>.png)")
    parser.add_argument("--theme", default=None, choices=THEMES,
                        help="지면 테마 (기본: newspaper=신문 1면형). magazine=매거진형, dark=다크 모드")
    args = parser.parse_args()

    data_path = ROOT / args.data_file if not Path(args.data_file).is_absolute() else Path(args.data_file)
    if not data_path.exists():
        print(f"데이터 파일을 찾을 수 없습니다: {data_path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(data_path.read_text(encoding="utf-8"))
    html = render_html(data, args.theme)

    if args.out:
        out_path = Path(args.out)
    else:
        safe_date = data.get("date", "output").replace(".", "-").replace(" ", "").replace("(", "").replace(")", "")
        theme = args.theme or data.get("theme") or DEFAULT_THEME
        suffix = "" if theme == DEFAULT_THEME else f"-{theme}"
        out_path = ROOT / "output" / f"{safe_date}{suffix}.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    html_to_png(html, out_path)
    print(f"이미지 생성 완료: {out_path}")


if __name__ == "__main__":
    main()
