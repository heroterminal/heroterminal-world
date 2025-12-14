#!/usr/bin/env python3
"""
Generate a newspaper-style SVG from a plaintext input file.
Requires Jinja2 (fails if missing).
"""
import argparse
from pathlib import Path

import jinja2

JINJA_TEMPLATE = """<?xml version="1.0"?>
<svg width="800" height="1200" viewBox="0 0 800 1200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="paperNoise">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" seed="7" result="noise"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.08 0"/>
    </filter>
  </defs>

  <rect width="100%" height="100%" fill="#f7f1e3"/>
  <rect width="100%" height="100%" fill="transparent" filter="url(#paperNoise)" opacity="0.4" pointer-events="none"/>

  <foreignObject x="0" y="0" width="800" height="1200">
    <div xmlns="http://www.w3.org/1999/xhtml" style="height:100%; box-sizing:border-box; padding:50px;">
      <style>
        .newsletter {
          height: 100%;
          box-sizing: border-box;
          background: linear-gradient(180deg, rgba(0,0,0,0.03) 0%, rgba(0,0,0,0.01) 100%);
          color: #1c1c1c;
          font-family: 'Times New Roman', Georgia, serif;
          line-height: 1.45;
        }
        .masthead { text-align: center; margin-bottom: 16px; }
        .title {
          font-size: 40px; font-weight: 900; letter-spacing: 2px;
          border-bottom: 3px solid #1c1c1c; display: inline-block;
          padding-bottom: 6px; text-transform: uppercase;
        }
        .meta { font-style: italic; font-size: 14px; margin-top: 6px; color: #444; }
        .dateline { font-size: 12px; letter-spacing: 0.4px; margin-top: 2px; color: #666; }
        .section {
          column-count: 2; column-gap: 36px;
          font-size: 15px; text-align: justify; margin-top: 20px;
        }
        .footer {
          text-align: center; font-size: 11px; letter-spacing: 0.3px;
          margin-top: 30px; color: #555; border-top: 1px dashed #999; padding-top: 10px;
        }
      </style>

      <div class="newsletter">
        <div class="masthead">
          <div class="title">{{ title }}</div>
          <div class="meta">{{ subtitle }}</div>
          <div class="dateline">{{ dateline }}</div>
        </div>
        <div class="section">
          {{ body | safe }}
        </div>
        <div class="footer">{{ footer }}</div>
      </div>
    </div>
  </foreignObject>
</svg>
"""


def render_svg(title: str, subtitle: str, dateline: str, body_html: str, footer: str) -> str:
    env = jinja2.Environment(autoescape=False)
    tpl = env.from_string(JINJA_TEMPLATE)
    return tpl.render(title=title, subtitle=subtitle, dateline=dateline, body=body_html, footer=footer)


def main():
    parser = argparse.ArgumentParser(
        description="Render a newspaper-style SVG from a plaintext input using Jinja2.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("input", help="Input plaintext file")
    parser.add_argument("output", help="Output SVG file")
    parser.add_argument("--title", default="The Herald", help="Masthead/title")
    parser.add_argument("--subtitle", default="HeroTerminal Newswire", help="Subtitle/meta line")
    parser.add_argument("--dateline", default="Lyon · 1999", help="Dateline")
    parser.add_argument("--footer", default="Distributed by HeroTerminal Network", help="Footer text")

    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)

    title = args.title
    subtitle = args.subtitle
    dateline = args.dateline
    footer = args.footer

    body_text = in_path.read_text(encoding="utf-8").strip()

    # Convert double newlines to paragraph breaks, single newlines to <br/>
    body_html = body_text.replace("\n\n", "</p><p>")
    body_html = body_html.replace("\n", "<br/>")
    body_html = f"<p>{body_html}</p>"

    svg_content = render_svg(title, subtitle, dateline, body_html, footer)
    out_path.write_text(svg_content, encoding="utf-8")


if __name__ == "__main__":
    main()
