"""Prototype charte v7 « moderne » : 6 slides du carrousel message suspect."""
import pathlib, sys
from playwright.sync_api import sync_playwright
from PIL import Image

REPO = pathlib.Path("/home/user/valorislab-media")
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
GRAD = sys.argv[2] if len(sys.argv) > 2 else "linear-gradient(100deg,#2E9E8A 0%,#7FBF7A 45%,#EDB24A 100%)"
F = REPO / "kit/fonts"
S = REPO / "kit/assets/scenes"

CSS = f"""
@font-face{{font-family:I;font-weight:400;src:url(file://{F}/inter-latin-400-normal.woff2)}}
@font-face{{font-family:I;font-weight:500;src:url(file://{F}/inter-latin-500-normal.woff2)}}
@font-face{{font-family:I;font-weight:600;src:url(file://{F}/inter-latin-600-normal.woff2)}}
@font-face{{font-family:I;font-weight:700;src:url(file://{F}/inter-latin-700-normal.woff2)}}
@font-face{{font-family:I;font-weight:800;src:url(file://{F}/inter-latin-800-normal.woff2)}}
@font-face{{font-family:J;font-weight:700;src:url(file://{F}/plus-jakarta-sans-latin-700-normal.woff2)}}
@font-face{{font-family:J;font-weight:800;src:url(file://{F}/plus-jakarta-sans-latin-800-normal.woff2)}}
:root{{--bg:#F7F2EC;--ink:#16130F;--mute:#6E665C;--grad:{GRAD};--card:#fff}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;background:var(--bg);color:var(--ink);font-family:I,sans-serif;overflow:hidden}}
.s{{position:relative;width:1080px;height:1350px;overflow:hidden;
  background:radial-gradient(900px 700px at 85% 10%,#fff 0,transparent 70%),var(--bg)}}
.pad{{position:absolute;left:72px;right:72px;top:84px}}
h1{{font-weight:800;text-transform:uppercase;font-size:92px;line-height:.98;letter-spacing:-.045em}}
.hl{{display:inline-block;font-family:J;font-weight:800;text-transform:none;letter-spacing:-.02em;color:#fff;
  background:var(--grad);border-radius:18px;padding:.04em .26em .1em;font-size:.72em;transform:rotate(-2deg);
  box-shadow:0 10px 30px rgba(46,158,138,.25);vertical-align:.08em}}
.sub{{margin-top:30px;font-size:38px;line-height:1.32;color:var(--mute);letter-spacing:-.01em;max-width:900px}}
.sub b{{color:var(--ink);font-weight:700}}
.badge{{display:inline-flex;align-items:center;gap:16px;background:var(--ink);color:#fff;border-radius:999px;
  padding:12px 30px 12px 12px;font-weight:700;font-size:30px;letter-spacing:.06em;margin-bottom:34px}}
.badge i{{width:44px;height:44px;border-radius:50%;background:var(--grad);display:grid;place-items:center;font-style:normal;font-size:24px}}
.brand{{position:absolute;left:72px;bottom:178px;font-weight:800;font-size:22px;letter-spacing:.22em;color:var(--mute)}}
.next{{position:absolute;right:72px;bottom:176px;display:flex;align-items:center;gap:18px;background:var(--grad);color:#fff;
  font-family:J;font-weight:800;font-size:36px;border-radius:999px;padding:14px 14px 14px 36px;box-shadow:0 14px 34px rgba(0,0,0,.14)}}
.next span{{width:58px;height:58px;border-radius:50%;background:var(--ink);display:grid;place-items:center;font-size:30px}}
/* phone */
.glow{{position:absolute;width:760px;height:760px;border-radius:50%;background:radial-gradient(closest-side,rgba(127,191,122,.28),rgba(237,178,74,.12) 60%,transparent);filter:blur(10px)}}
.phone{{position:absolute;width:520px;height:620px;border-radius:68px;background:#111;padding:14px;
  box-shadow:0 40px 80px rgba(40,30,20,.25),0 0 0 2px #2a2a2a inset}}
.scr{{width:100%;height:100%;border-radius:52px;background:#F4F4F6;overflow:hidden;position:relative;padding:62px 22px 20px}}
.isl{{position:absolute;top:16px;left:50%;transform:translateX(-50%);width:130px;height:36px;border-radius:20px;background:#111}}
.tm{{position:absolute;top:20px;left:40px;font-weight:700;font-size:22px}}
.ch{{display:flex;align-items:center;gap:14px;padding:8px 6px 18px;border-bottom:1px solid #e3e3e8;margin-bottom:18px}}
.av{{width:54px;height:54px;border-radius:50%;background:#cfd3da;display:grid;place-items:center;font-weight:700;color:#fff;font-size:24px}}
.ch b{{display:block;font-size:27px}} .ch small{{font-size:18px;color:#8a8a92}}
.m{{max-width:80%;font-size:30px;line-height:1.3;padding:16px 20px;border-radius:26px;margin-bottom:14px}}
.them{{background:#fff;border-bottom-left-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,.05)}}
.me{{background:#2E9E8A;color:#fff;margin-left:auto;border-bottom-right-radius:8px}}
.m.alert{{outline:4px solid #EDB24A;outline-offset:3px}}
/* annotations */
.ann{{position:absolute;display:flex;align-items:center;gap:20px;background:var(--ink);color:#fff;border-radius:999px;
  padding:14px 34px 14px 14px;font-weight:600;font-size:30px;line-height:1.15;box-shadow:0 16px 36px rgba(0,0,0,.18)}}
.ann i{{flex:none;width:56px;height:56px;border-radius:50%;background:var(--grad);display:grid;place-items:center;font-style:normal;font-size:28px}}
/* app window */
.win{{position:absolute;background:#fff;border-radius:34px;box-shadow:0 30px 70px rgba(40,30,20,.16);overflow:hidden}}
.wbar{{display:flex;gap:10px;align-items:center;padding:20px 26px;border-bottom:1px solid #eee;font-size:22px;color:#777}}
.wbar u{{width:14px;height:14px;border-radius:50%;background:#e4dfd8;text-decoration:none}}
.cards{{position:absolute;left:72px;right:72px;display:grid;gap:22px}}
.card{{background:#fff;border-radius:30px;padding:36px 36px;display:flex;gap:26px;align-items:center;box-shadow:0 14px 34px rgba(40,30,20,.08);font-size:38px;font-weight:600}}
.card i{{flex:none;width:64px;height:64px;border-radius:20px;background:var(--grad);color:#fff;display:grid;place-items:center;font-style:normal;font-weight:800;font-size:30px}}
.src{{position:absolute;left:72px;right:72px;bottom:290px;font-size:22px;color:var(--mute)}}
.photo{{position:absolute;inset:0;background-size:cover;background-position:center}}
.fade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(247,242,236,.92) 0,rgba(247,242,236,.55) 22%,rgba(247,242,236,0) 38%)}}
.tag{{position:absolute;left:72px;bottom:270px;background:rgba(22,19,15,.86);color:#fff;border-radius:999px;font-size:22px;font-weight:600;padding:10px 22px}}
.bubble{{position:absolute;left:72px;bottom:330px;width:500px;background:#fff;border-radius:34px;border-bottom-left-radius:10px;padding:26px 30px;
  font-size:32px;line-height:1.3;font-weight:500;box-shadow:0 24px 60px rgba(0,0,0,.22);transform:rotate(-3deg)}}
.bubble small{{display:block;font-size:20px;color:#999;margin-bottom:8px;font-weight:600}}
.band{{position:absolute;left:0;right:0;bottom:0;height:430px;background:rgba(32,26,22,.94);color:#fff;text-align:center;padding-top:56px}}
.band .big{{display:inline-flex;align-items:center;gap:22px;font-weight:800;font-size:64px;letter-spacing:-.03em}}
.band .big span{{background:#F7F2EC;color:var(--ink);border-radius:20px;padding:4px 22px 10px}}
.band p{{margin-top:22px;font-size:32px;font-weight:500}} .band small{{display:block;margin-top:18px;font-size:22px;color:#c9c0b4}}
"""

