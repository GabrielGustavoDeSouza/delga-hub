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
# =====================================================================
PROJETOS = {
    "nome": "Delga Projects", "sub": "Redução de Custos & Performance Operacional",
    "icone": "📊",
    "url": "https://plataformadegest-odeprojetosdelga-2miazhybxebzwmz7nyvcgx.streamlit.app/",
}

OUTROS = [
    {"nome": "Delga Mobile", "sub": "App do Grupo Delga", "icone": "📱",
     "url": None},
    {"nome": "Delga OEE", "sub": "Eficiência de Equipamentos", "icone": "⚙️",
     "botoes": [("Delga Sync", None), ("Delga Ega", None)]},
    {"nome": "Delga SGI", "sub": "Sistema de Gestão Integrada", "icone": "📁",
     "url": None},
    {"nome": "Delga Helps", "sub": "Chamados de Manutenção & TI", "icone": "🛠️",
     "botoes": [("Tractian", None), ("GLPI", None)]},
    {"nome": "Delga Academy", "sub": "Cursos Gupy & Treinamentos", "icone": "🎓",
     "url": None},
    {"nome": "Delga Logística", "sub": "Iniciativas de Processos Logísticos", "icone": "🚚",
     "url": None},
    {"nome": "Delga Sell", "sub": "Cotações & Vendas", "icone": "💰",
     "url": None},
]

# =====================================================================
st.markdown(f"""
<video autoplay muted loop playsinline
  style="position:fixed;inset:0;width:100%;height:100%;object-fit:cover;z-index:-3;">
  <source src="{BG_VIDEO_DATA_URI}" type="video/mp4">
</video>
<div style="position:fixed;inset:0;width:100%;height:100%;z-index:-2;
     background-image:url('{BG_OVERLAY_DATA_URI}');background-size:cover;
     background-position:center;mix-blend-mode:multiply;opacity:.92;"></div>
<div style="position:fixed;inset:0;width:100%;height:100%;z-index:-1;
     background:linear-gradient(180deg,rgba(6,8,26,.35) 0%,rgba(6,8,26,.6) 100%);"></div>
""", unsafe_allow_html=True)

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html,body,[class*="css"]{{font-family:'Inter',sans-serif;}}
#MainMenu{{visibility:hidden;}}footer{{visibility:hidden;}}
header[data-testid="stHeader"]{{display:none;}}
section[data-testid="stSidebar"]{{display:none!important;}}
.block-container{{padding-top:4vh!important;max-width:1200px;}}
[data-testid="stAppViewContainer"], .stApp{{background:transparent!important;}}

.hub-logo-wrap{{display:flex;justify-content:center;margin-bottom:18px;}}
.hub-logo-wrap img{{height:48px;filter:drop-shadow(0 4px 18px rgba(20,40,255,.35));}}
.hub-title{{text-align:center;color:white;font-size:34px;font-weight:800;
  letter-spacing:.5px;margin-bottom:6px;}}
.hub-sub{{text-align:center;color:rgba(255,255,255,.55);font-size:14px;
  margin-bottom:40px;}}

.hero-card{{background:linear-gradient(120deg,{BLUE} 0%,{BLUE2} 100%);
  border-radius:20px;padding:30px 40px;margin-bottom:36px;
  box-shadow:0 20px 60px rgba(20,40,255,.35),0 2px 0 rgba(255,255,255,.08) inset;
  display:flex;align-items:center;gap:24px;text-decoration:none!important;
  transition:transform .15s, box-shadow .15s;}}
.hero-card:hover{{transform:translateY(-3px);
  box-shadow:0 26px 70px rgba(20,40,255,.45),0 2px 0 rgba(255,255,255,.08) inset;}}
.hero-icon{{font-size:44px;flex-shrink:0;
  background:rgba(255,255,255,.12);border-radius:16px;padding:16px 20px;}}
.hero-name{{color:white;font-size:24px;font-weight:800;margin:0;}}
.hero-sub{{color:rgba(255,255,255,.75);font-size:13px;margin-top:4px;}}
.hero-arrow{{margin-left:auto;color:white;font-size:26px;opacity:.7;flex-shrink:0;}}

