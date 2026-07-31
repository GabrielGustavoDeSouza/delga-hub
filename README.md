# Delga HUB

Central de links das soluções digitais do Grupo Delga — uma tela inicial única
que direciona pra cada plataforma (Projects, Mobile, OEE, SGI, Helps, Academy,
Logística, Sell).

## Como adicionar/atualizar um link

Abra `app.py` e edite o dicionário `PROJETOS` (o card em destaque) ou a lista
`OUTROS` (os demais cards). Basta preencher o campo `"url"` — o card sai
automaticamente do estado "Em breve" e vira um link clicável.

Cards com dois botões (Delga OEE e Delga Helps) usam `"botoes": [(nome, url), ...]`
em vez de `"url"` — cada botão é preenchido e liberado independente do outro.

## Rodar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy

Suba este repositório separado no Streamlit Community Cloud (streamlit.io/cloud),
apontando pra `app.py` como arquivo principal — igual já é feito com a
Plataforma de Gestão de Projetos.

---
Desenvolvido por Gabriel Souza · Grupo Delga