def phone(x, y, time, msgs, contact="Inconnu", status="Conversation fictive"):
    g = f'<div class="glow" style="left:{x-140}px;top:{y-80}px"></div>'
    m = "".join(f'<div class="m {c}">{t}</div>' for c, t in msgs)
    return g + f'''<div class="phone" style="left:{x}px;top:{y}px"><div class="scr"><div class="isl"></div><div class="tm">{time}</div>
<div class="ch"><div class="av">?</div><div><b>{contact}</b><small>{status}</small></div></div>{m}</div></div>'''

def ann(x, y, text, w=None):
    st = f"left:{x}px;top:{y}px" + (f";width:{w}px" if w else "")
    return f'<div class="ann" style="{st}"><i>←</i><span>{text}</span></div>'

NEXT = '<div class="next">{t}<span>→</span></div>'
BRAND = '<div class="brand">VALORISLAB</div>'

slides = []
# 1 cover
slides.append(f'''<div class="s"><div class="photo" style="background-image:url(file://{S}/ia-cover-message-suspect-v7.jpg)"></div><div class="fade"></div>
<div class="pad"><h1 style="font-size:116px">Tu vois<br>le piège ?</h1><div style="margin-top:22px"><span class="hl" style="font-size:66px">dans ce message</span></div></div>
<div class="bubble"><small>Inconnu · 21:47</small>Salut ! J'ai doublé mon argent en 3 semaines, je te montre ?</div>
<div class="tag">Conversation fictive</div>
{NEXT.format(t="je te montre")}</div>''')
# 2 signal 1
slides.append(f'''<div class="s"><div class="pad"><div class="badge"><i>1</i>SIGNAL 1</div>
<h1>Un gain trop beau <span class="hl">pour être vrai.</span></h1>
<p class="sub">« +100 % en 3 semaines », puis on te propose de <b>commencer petit</b>.</p></div>
{phone(80, 540, "21:47", [("them alert","Je trade la crypto. +100&nbsp;% en 3&nbsp;semaines&nbsp;!"),("them","Commence avec 250&nbsp;€, je te guide.")])}
{ann(545, 660, "un gain promis,<br>et vite")}{ann(545, 860, "une petite mise<br>pour te ferrer")}
{NEXT.format(t="la suite")}</div>''')
# 3 signal 2
slides.append(f'''<div class="s"><div class="pad"><div class="badge"><i>2</i>SIGNAL 2</div>
<h1>Des gains <span class="hl">affichés à l'écran.</span></h1>
<p class="sub">Deux jours plus tard, ton compte montre <b>+40 %</b>. Ça rassure : c'est fait pour.</p></div>
<div class="win" style="left:72px;top:540px;width:620px"><div class="wbar"><u></u><u></u><u></u>&nbsp;plateforme fictive</div>
<div style="padding:34px 38px 40px"><div style="font-size:24px;color:#888">Ton solde</div>
<div style="font-weight:800;font-size:96px;letter-spacing:-.04em">350 €</div>
<div style="display:inline-block;margin-top:10px;background:#E3F4EE;color:#1F7A69;font-weight:700;font-size:30px;border-radius:999px;padding:8px 22px">▲ +40 %</div>
<svg viewBox="0 0 520 150" style="margin-top:26px;width:100%"><path d="M0 140 C80 130 120 120 170 100 S260 90 300 70 S420 30 520 12" fill="none" stroke="#2E9E8A" stroke-width="7" stroke-linecap="round"/></svg></div></div>
{ann(580, 600, "des chiffres<br>tapés au clavier", 430)}{ann(580, 900, "un argent<br>impossible à retirer", 430)}
{NEXT.format(t="et là…")}</div>''')
# 4 signal 3
slides.append(f'''<div class="s"><div class="pad"><div class="badge"><i>3</i>SIGNAL 3</div>
<h1>Payer pour <span class="hl">retirer ses gains.</span></h1>
<p class="sub">Tu veux récupérer ton argent ? On te réclame <b>15 % de frais</b> d'abord.</p></div>
{phone(80, 540, "18:20", [("me","Top, je retire mes gains."),("them alert","Pour retirer, paie d'abord 15&nbsp;% de frais.")])}
{ann(545, 820, "le piège<br>se referme ici")}
{NEXT.format(t="la réponse")}</div>''')
# 5 reveal
slides.append(f'''<div class="s"><div class="pad"><div class="badge"><i>✓</i>CE QUE DIT LA FSMA</div>
<h1>C'est une fausse <span class="hl">plateforme.</span></h1>
<p class="sub">Gains affichés, retrait bloqué, frais réclamés : <b>le schéma décrit par la FSMA</b>.</p></div>
<div class="cards" style="top:560px">
<div class="card"><i>1</i>Ne paie rien de plus.</div>
<div class="card"><i>2</i>Préviens tout de suite ta banque.</div>
<div class="card"><i>3</i>Porte plainte à la police.</div><div style="font-size:22px;color:var(--mute);padding:0 6px">Source : FSMA, mises en garde sur les plateformes de trading crypto.</div></div>

{NEXT.format(t="encore une")}</div>''')
# 6 CTA
slides.append(f'''<div class="s"><div class="photo" style="background-image:url(file://{S}/ia-cover-message-suspect-v6b.jpg);background-position:center 20%"></div><div class="fade"></div>
<div class="pad"><h1 style="font-size:84px">C'est l'une des<br>20 erreurs <span class="hl">du guide.</span></h1></div>
<div class="band"><div class="big">Guide gratuit <span>LIEN EN BIO</span></div>
<p>Les 20 erreurs à éviter quand on débute.</p><small>valorislab.be · Contenu éducatif, pas un conseil financier</small></div></div>''')

