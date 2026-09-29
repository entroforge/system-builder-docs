#!/usr/bin/env python3
"""Generate the two accessible, Chinese-labelled SVG views of the REQ stage map."""

from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "public" / "images"

STAGES = {
    0: ("确认需求", "REQ", "人确认"),
    1: ("登记授权", "绑定记录", "人授权"),
    2: ("建立设计", "架构 · 场景", ""),
    3: ("统一约定", "契约", ""),
    4: ("安排工作", "任务", ""),
    5: ("独立核对", "审查结论", ""),
    6: ("构建接收", "共同版本", ""),
    7: ("完整验证", "验证结果", ""),
    8: ("查明原因", "根因", ""),
    9: ("有界修复", "修复 · 重验", ""),
    10: ("交付核对", "验收 · 审计", ""),
    11: ("决定发布", "人的决定", "人决定"),
}


def serialize(parts: list[str]) -> str:
    return "\n".join(line.rstrip() for line in "\n".join(parts).splitlines()) + "\n"


def svg_open(width: int, height: int, title: str, desc: str, mobile: bool = False) -> str:
    mobile_styles = '''
    .title{font-size:48px} .sub{font-size:27px} .group{font-size:36px}
    .stage{font-size:31px} .action{font-size:34px} .output{font-size:27px}
    .human{font-size:20px} .small{font-size:27px} .small-action{font-size:30px} .small-output{font-size:27px}
    .zone-title{font-size:29px}
    ''' if mobile else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(desc)}</desc>
  <defs>
    <pattern id="grain" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="4" cy="9" r="0.8" fill="#b9b5a9" opacity=".38"/><circle cx="22" cy="23" r=".65" fill="#b9b5a9" opacity=".25"/></pattern>
    <marker id="arrow" markerWidth="11" markerHeight="11" refX="8" refY="5.5" orient="auto" markerUnits="userSpaceOnUse"><path d="M2 2 L9 5.5 L2 9" fill="none" stroke="#38525c" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></marker>
    <marker id="orangeArrow" markerWidth="11" markerHeight="11" refX="8" refY="5.5" orient="auto" markerUnits="userSpaceOnUse"><path d="M2 2 L9 5.5 L2 9" fill="none" stroke="#cf744d" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></marker>
    <g id="paperIcon" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 7 Q10 8 10 13 L10 53 Q10 57 15 57 L48 57 Q53 56 53 52 L53 16 L44 7 Z"/><path d="M44 7 L44 17 L53 17"/><path d="M19 27 Q29 26 42 27 M19 35 Q30 36 42 35 M19 43 Q27 42 34 43"/></g>
    <g id="taskIcon" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 12 L46 12 L49 19 L14 19 Z M15 25 L50 25 L53 32 L18 32 Z M11 38 L46 38 L49 45 L14 45 Z"/><path d="M21 51 L45 51"/></g>
    <g id="checkIcon" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 29 L22 39 L47 15 M11 51 Q31 55 52 48"/><circle cx="31" cy="29" r="24"/></g>
    <g id="sealIcon" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 16 Q30 10 47 17 L47 49 Q30 54 14 49 Z M22 32 L29 39 L40 25"/><path d="M20 54 Q32 57 46 54"/></g>
    <g id="loopIcon" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M47 20 Q30 7 15 24 L14 15 M15 24 L24 22 M16 42 Q33 56 49 39 L50 49 M49 39 L40 42"/></g>
  </defs>
  <style>
    .bg{{fill:#fbf7ed}} .ink{{fill:#2e434b}} .muted{{fill:#62747a}} .orange{{fill:#c66c48}}
    .title{{font:700 40px 'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC',sans-serif;letter-spacing:1px}}
    .sub{{font:400 19px 'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC',sans-serif}}
    .group{{font:700 33px 'STKaiti','Kaiti SC','PingFang SC',sans-serif}}
    .stage{{font:700 24px 'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC',sans-serif}}
    .action{{font:700 29px 'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC',sans-serif}}
    .output{{font:500 25px 'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC',sans-serif}}
    .small-output{{font:500 19px 'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC',sans-serif}}
    .human{{font:600 20px 'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC',sans-serif}}
    .small{{font:500 18px 'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC',sans-serif}}
    .small-action{{font:700 22px 'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC',sans-serif}}
    .zone-title{{font:700 23px 'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC',sans-serif}}
    {mobile_styles}
  </style>
  <rect class="bg" width="{width}" height="{height}"/>
  <rect width="{width}" height="{height}" fill="url(#grain)"/>
'''


def box(x: int, y: int, w: int, h: int, fill: str, stroke: str = "#527079") -> str:
    # Slightly uneven corners make the geometry feel drawn by hand without distorting text.
    d = f"M{x+12} {y+2} Q{x+2} {y+4} {x+2} {y+15} L{x+1} {y+h-17} Q{x+3} {y+h-2} {x+19} {y+h-2} L{x+w-16} {y+h-1} Q{x+w-1} {y+h-4} {x+w-2} {y+h-20} L{x+w-1} {y+17} Q{x+w-3} {y+1} {x+w-19} {y+2} Z"
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'


def phase_zone(x: int, y: int, w: int, h: int, title: str, fill: str, stroke: str) -> str:
    return f'''<g>
  <path d="M{x+18} {y+2} Q{x+2} {y+4} {x+2} {y+18} L{x+2} {y+h-20} Q{x+3} {y+h-2} {x+21} {y+h-2} L{x+w-20} {y+h-2} Q{x+w-2} {y+h-4} {x+w-2} {y+h-22} L{x+w-2} {y+18} Q{x+w-4} {y+2} {x+w-20} {y+2} Z" fill="{fill}" fill-opacity=".35" stroke="{stroke}" stroke-width="3" stroke-dasharray="10 10" stroke-linecap="round"/>
  <rect x="{x+16}" y="{y+3}" width="{len(title)*32+15}" height="29" fill="#fbf7ed"/>
  <text x="{x+21}" y="{y+27}" class="zone-title ink">{escape(title)}</text>
</g>'''


def review_target(x: int, y: int, w: int, h: int, card_start: int) -> str:
    center = x + w // 2
    return f'''<g>
  {box(x, y, w, h, "#dcebe6", "#8aada5")}
  <path d="M{center} {card_start-4} Q{center-3} {y+h+20} {center} {y+h+8}" fill="none" stroke="#547d78" stroke-width="4" stroke-linecap="round"/>
  <path d="M{center-12} {y+h+20} L{center} {y+h+7} L{center+12} {y+h+20}" fill="none" stroke="#547d78" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
</g>'''


def group(x: int, y: int, w: int, h: int, title: str, number: str, icon: str, fill: str) -> str:
    return f'''<g>
  {box(x, y, w, h, fill)}
  <text x="{x+25}" y="{y+46}" class="group ink">{escape(title)}</text>
  <path d="M{x+25} {y+56} Q{x+90} {y+52} {x+169} {y+57}" fill="none" stroke="#77a39d" stroke-width="3" stroke-linecap="round"/>
  <text x="{x+w-80}" y="{y+45}" text-anchor="end" class="small muted">{escape(number)}</text>
  <use href="#{icon}" x="{x+w-65}" y="{y+13}" width="48" height="48" style="color:#608c88"/>
</g>'''


def card(x: int, y: int, w: int, h: int, number: int) -> str:
    action, output, human = STAGES[number]
    pill_width = min(w - 95, max(86, 24 + len(output) * 19))
    human_label = ''
    if human:
        human_label = f'''<path d="M{x+w-102} {y+15} Q{x+w-100} {y+10} {x+w-92} {y+10} L{x+w-13} {y+10} Q{x+w-8} {y+11} {x+w-8} {y+18} L{x+w-10} {y+36} L{x+w-101} {y+35} Z" fill="#f8e2d7" stroke="#dfb29c" stroke-width="1.4"/>
  <text x="{x+w-55}" y="{y+28}" text-anchor="middle" class="human orange">{escape(human)}</text>'''
    return f'''<g>
  {box(x, y, w, h, "#fffdfa", "#8ba9a7")}
  <circle cx="{x+37}" cy="{y+39}" r="26" fill="#e3f0ea" stroke="#547d78" stroke-width="2.4"/>
  <text x="{x+37}" y="{y+46}" text-anchor="middle" class="stage ink">S{number}</text>
  <text x="{x+77}" y="{y+31}" class="action ink">{escape(action)}</text>
  {human_label}
  <path d="M{x+78} {y+47} Q{x+82} {y+43} {x+90} {y+44} L{x+78+pill_width} {y+44} Q{x+84+pill_width} {y+45} {x+84+pill_width} {y+52} L{x+83+pill_width} {y+69} L{x+79} {y+70} Z" fill="#edf3ef"/>
  <text x="{x+88}" y="{y+63}" class="output muted">{escape(output)}</text>
</g>'''


def small_card(x: int, y: int, w: int, number: int) -> str:
    action, output, _ = STAGES[number]
    return f'''<g>
  {box(x, y, w, 102, "#fffdfa", "#d19570")}
  <circle cx="{x+29}" cy="{y+32}" r="21" fill="#fae4d6" stroke="#c97852" stroke-width="2.3"/>
  <text x="{x+29}" y="{y+39}" text-anchor="middle" class="stage ink">S{number}</text>
  <text x="{x+58}" y="{y+39}" class="small-action ink">{escape(action)}</text>
  <path d="M{x+18} {y+64} Q{x+28} {y+60} {x+40} {y+62} L{x+w-24} {y+62} Q{x+w-13} {y+64} {x+w-17} {y+80} L{x+19} {y+82} Z" fill="#fdf0e6"/>
  <text x="{x+29}" y="{y+80}" class="small-output muted">{escape(output)}</text>
</g>'''


def desktop() -> str:
    parts = [svg_open(1800, 980, "一项 REQ 的工作路径", "S0 至 S5 是谋划：确定承诺、形成契约和任务，S5 回看 S3 与 S4 并追溯需求和设计。S6 至 S9 是实现与验证，发现问题时由 S7 进入 S8 调查、S9 修复，再返回新一轮 S7。S7 通过后进入 S10 和 S11。")]
    parts += ['<text x="72" y="77" class="title ink">一项 REQ 的工作路径</text>',
              '<text x="74" y="113" class="sub muted">每一步留下可追查的东西；小标签写的是这一阶段的产物</text>',
              '<path d="M73 132 Q230 127 413 132" fill="none" stroke="#d5e4dd" stroke-width="10" stroke-linecap="round"/>',
              phase_zone(45, 141, 770, 477, "谋划：把事情说清", "#e7f2e8", "#84a99f"),
              phase_zone(823, 141, 507, 774, "实施与验证", "#f9e9da", "#cb9b79")]
    groups = [(70, "确定承诺", "S0—S2", "paperIcon", "#f0f5ed"),
              (455, "安排工作", "S3—S5", "taskIcon", "#edf4f0"),
              (840, "完成并检查", "S6—S7", "checkIcon", "#f2f5ed"),
              (1350, "验收与决定", "S10—S11", "sealIcon", "#f4f1e9")]
    widths = [345, 345, 345, 380]
    for (x, title, num, icon, fill), w in zip(groups, widths):
        parts.append(group(x, 174, w, 415, title, num, icon, fill))
    for row, n in enumerate((0, 1, 2)):
        parts.append(card(91, 251+row*105, 303, 84, n))
    parts.append(review_target(465, 243, 324, 210, 492))
    for row, n in enumerate((3, 4)):
        parts.append(card(476, 251+row*105, 303, 84, n))
    parts.append(card(476, 492, 303, 84, 5))
    for row, n in enumerate((6, 7)):
        parts.append(card(861, 292+row*142, 303, 90, n))
    for row, n in enumerate((10, 11)):
        parts.append(card(1372, 292+row*142, 336, 90, n))
    parts += [
        '<path d="M417 375 Q435 370 450 375" fill="none" stroke="#38525c" stroke-width="4" stroke-linecap="round" marker-end="url(#arrow)"/>',
        '<path d="M802 375 Q821 370 835 375" fill="none" stroke="#38525c" stroke-width="4" stroke-linecap="round" marker-end="url(#arrow)"/>',
        '<path d="M1187 375 Q1252 366 1344 375" fill="none" stroke="#38525c" stroke-width="4" stroke-linecap="round" marker-end="url(#arrow)"/>',
        '<text x="1246" y="351" class="small muted">通过</text>',
        group(850, 655, 395, 235, "调查与修复", "S8—S9", "loopIcon", "#fff1e5"),
        small_card(876, 740, 159, 8),
        small_card(1057, 740, 161, 9),
        '<path d="M1038 789 Q1045 786 1051 789" fill="none" stroke="#cf744d" stroke-width="3.5" stroke-linecap="round" marker-end="url(#orangeArrow)"/>',
        '<path d="M932 526 Q925 590 924 649" fill="none" stroke="#cf744d" stroke-width="3.7" stroke-linecap="round" marker-end="url(#orangeArrow)"/>',
        '<text x="938" y="618" class="small orange">发现问题</text>',
        '<path d="M1222 787 Q1313 787 1312 713 L1312 603 Q1310 562 1273 559 L1174 559 Q1142 558 1146 530" fill="none" stroke="#cf744d" stroke-width="3.7" stroke-linecap="round" marker-end="url(#orangeArrow)"/>',
        '<text x="1135" y="628" class="small orange">新一轮 S7</text>',
        '<path d="M77 933 Q437 937 791 932" fill="none" stroke="#c5d7d1" stroke-width="2.2" stroke-dasharray="4 9" stroke-linecap="round"/>',
        '<text x="81" y="956" class="small muted">深色线：产物接力</text>',
        '<path d="M291 950 L341 950" fill="none" stroke="#cf744d" stroke-width="3" marker-end="url(#orangeArrow)"/>',
        '<text x="356" y="956" class="small muted">橙色线：发现后的纠错回路</text>',
        '<text x="1334" y="956" class="small muted">S11 批准后，发布仍由人执行</text>',
        '</svg>'
    ]
    return serialize(parts)


def mobile() -> str:
    parts = [svg_open(780, 2390, "一项 REQ 的工作路径，竖版", "S0 至 S5 是谋划，其中 S5 回看 S3 与 S4，并追溯需求和设计。S6 至 S9 是实现与验证；发现问题时进入 S8、S9，再返回新一轮 S7。S7 通过后进入 S10 和 S11。", mobile=True)]
    parts += ['<text x="47" y="73" class="title ink">一项 REQ 的工作路径</text>',
              '<text x="49" y="110" class="sub muted">小标签 = 这一阶段留下的产物</text>',
              '<g transform="translate(0 50)">',
              phase_zone(20, 115, 740, 932, "谋划：把事情说清", "#e7f2e8", "#84a99f"),
              phase_zone(20, 1055, 740, 790, "实施与验证", "#f9e9da", "#cb9b79")]
    specs = [(46, 154, 688, 414, "确定承诺", "S0—S2", "paperIcon", "#f0f5ed", (0,1,2)),
             (46, 621, 688, 414, "安排工作", "S3—S5", "taskIcon", "#edf4f0", (3,4,5)),
             (46, 1088, 688, 309, "完成并检查", "S6—S7", "checkIcon", "#f2f5ed", (6,7)),
             (46, 1910, 688, 309, "验收与决定", "S10—S11", "sealIcon", "#f4f1e9", (10,11))]
    for x,y,w,h,title,num,icon,fill,stages in specs:
        parts.append(group(x,y,w,h,title,num,icon,fill))
        if stages == (3,4,5):
            parts.append(review_target(x+14, y+74, w-28, 210, y+321))
            parts.append(card(x+25, y+82, w-50, 84, 3))
            parts.append(card(x+25, y+185, w-50, 84, 4))
            parts.append(card(x+25, y+321, w-50, 84, 5))
        else:
            for i,n in enumerate(stages):
                parts.append(card(x+25,y+82+i*103,w-50,84,n))
    parts += [
        '<path d="M390 570 Q387 595 390 615" fill="none" stroke="#38525c" stroke-width="4" stroke-linecap="round" marker-end="url(#arrow)"/>',
        '<path d="M390 1037 Q388 1063 390 1080" fill="none" stroke="#38525c" stroke-width="4" stroke-linecap="round" marker-end="url(#arrow)"/>',
        '<path d="M704 1398 Q740 1417 737 1464 L737 1830 Q735 1880 700 1901" fill="none" stroke="#38525c" stroke-width="4" stroke-linecap="round" marker-end="url(#arrow)"/>',
        '<text x="662" y="1460" class="small muted">通过</text>',
        group(73, 1485, 595, 334, "调查与修复", "S8—S9", "loopIcon", "#fff1e5"),
        small_card(103, 1573, 253, 8),
        small_card(385, 1573, 253, 9),
        '<path d="M359 1624 Q369 1620 380 1624" fill="none" stroke="#cf744d" stroke-width="3.7" stroke-linecap="round" marker-end="url(#orangeArrow)"/>',
        '<path d="M206 1375 Q169 1416 169 1478" fill="none" stroke="#cf744d" stroke-width="3.7" stroke-linecap="round" marker-end="url(#orangeArrow)"/>',
        '<text x="91" y="1450" class="small orange">发现问题</text>',
        '<path d="M620 1684 Q682 1681 686 1618 L686 1449 Q684 1412 637 1410 L556 1410 Q524 1412 525 1391" fill="none" stroke="#cf744d" stroke-width="3.7" stroke-linecap="round" marker-end="url(#orangeArrow)"/>',
        '<text x="484" y="1743" class="small orange">新一轮 S7</text>',
        '<text x="50" y="2283" class="small muted">深色线：产物接力　　橙色线：发现后重新验证</text>',
        '</g>',
        '</svg>'
    ]
    return serialize(parts)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "req-stage-map.svg").write_text(desktop(), encoding="utf-8")
    (OUT / "req-stage-map-mobile.svg").write_text(mobile(), encoding="utf-8")


if __name__ == "__main__":
    main()
