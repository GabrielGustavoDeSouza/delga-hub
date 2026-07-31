import streamlit as st
from assets import LOGO_LIGHT_DATA_URI, BG_VIDEO_DATA_URI, BG_OVERLAY_DATA_URI

st.set_page_config(page_title="Delga HUB", page_icon="🏭", layout="wide",
                    initial_sidebar_state="collapsed")

NAVY = "#0B0F2B"
BLUE = "#1B2A9E"
BLUE2 = "#33459E"

# =====================================================================
# LINKS — preencha aqui conforme for tendo os endereços de cada solução.
# Um card com url=None aparece esmaecido, com "Em breve", sem clique —
# assim que preencher a url, ele vira um link normal sozinho.
#
# "Delga Projects" tem destaque=True — mesmo tamanho dos outros, só com
# a cor em gradiente pra chamar mais atenção. A ORDEM da lista é a ordem
# na grade (4 colunas): Projects entra na 2ª posição de propósito, pra
# ficar central na primeira fileira.
# =====================================================================
TODOS = [
    {"nome": "Delga Mobile", "sub": "App do Grupo Delga", "icone": "📱",
     "url": None},
    {"nome": "Delga Projects", "sub": "Redução de Custos & Performance", "icone": "📊",
     "url": "https://plataformadegest-odeprojetosdelga-2miazhybxebzwmz7nyvcgx.streamlit.app/",
     "destaque": True},
    {"nome": "Delga OEE", "sub": "Eficiência de Equipamentos", "icone": "⚙️",
     "botoes": [("Delga Sync", None), ("Delga Ega", None)]},
    {"nome": "Delga SGI", "sub": "Sistema de Gestão Integrada", "icone": "📁",
     "url": None},
    {"nome": "Delga Helps", "sub": "Chamados de Manutenção & TI", "icone": "🛠️",
     "botoes": [("Tractian", None), ("GLPI", None)]},
    {"nome": "Delga Academy", "sub": "Cursos Gupy & Treinamentos", "icone": "🎓",
     "url": None},
    {"nome": "Delga Logística", "sub": "Processos Logísticos", "icone": "🚚",
     "url": None},
    {"nome": "Delga Sell", "sub": "Cotações & Vendas", "icone": "💰",
     "url": None},
]

# =====================================================================
# Fundo: vídeo em loop + filtro azul por cima — cada tag numa linha só,
# sem indentação, pra não confundir o parser de Markdown do Streamlit
# (linha com 4+ espaços de indentação vira "bloco de código" e some o
# HTML — já vimos esse bug antes).
st.markdown(
    f'<video autoplay muted loop playsinline style="position:fixed;inset:0;width:100%;height:100%;object-fit:cover;z-index:-3;"><source src="{BG_VIDEO_DATA_URI}" type="video/mp4"></video>'
    f'<div style="position:fixed;inset:0;width:100%;height:100%;z-index:-2;background-image:url(\'{BG_OVERLAY_DATA_URI}\');background-size:cover;background-position:center;mix-blend-mode:multiply;opacity:.92;"></div>'
    f'<div style="position:fixed;inset:0;width:100%;height:100%;z-index:-1;background:linear-gradient(180deg,rgba(6,8,26,.35) 0%,rgba(6,8,26,.6) 100%);"></div>',
    unsafe_allow_html=True)

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html,body,[class*="css"]{{font-family:'Inter',sans-serif;}}
#MainMenu{{visibility:hidden;}}footer{{visibility:hidden;}}
header[data-testid="stHeader"]{{display:none;}}
section[data-testid="stSidebar"]{{display:none!important;}}
.block-container{{padding-top:2.2vh!important;padding-bottom:1vh!important;max-width:1080px;}}
[data-testid="stAppViewContainer"], .stApp{{background:transparent!important;}}

.hub-logo-wrap{{display:flex;justify-content:center;margin-bottom:10px;}}
.hub-logo-wrap img{{height:38px;filter:drop-shadow(0 4px 18px rgba(20,40,255,.35));}}
.hub-title{{text-align:center;color:white;font-size:26px;font-weight:800;
  letter-spacing:.4px;margin-bottom:3px;}}
.hub-sub{{text-align:center;color:rgba(255,255,255,.55);font-size:12.5px;
  margin-bottom:22px;}}

