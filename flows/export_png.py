from playwright.sync_api import sync_playwright
from pathlib import Path

FLOWS_DIR = Path(__file__).parent
OUTPUT_DIR = FLOWS_DIR / "png"
OUTPUT_DIR.mkdir(exist_ok=True)

HTML_FILES = [
    "flow-plan-lifecycle.html",
    "flow-required-designated.html",
    "flow-required-selfenroll.html",
    "flow-elective-system.html",
    "flow-elective-external.html",
    "flow-credit-review.html",
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 800}, device_scale_factor=2)
    for html_file in HTML_FILES:
        src = FLOWS_DIR / html_file
        png_name = src.stem + ".png"
        url = src.as_uri()
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(500)
        page.screenshot(path=str(OUTPUT_DIR / png_name), full_page=True)
        print(f"✓ {png_name}")
    browser.close()

print(f"\n全部完成，共导出 {len(HTML_FILES)} 张图片到 {OUTPUT_DIR}")
