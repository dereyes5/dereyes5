from html import escape
from datetime import date

b, t = date(2002, 7, 16), date.today()
m = (t.year - b.year) * 12 + t.month - b.month - (t.day < b.day)
d = (t - date(b.year + (b.month - 1 + m) // 12, (b.month - 1 + m) % 12 + 1, b.day)).days
UPTIME = f"{m // 12} years, {m % 12} months, {d} days"

W = 58  # ancho columna derecha en caracteres

info = [
    ("title", "david@reyes"),
    ("OS", "Ubuntu 26.04, Windows 11"),
    ("Uptime", UPTIME),
    ("Host", "Tecnihealth"),
    ("Kernel", "Software Developer"),
    ("IDE", "VS Code, Claude Code"),
    ("Education", "ESPE - Ing. TI"),
    ("", ""),
    ("Languages.Programming", "PHP, JavaScript, TypeScript, Java"),
    ("Languages.Computer", "Python, HTML, CSS, SQL, Shell"),
    ("Languages.Real", "Spanish, English"),
    ("", ""),
    ("Frameworks.Backend", "Laravel, Spring Boot, Node.js"),
    ("Frameworks.Frontend", "Vue, React, Bootstrap"),
    ("Infra", "PostgreSQL, Docker, Nginx, Apache"),
    ("", ""),
    ("section", "Contact"),
    ("Email", "estebanreyes36@gmail.com"),
    ("LinkedIn", "linkedin.com/in/david-reyes-b20a2680"),
    ("Hobbies", "Gaming"),
    ("", ""),
    ("section", "GitHub Stats"),
    ("stats1", ""),
    ("stats2", ""),
]

ascii_art = [
    "              .,-:;//;:=,               ",
    "          . :H@@@MM@M#H/.,+%;,          ",
    "       ,/X+ +M@@M@MM%=,-%HMMM@X/,      ",
    "     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-    ",
    "    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.  ",
    "  ,%MM@@MH ,@%=             .---=-=:=,. ",
    "  =@#@@@MX.,                -%HX$$%%%:; ",
    " =-./@M@M$                   .;@MMMM@MM:",
    " X@/ -$MM/                    . +MM@@@M$",
    ",@M@H: :@:                    . =X#@@@@-",
    ",@@@MMX, .                    /H- ;@M@M=",
    ".H@@@@M@+,                    %MM+..%#$.",
    " /MMMM@MMH/.                  XM@MH; =; ",
    "  /%+%$XHH@$=              , .H@@@@MX,  ",
    "   .=--------.           -%H.,@@@@@MX,  ",
    "   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.  ",
    "     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=    ",
    "       =%@M@M#@$-.=$@MM@@@M; %M%=       ",
    "         ,:+$+-,/H#MMMMMMM@= =,         ",
    "               =++%%%%+/:-.             ",
]

THEMES = {
    "dark": dict(bg="#161b22", fg="#c9d1d9", key="#ffa657", val="#a5d6ff", dot="#616e7f", add="#3fb950", rem="#f85149"),
    "light": dict(bg="#f6f8fa", fg="#24292f", key="#953800", val="#0a3069", dot="#c2cfde", add="#1a7f37", rem="#cf222e"),
}


def line(key, val, t):
    dots = W - len(key) - len(val) - 4
    return (f'. <tspan fill="{t["key"]}">{escape(key)}</tspan>:'
            f'<tspan fill="{t["dot"]}"> {"." * dots} </tspan>'
            f'<tspan fill="{t["val"]}">{escape(val)}</tspan>')


def header(text):
    return f'{escape(text)} {"—" * (W - len(text) - 4)}-—-'


def build(t):
    rows = []
    for k, v in info:
        if k == "title":
            rows.append(f'<tspan fill="{t["fg"]}">{header(v)}</tspan>')
        elif k == "section":
            rows.append(f'- {header(v)}')
        elif k == "stats1":
            left = f'. <tspan fill="{t["key"]}">Repos</tspan>:<tspan fill="{t["dot"]}"> .... </tspan><tspan fill="{t["val"]}">27</tspan> {{<tspan fill="{t["key"]}">Private</tspan>: <tspan fill="{t["val"]}">7</tspan>}} | <tspan fill="{t["key"]}">Stars</tspan>:<tspan fill="{t["dot"]}"> ......... </tspan><tspan fill="{t["val"]}">1</tspan>'
            rows.append(left)
        elif k == "stats2":
            rows.append(f'. <tspan fill="{t["key"]}">Commits</tspan>:<tspan fill="{t["dot"]}"> .............. </tspan><tspan fill="{t["val"]}">XXX</tspan> | <tspan fill="{t["key"]}">Followers</tspan>:<tspan fill="{t["dot"]}"> ...... </tspan><tspan fill="{t["val"]}">2</tspan>')
        elif k == "":
            rows.append(f'<tspan fill="{t["dot"]}">.</tspan>')
        else:
            rows.append(line(k, v, t))

    lh, y0 = 20, 30
    art = "\n".join(f'<tspan x="15" y="{y0 + i * lh}">{escape(a)}</tspan>' for i, a in enumerate(ascii_art))
    txt = "\n".join(f'<tspan x="390" y="{y0 + i * lh}">{r}</tspan>' for i, r in enumerate(rows))
    h = y0 + len(rows) * lh
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" font-family="ConsolasFallback,Consolas,'DejaVu Sans Mono',monospace" width="985" height="{h}" viewBox="0 0 985 {h}" font-size="15px">
<style>text, tspan {{white-space: pre;}}</style>
<rect width="985" height="{h}" fill="{t["bg"]}" rx="15"/>
<text fill="{t["fg"]}" class="ascii">
{art}
</text>
<text fill="{t["fg"]}">
{txt}
</text>
</svg>
'''


for name, t in THEMES.items():
    with open(f"{name}_mode.svg", "w") as f:
        f.write(build(t))