.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;}}
.card{{display:block;text-decoration:none!important;}}
.card-inner{{background:rgba(40,60,190,.22);backdrop-filter:blur(14px);
  -webkit-backdrop-filter:blur(14px);border:1px solid rgba(90,120,255,.30);
  border-radius:14px;padding:16px;box-sizing:border-box;
  aspect-ratio:1/1;display:flex;flex-direction:column;align-items:center;
  justify-content:center;text-align:center;gap:6px;
  transition:transform .16s ease, filter .16s ease, border-color .16s ease;}}
.card:hover .card-inner{{transform:translateY(-4px);filter:brightness(1.18);
  border-color:rgba(140,165,255,.6);}}
.card-inner.destaque{{border-color:rgba(140,165,255,.5);}}
.card.disabled .card-inner{{opacity:.62;}}
.card-icon{{font-size:26px;}}
.card-name{{color:white;font-size:13.5px;font-weight:700;line-height:1.25;}}
.card-sub{{color:rgba(255,255,255,.6);font-size:10px;line-height:1.35;}}
.card-badge{{font-size:8.5px;font-weight:600;text-transform:uppercase;
  letter-spacing:.5px;padding:2px 8px;border-radius:8px;margin-top:2px;}}
.card-badge.live{{background:rgba(46,204,113,.22);color:#4ADE80;}}
.card-badge.soon{{background:rgba(255,255,255,.14);color:rgba(255,255,255,.65);}}

.mini-btns{{display:flex;gap:6px;margin-top:2px;width:100%;}}
.mini-btn{{flex:1;text-align:center;font-size:9.5px;font-weight:600;
  padding:6px 4px;border-radius:7px;text-decoration:none!important;
  background:rgba(90,120,255,.22);color:rgba(255,255,255,.92);
  transition:background .15s;}}
.mini-btn:hover{{background:rgba(90,120,255,.40);}}
.mini-btn.disabled{{opacity:.6;cursor:default;}}

.hub-foot{{text-align:center;color:rgba(255,255,255,.28);font-size:9.5px;
  margin-top:22px;letter-spacing:.3px;}}

@media (max-width: 900px) {{ .grid{{grid-template-columns:repeat(2,1fr);}} }}
</style>
""", unsafe_allow_html=True)

# =====================================================================
def _card_html(item):
    """Monta o HTML do card tudo em uma linha só — quebrar em várias
    linhas indentadas faz o Markdown do Streamlit tratar como bloco de
    código em vez de HTML. O <a>/<div> externo sempre tem 1 filho só
    (.card-inner), pra não repetir o bug do card com vários blocos soltos
    dentro de uma tag <a>."""
    url = item.get("url")
    tem_botoes = "botoes" in item
    destaque = " destaque" if item.get("destaque") else ""

    if tem_botoes:
        partes = []
        for nome_b, url_b in item["botoes"]:
            if url_b:
                partes.append(f'<a class="mini-btn" href="{url_b}" target="_blank" rel="noopener noreferrer">{nome_b}</a>')
            else:
                partes.append(f'<span class="mini-btn disabled">{nome_b}</span>')
        extra = f'<div class="mini-btns">{"".join(partes)}</div>'
        tag, href, classe = "div", "", "card"
    else:
        tag = "a" if url else "div"
        href = f'href="{url}" target="_blank" rel="noopener noreferrer"' if url else ""
        classe = "card" if url else "card disabled"
        extra = ('<span class="card-badge live">Disponível</span>' if url
                 else '<span class="card-badge soon">Em breve</span>')

    return (f'<{tag} class="{classe}" {href}>'
            f'<div class="card-inner{destaque}">'
            f'<div class="card-icon">{item["icone"]}</div>'
            f'<div class="card-name">{item["nome"]}</div>'
            f'<div class="card-sub">{item["sub"]}</div>'
            f'{extra}'
            f'</div>'
            f'</{tag}>')

st.markdown(
    f'<div class="hub-logo-wrap"><img src="{LOGO_LIGHT_DATA_URI}"></div>'
    f'<div class="hub-title">Delga HUB</div>'
    f'<div class="hub-sub">Central de soluções do Grupo Delga</div>',
    unsafe_allow_html=True)

cards_html = "".join(_card_html(item) for item in TODOS)
st.markdown(f'<div class="grid">{cards_html}</div>', unsafe_allow_html=True)

st.markdown('<div class="hub-foot">Grupo Delga Ind. e Com. · Desenvolvido por Gabriel Souza · Lato Sensu em Gestão de Projetos</div>',
            unsafe_allow_html=True)