.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;}}
.card{{background:rgba(255,255,255,.06);backdrop-filter:blur(16px);
  -webkit-backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.10);
  border-radius:16px;padding:22px 20px;text-decoration:none!important;
  display:flex;flex-direction:column;gap:10px;min-height:150px;
  transition:transform .15s, border-color .15s, background .15s;}}
.card:hover{{transform:translateY(-3px);border-color:rgba(255,255,255,.28);
  background:rgba(255,255,255,.10);}}
.card.disabled{{opacity:.5;cursor:default;}}
.card.disabled:hover{{transform:none;border-color:rgba(255,255,255,.10);
  background:rgba(255,255,255,.06);}}
.card-icon{{font-size:26px;}}
.card-name{{color:white;font-size:15px;font-weight:700;margin:0;}}
.card-sub{{color:rgba(255,255,255,.5);font-size:11px;line-height:1.4;flex:1;}}
.card-badge{{align-self:flex-start;font-size:9px;font-weight:600;
  text-transform:uppercase;letter-spacing:.5px;padding:3px 9px;border-radius:10px;}}
.card-badge.live{{background:rgba(46,204,113,.18);color:#4ADE80;}}
.card-badge.soon{{background:rgba(255,255,255,.10);color:rgba(255,255,255,.55);}}

.mini-btns{{display:flex;gap:8px;margin-top:auto;}}
.mini-btn{{flex:1;text-align:center;font-size:11px;font-weight:600;
  padding:7px 6px;border-radius:8px;text-decoration:none!important;
  background:rgba(255,255,255,.10);color:rgba(255,255,255,.85);
  transition:background .15s;}}
.mini-btn:hover{{background:rgba(255,255,255,.20);}}
.mini-btn.disabled{{opacity:.45;cursor:default;}}
.mini-btn.disabled:hover{{background:rgba(255,255,255,.10);}}

.hub-foot{{text-align:center;color:rgba(255,255,255,.28);font-size:10px;
  margin-top:48px;letter-spacing:.3px;}}

@media (max-width: 900px) {{ .grid{{grid-template-columns:repeat(2,1fr);}} }}
</style>
""", unsafe_allow_html=True)

# =====================================================================
def _card_html(item):
    url = item.get("url")
    tag = "a" if url else "div"
    href = f'href="{url}" target="_blank" rel="noopener noreferrer"' if url else ""
    classe = "card" if url else "card disabled"
    badge = ('<span class="card-badge live">Disponível</span>' if url
             else '<span class="card-badge soon">Em breve</span>')

    botoes_html = ""
    if "botoes" in item:
        partes = []
        for nome_b, url_b in item["botoes"]:
            if url_b:
                partes.append(f'<a class="mini-btn" href="{url_b}" target="_blank" '
                              f'rel="noopener noreferrer">{nome_b}</a>')
            else:
                partes.append(f'<span class="mini-btn disabled">{nome_b}</span>')
        botoes_html = f'<div class="mini-btns">{"".join(partes)}</div>'
        badge = ""  # o card em si não é clicável quando tem 2 botões — o clique é neles

    if "botoes" in item:
        tag, href, classe = "div", "", "card"

    return f"""<{tag} class="{classe}" {href}>
      <div class="card-icon">{item['icone']}</div>
      <div class="card-name">{item['nome']}</div>
      <div class="card-sub">{item['sub']}</div>
      {botoes_html}
      {badge}
    </{tag}>"""

st.markdown(f"""
<div class="hub-logo-wrap"><img src="{LOGO_LIGHT_DATA_URI}"></div>
<div class="hub-title">Delga HUB</div>
<div class="hub-sub">Central de soluções do Grupo Delga</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<a class="hero-card" href="{PROJETOS['url']}" target="_blank" rel="noopener noreferrer">
  <div class="hero-icon">{PROJETOS['icone']}</div>
  <div>
    <p class="hero-name">{PROJETOS['nome']}</p>
    <p class="hero-sub">{PROJETOS['sub']}</p>
  </div>
  <div class="hero-arrow">→</div>
</a>
""", unsafe_allow_html=True)

cards_html = "".join(_card_html(item) for item in OUTROS)
st.markdown(f'<div class="grid">{cards_html}</div>', unsafe_allow_html=True)

st.markdown('<div class="hub-foot">Grupo Delga Ind. e Com. · Desenvolvido por Gabriel Souza</div>',
            unsafe_allow_html=True)