OUT.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
    for i, body in enumerate(slides, 1):
        h = OUT / f"s{i}.html"; h.write_text(f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>", encoding="utf-8")
        pg.goto(h.resolve().as_uri()); pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(250)
        # mesure : rien ne sort du cadre, rien dans les 160 px du bas (sauf fonds)
        bad = pg.evaluate("""()=>[...document.querySelectorAll('h1,.sub,.ann,.phone,.win,.card,.next,.bubble,.badge,.src,.tag,.band .big')].map(e=>{const r=e.getBoundingClientRect();return [e.className||e.tagName,Math.round(r.left),Math.round(r.right),Math.round(r.bottom)]}).filter(([c,l,r,b])=>l<40||r>1040||b>1190)""")
        over = pg.evaluate("""()=>{const a=[...document.querySelectorAll('.ann,.phone,.win,.card,.next,.bubble,.tag,.sub,h1,.src')].map(e=>[e.className||e.tagName,e.getBoundingClientRect()]);const o=[];for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++){const[x,r]=a[i],[y,s]=a[j];if(!((x.includes('ann')&&(y.includes('phone')||y.includes('win')))||(y.includes('ann')&&(x.includes('phone')||x.includes('win'))))&&r.left<s.right&&s.left<r.right&&r.top<s.bottom&&s.top<r.bottom)o.push(x+' x '+y)}return o}""")
        print(i, "hors cadre:", bad, "chevauchements:", over)
        f = OUT / f"s{i}.png"
        pg.screenshot(path=str(f))
        Image.open(f).convert("RGB").resize((1080, 1350), Image.LANCZOS).save(OUT / f"feed-0{i}.jpg", quality=92)
    b.close()
