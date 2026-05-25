#!/usr/bin/env python3
"""Rebuild all mail/*.html from trade/withdraw_success_zh.html shell; strip <style>, inline-only."""

import re
from pathlib import Path
from typing import List, Optional

ROOT = Path(__file__).resolve().parent
REF_PATH = ROOT / "trade" / "withdraw_success_zh.html"
SKIP = {REF_PATH.resolve()}

HERO_FALLBACK_ZH = "https://aws-msx-assets.s3.ap-southeast-1.amazonaws.com/uploads/activity/20260401/f7703d810b4b4385b499ea72d47f259c.png"
HERO_FALLBACK_EN = "https://aws-msx-assets.s3.ap-southeast-1.amazonaws.com/uploads/activity/20260401/aa8d531f9f9f4fa0879d26e8dfbeed71.png"


def strip_style(html: str) -> str:
    return re.sub(r"<style\b[^>]*>[\s\S]*?</style>", "", html, flags=re.I)


def strip_class(html: str) -> str:
    html = re.sub(r'\sclass\s*=\s*"[^"]*"', "", html)
    html = re.sub(r"\sclass\s*=\s*'[^']*'", "", html)
    return html


def fix_flex_td(html: str) -> str:
    html = re.sub(
        r"display:\s*flex;\s*justify-items:\s*center;\s*justify-content:\s*center;",
        "text-align: center;",
        html,
        flags=re.I,
    )
    html = re.sub(r"display:\s*flex;", "text-align: center;", html, flags=re.I)
    return html


def extract_title(html: str) -> str:
    m = re.search(r"<title>([\s\S]*?)</title>", html, re.I)
    return m.group(1).strip() if m else "MSX"


def extract_lang(html: str) -> str:
    m = re.search(r'<html[^>]*\blang="([^"]*)"', html, re.I)
    return m.group(1).strip() if m else "zh"


def first_hero_src(html: str) -> Optional[str]:
    for m in re.finditer(
        r'<img[^>]+src="(https://mystonks\.org/files/uploads/activity/[^"]+\.png)"[^>]*>',
        html,
        re.I,
    ):
        return m.group(1)
    return None


def extract_content_box_inner_table(html: str) -> Optional[str]:
    marker = '<td class="content-box">'
    idx = html.find(marker)
    if idx == -1:
        idx = html.find('<td class="content-box"')
        if idx == -1:
            return None
        gt = html.find(">", idx)
        if gt == -1:
            return None
        start = gt + 1
    else:
        start = idx + len(marker)

    while start < len(html) and html[start] in " \n\t\r":
        start += 1
    if start + 6 >= len(html) or html[start : start + 6].lower() != "<table":
        return None

    i = start
    depth = 0
    while i < len(html):
        if html[i : i + 6].lower() == "<table":
            depth += 1
            j = html.find(">", i)
            if j == -1:
                return None
            i = j + 1
        elif html[i : i + 8].lower() == "</table>":
            depth -= 1
            i += 8
            if depth == 0:
                return html[start:i]
        else:
            i += 1
    return None


def is_en_path(path: Path) -> bool:
    p = path.as_posix()
    return "/en/" in p or path.name.endswith("_en.html")


def build_prefix(ref_lines: List[str], title: str, lang: str, hero: str) -> str:
    prefix = "".join(ref_lines[:70])
    prefix = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", prefix, count=1, flags=re.I)
    prefix = re.sub(r'<html lang="[^"]*"', f'<html lang="{lang}"', prefix, count=1, flags=re.I)
    prefix = re.sub(
        r'(src=")(https://mystonks\.org/files/uploads/activity/[^"]+\.png)',
        rf"\g<1>{hero}",
        prefix,
        count=1,
    )
    return prefix


def main() -> None:
    ref_text = REF_PATH.read_text(encoding="utf-8")
    ref_lines = ref_text.splitlines(keepends=True)

    main_open = "".join(ref_lines[70:72])
    main_close = """                    </td>
                  </tr>
                </table>
              </td>
            </tr>

"""
    suffix_zh = "".join(ref_lines[242:624])
    suffix_en = suffix_zh
    suffix_en = suffix_en.replace(
        "使用 MSX APP，随时随地进行交易",
        "Trade anytime, anywhere with the MSX APP",
    )
    suffix_en = suffix_en.replace(
        "感谢您选择MSX，如有任何问题或建议，请联系MSX客服",
        "Thank you for choosing MSX. If you have any questions or feedback, please contact MSX Customer Support.",
    )
    suffix_en = suffix_en.replace("版权所有 © 2026 保留所有权利", "Copyright © 2026. All rights reserved.")
    tail = "".join(ref_lines[624:630])

    ok, fail = 0, []
    for path in sorted(ROOT.rglob("*.html")):
        if path.resolve() in SKIP:
            continue
        raw = path.read_text(encoding="utf-8")
        title = extract_title(raw)
        lang = extract_lang(raw)
        cleaned = strip_style(raw)
        inner = extract_content_box_inner_table(cleaned)
        if not inner:
            fail.append((path, "no content-box table"))
            continue
        inner = strip_class(inner)
        inner = fix_flex_td(inner)
        hero = first_hero_src(cleaned) or (HERO_FALLBACK_EN if is_en_path(path) else HERO_FALLBACK_ZH)
        prefix = build_prefix(ref_lines, title, lang, hero)
        suffix = suffix_en if is_en_path(path) else suffix_zh
        out = prefix + main_open + inner + main_close + suffix + tail
        out = strip_class(out)
        path.write_text(out, encoding="utf-8")
        ok += 1

    print(f"ok {ok}")
    for p, reason in fail:
        print(f"FAIL {p.relative_to(ROOT)}: {reason}")


if __name__ == "__main__":
    main()
