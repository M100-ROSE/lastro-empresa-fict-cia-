# Briefing — LASTRO

**Plataforma B2B de tesouraria e conciliação financeira**
Versão 1.0 · Responsável: Day · 26/10/2026 · Status: pronto para design

---

## 1. Visão geral

| Item | Definição |
|---|---|
| **Nicho** | Fintech B2B — tesouraria, conciliação bancária e fechamento contábil para empresas de R$ 20 mi a R$ 500 mi de faturamento |
| **Público** | CFOs, controllers e analistas financeiros de 30 a 50 anos. Rotina técnica, alta exigência de precisão, pouco tempo e ceticismo com promessas de marketing. |
| **Objetivo do site** | Gerar demos qualificadas com empresas de médio porte e transmitir segurança técnica (integrações, auditoria, compliance). |
| **Local fictício** | Empresa brasileira, sede em São Paulo/SP; operação remota. |
| **Tom de voz** | Sóbrio, específico e verificável. Frase curta + número com fonte. Nenhum superlativo. Fala de risco, prazo e controle. |

**Promessa central:** todo real conciliado, todos os dias, com rastro de auditoria.

**Conversões principais**
1. Agendar demo de 30 minutos (primária).
2. Ver integrações e segurança.
3. Baixar o guia de fechamento.

---

## 2. Sentimento alvo

**Sentimento alvo: confiança, precisão e controle.**

**Declaração:** o visitante deve sentir que está olhando para uma ferramenta usada por gente tão exigente quanto ele — e que cada número exibido pode ser conferido.

Como o design produz isso:

- **Densidade informacional controlada:** o site usa a linguagem do produto (tabelas, KPIs, status, logs) em vez de ilustrações de marketing.
- **Paleta fria e sóbria:** navy, branco, cinza-azulado e teal. Âmbar apenas para atenção; verde apenas para sucesso. Nenhuma cor decorativa.
- **Tipografia técnica:** IBM Plex Sans para interface e IBM Plex Mono para números, códigos de transação, IDs e labels de sistema.
- **Grid modular de 8 px:** tudo alinhado, nada flutuando. Raios de 8 px, bordas de 1 px, sombras quase invisíveis.
- **Prova numérica:** KPIs com data de referência, fontes e metodologia. Nada de "milhares de clientes" sem número.
- **Motion discreto:** 150–200 ms, sem parallax, sem contadores chamativos. Gráficos desenham uma vez.
- **Hierarquia de console:** navegação lateral fixa, barra superior com status do sistema e atalho para demo.

---

## 3. Identidade verbal

**Nome:** LASTRO
**Justificativa:** lastro é o que dá garantia e estabilidade a uma operação financeira — o respaldo que sustenta o valor. É uma palavra do vocabulário do CFO, curta, concreta e não genérica como "Finance".

**Tagline:** *Todo real conciliado. Todo dia.*

**Headlines de exemplo**
1. "Feche o mês em 2 dias, não em 2 semanas."
2. "98,4% das transações conciliadas sem toque humano."
3. "Se não está no lastro, não está no relatório."
4. "Feito para quem assina o balanço."
5. "Menos planilha. Menos surpresa no fechamento."

**Microcopy de apoio**
- CTA principal: "Agendar demo"
- CTA secundário: "Ver integrações"
- Formulário: "Quantas contas bancárias a operação movimenta?"
- Confirmação: "Recebido. Nosso time comercial responde em até 1 dia útil com uma agenda."
- Rodapé: "Dados de performance ilustrativos, base 2026. Metodologia disponível sob solicitação."

**Vocabulário preferido:** conciliação, fechamento, lastro, alçada, trilha de auditoria, divergência, extrato, baixa, competência, controle.
**Vocabulário proibido:** revolucionar, disruptivo, mágico, simples assim, "ame", "incrível", emojis, "o futuro do dinheiro".

---

## 4. Paleta de cores

| Papel | Nome | HEX | Uso |
|---|---|---|---|
| Primária | Teal operacional | `#0E7C86` | CTAs, links primários, séries de gráfico, estados ativos |
| Secundária | Azul confiança | `#1D4ED8` | Links informativos, foco, seleção, dados de referência |
| Acento | Âmbar de atenção | `#B45309` | Divergências, alertas, prazos, status "atenção" |
| Suporte | Verde conciliado | `#157347` | Status "ok", valores conciliados, sucesso |
| Fundo | Cinza-papel | `#F7F9FB` | Fundo global |
| Superfície | Branco | `#FFFFFF` | Cards, tabelas, header, sidebar |
| Texto | Navy | `#0B1F33` | Títulos, corpo, números |
| Texto suave | Cinza-azulado | `#5A6B7B` | Labels, metadados, texto auxiliar |
| Borda | Cinza claro | `#D7DEE6` | Bordas de 1 px, divisores de tabela |

**Regras de contraste (WCAG 2.2)**

| Combinação | Razão | Nível |
|---|---|---|
| `#0B1F33` sobre `#F7F9FB` | 15,8:1 | AAA |
| `#0B1F33` sobre `#FFFFFF` | 16,7:1 | AAA |
| `#FFFFFF` sobre `#0E7C86` | 5,0:1 | AA |
| `#0E7C86` sobre `#FFFFFF` | 5,0:1 | AA |
| `#1D4ED8` sobre `#FFFFFF` | 6,7:1 | AA |
| `#B45309` sobre `#FFFFFF` | 5,0:1 | AA |
| `#157347` sobre `#FFFFFF` | 5,9:1 | AA |
| `#5A6B7B` sobre `#F7F9FB` | 5,2:1 | AA |

**Restrições:** teal sobre `#F7F9FB` tem 4,7:1 — usar em textos a partir de 16 px, com margem de segurança; âmbar nunca é fundo de botão primário; nenhum gradiente; nenhuma cor fora da paleta, exceto em gráficos com legenda explícita.

---

## 5. Tipografia

| Papel | Fonte | Peso | Uso |
|---|---|---|---|
| Títulos / interface | **IBM Plex Sans** (Google Fonts) | 400, 500, 600 | H1–H4, navegação, botões, corpo, tabelas |
| Dados / código | **IBM Plex Mono** (Google Fonts) | 400, 500 | Números, IDs, valores monetários, labels de sistema, snippets |

**Escala desktop (base 16 px)**

| Token | px | rem | Entrelinha | Letter-spacing |
|---|---:|---:|---:|---:|
| Display | 48 | 3.0 | 52 px (1.08) | −0,02em |
| H1 | 36 | 2.25 | 44 px (1.22) | −0,015em |
| H2 | 30 | 1.875 | 38 px (1.27) | −0,01em |
| H3 | 24 | 1.5 | 32 px (1.33) | 0 |
| Lead | 20 | 1.25 | 30 px (1.5) | 0 |
| Corpo | 16 | 1.0 | 26 px (1.63) | 0 |
| Corpo pequeno | 14 | 0.875 | 22 px (1.57) | 0 |
| Label de UI | 13 | 0.8125 | 18 px (1.38) | 0,02em |
| Micro / tabela | 12 | 0.75 | 18 px (1.5) | 0,02em |
| Dado monetário | 14 | 0.875 | 20 px (1.43) | 0,01em, tabular |

**Escala mobile (≤ 767 px):** Display 36/40; H1 30/36; H2 26/32; H3 21/28; Lead 18/28; Corpo 16/26; Pequeno 14/22; Label 12/17.

**Regras:** IBM Plex Mono só em números, IDs, valores e labels de sistema; nunca em parágrafos. Todos os números usam `font-variant-numeric: tabular-nums`. Títulos com peso 600; corpo 400; labels 500 em caixa alta quando forem de sistema. Nada de itálico. Sem caixa alta em títulos longos.

---

## 6. Layout e componentes

### Direção de layout — **dashboard denso com shell de produto**

O site inteiro adota a linguagem de um console, não de uma landing page:

- **Sidebar fixa de 248 px** à esquerda, com logotipo, anchors de seção (Visão geral, Produto, Integrações, Segurança, Clientes, Preços) e bloco de status no rodapé.
- **Topbar de 64 px** com breadcrumb, seletor "PT-BR", link "Entrar" e CTA "Agendar demo"; à direita, indicador verde "Todos os sistemas operacionais" com link para status.
- **Área de conteúdo** com largura máxima **1200 px** dentro do shell, grid de **12 colunas**, gutter **16 px**, padding **32 px**. Base de espaçamento **8 px** (8/16/24/32/48/64/96).
- **Hero em split 5/7:** texto à esquerda (5 col) e um painel de produto à direita (7 col) com 3 KPIs, um gráfico de conciliação e uma tabela de 4 linhas. O painel tem moldura de 1 px, raio 8 px, sem sombra pesada.
- **Seções como "módulos"** com cabeçalho de 48 px, borda superior de 1 px e labels de sistema em mono.
- **Tabelas reais** na home (não screenshots): 5 linhas de transações com status, banco, valor e ação.
- Cards com raio **8 px**, borda 1 px `#D7DEE6`, sombra `0 1px 2px rgba(11,31,51,0.06)`.
- Sem full-bleed, sem diagonais, sem imagens decorativas. Uma única foto (equipe) na página "Sobre", em proporção 16:9, sem tratamento artístico.
- **Densidade:** 3 níveis de espaçamento (compacto 8 px, padrão 16 px, seção 96 px); tabelas com linha de 48 px e opção de densidade confortável (56 px).

### Breakpoints

| Nome | Largura | Grid | Comportamento |
|---|---:|---|---|
| XS | 360–479 | 4 col, gutter 12 | Sidebar vira drawer; hero empilhado; tabela com scroll horizontal |
| SM | 480–767 | 4 col, gutter 12 | KPIs em 2 col; tabela com colunas essenciais |
| MD | 768–1023 | 8 col, gutter 16 | Sidebar colapsada em ícones (72 px); hero 6/6 |
| LG | 1024–1279 | 12 col, gutter 16 | Sidebar 248 px; split 5/7 |
| XL | 1280–1439 | 12 col, gutter 16 | Conteúdo 1200 px |
| 2XL | ≥ 1440 | 12 col | Margens crescem; shell fixo |

### Componentes e estados

**Botão primário (teal)**
- Default: fundo `#0E7C86`, texto branco, altura 40 px (48 px em formulários), padding 20 px, raio 8 px, IBM Plex Sans 500 14 px.
- Hover: fundo `#0A646C`, transição 150 ms.
- Focus: anel `#1D4ED8` de 2 px com offset 2 px + anel branco de 2 px.
- Active: fundo `#085158`.
- Disabled: fundo `#E3E9EF`, texto `#8796A5`, sem borda.
- Loading: spinner de 16 px + texto "Agendando…", largura travada, `aria-busy="true"`.

**Botão secundário:** fundo branco, borda 1 px `#C9D3DD`, texto navy; hover fundo `#F0F4F8`.

**Botão terciário (link):** texto teal, sem fundo; hover sublinhado; foco anel azul.

**Campo de formulário:** altura 40 px, raio 6 px, borda 1 px `#C9D3DD`, fundo branco, label 13 px/500 acima; foco borda azul 2 px + anel azul 3 px com 20% de opacidade; erro borda âmbar + mensagem 13 px; sucesso borda verde; helper text 12 px.

**Card de KPI:** borda 1 px, raio 8 px, padding 20 px; label 12 px em mono caixa alta; valor 30 px em Plex Sans 600 com tabular-nums; variação com seta e cor + texto ("+12,4% vs. mês anterior"); rodapé com fonte e data.

**Tabela de transações:** header sticky, fundo `#F7F9FB`, label 11 px mono caixa alta; linhas de 48 px, borda inferior 1 px; colunas: data, banco, descrição, valor (alinhado à direita), status, ação. Hover `#F0F4F8`; linha selecionada com barra teal de 2 px à esquerda; status com ícone + texto.

**Badge de status:** "CONCILIADO" (verde, fundo 8%), "DIVERGENTE" (âmbar, fundo 8%), "PENDENTE" (cinza). Sempre ícone + texto, nunca só cor.

**Gráfico de linha:** eixo Y em mono 11 px, grid horizontal de 1 px `#E8EDF2`, linha teal de 2 px, área com 8% de opacidade; tooltip com valor e data; legenda acima; tabela alternativa acessível abaixo (recolhível).

**Tabs:** altura 40 px, label 13 px/500, indicador teal de 2 px na base; foco visível; navegação por setas.

**Tooltip:** fundo navy, texto branco 12 px, raio 4 px, seta de 6 px; aparece no hover e no foco; fechável por Esc.

### Animações

- Transições de UI: 150 ms `ease-out`; hover de linha: 100 ms.
- Entrada de seção: fade de 200 ms + `translateY(8px)`, uma vez.
- Gráfico: linha desenha em 600 ms ao entrar na viewport; números não contam.
- Sem parallax, sem marquee, sem vídeo, sem cursor customizado.
- `prefers-reduced-motion`: gráfico aparece completo, fades removidos.

---

## 7. Estrutura de páginas e conteúdo

### Mapa do site

1. Home
2. Plataforma — Conciliação, Tesouraria, Fechamento
3. Integrações (bancos, ERPs, adquirentes)
4. Segurança e compliance
5. Clientes e casos
6. Preços
7. Recursos (guias e calculadora de fechamento)
8. Demo
9. Status e login (links externos ao app)

### Wireframe — Home

```
┌───────────┬──────────────────────────────────────────────────────────┐
│ LASTRO    │ Visão geral / PT-BR        [Entrar]  [AGENDAR DEMO]      │ 64px
│           ├──────────────────────────────────────────────────────────┤
│ Visão geral│ ● Todos os sistemas operacionais            status →    │
│ Produto    │                                                          │
│ Integrações│  Tesouraria sem planilha.          ┌ KPI ──────────────┐ │
│ Segurança  │  Fechamento sem surpresa.          │ 98,4% conciliado  │ │
│ Clientes   │                                    │ 2,1 dias fecham.  │ │
│ Preços     │  Concilie 12 bancos, Pix e         │ R$ 4,2 bi lastro. │ │
│ Recursos   │  cartões em um só lugar, com       └───────────────────┘ │
│            │  trilha de auditoria.              ┌ gráfico linha ────┐ │
│            │  [AGENDAR DEMO] [VER INTEGRAÇÕES]  │ 30 dias           │ │
│            │                                    └───────────────────┘ │
│            │                                    ┌ tabela 4 linhas ─┐ │
│            │                                    │ Itaú · Pix · ok   │ │
│            │                                    └───────────────────┘ │
│            ├──────────────────────────────────────────────────────────┤
│            │  MÓDULO 01 — CONCILIAÇÃO                                │
│            │  texto 5 col + checklist 5 col + link                   │
│            ├──────────────────────────────────────────────────────────┤
│            │  MÓDULO 02 — TESOURARIA (fundo cinza, 3 cards)          │
│            ├──────────────────────────────────────────────────────────┤
│            │  MÓDULO 03 — FECHAMENTO (tabela + prazos)                │
│            ├──────────────────────────────────────────────────────────┤
│            │  INTEGRAÇÕES — grade de logos em escala de cinza + texto │
│            ├──────────────────────────────────────────────────────────┤
│            │  SEGURANÇA — 4 itens: SOC 2, ISO 27001, LGPD, auditoria  │
│            ├──────────────────────────────────────────────────────────┤
│            │  PROVA — caso de cliente com 3 números e citação curta    │
│            ├──────────────────────────────────────────────────────────┤
│            │  PREÇOS — 3 planos em tabela comparativa                 │
│            ├──────────────────────────────────────────────────────────┤
│            │  CTA — fundo navy: "Veja seu fechamento em 30 minutos."  │
│            ├──────────────────────────────────────────────────────────┤
│            │  Rodapé denso: colunas de produto, empresa, legal, status │
└───────────┴──────────────────────────────────────────────────────────┘
```

### Conteúdo por página

**Home**
- Hero: H1 "Tesouraria sem planilha. Fechamento sem surpresa.", lead de 2 linhas, dois CTAs, microcopy "Demo de 30 min · sem instalação".
- Painel de produto: 3 KPIs (98,4% de conciliação automática; 2,1 dias úteis para fechar o mês; R$ 4,2 bi conciliados em 2025), gráfico de 30 dias e tabela de 4 transações com status.
- Módulos: Conciliação (bancos, Pix, cartões, adquirentes), Tesouraria (saldo consolidado, previsão de caixa, alçadas), Fechamento (competência, provisões, trilha de auditoria).
- Integrações: 40+ bancos, TOTVS, SAP Business One, Omie, Conta Azul, adquirentes; busca por nome; aviso "não encontrou? fale com a gente".
- Segurança: SOC 2 Tipo II, ISO 27001, LGPD, criptografia AES-256, logs imutáveis, SSO/SAML, disponibilidade 99,95% com histórico.
- Caso: "Grupo Meridiano — 14 empresas, 38 contas, fechamento de 11 para 3 dias" com citação do controller.
- Preços: Essencial (até 5 contas) R$ 1.490/mês; Performance (até 25 contas) R$ 3.900/mês; Enterprise sob consulta. Todos com implementação assistida.
- CTA final: "Veja seu fechamento em 30 minutos" + formulário curto.

**Plataforma:** uma página por módulo, com fluxo em 4 etapas, regras de negócio, exemplos de divergência, limites e API. Cada página tem uma tabela de "o que entra / o que sai" e um bloco de perguntas técnicas.

**Integrações:** catálogo filtrável por categoria (banco, ERP, adquirente, planilha), status de homologação, tempo médio de implantação, documentação de API (link externo). Nenhum logo colorido: todos em navy com opacidade 70%.

**Segurança:** certificações com ano, escopo, auditor, link para relatório sob NDA; arquitetura em diagrama de blocos (não ilustração 3D); política de incidentes; subprocessadores; plano de continuidade.

**Clientes:** 3 casos com números antes/depois, porte da empresa, ERP, quantidade de contas e citação com nome e cargo. Sem logos de clientes sem autorização.

**Preços:** tabela comparativa com 18 linhas, agrupadas por categoria; taxas de implementação explícitas; FAQ sobre contrato, cancelamento e reajuste; CTA de demo em cada plano.

**Demo:** formulário de 6 campos (nome, e-mail corporativo, empresa, cargo, número de contas, ERP), qualificação por faixa; promessa de resposta em 1 dia útil; alternativa de contato comercial; política de privacidade linkada.

**Recursos:** guia "Fechamento em 5 dias", calculadora de custo de planilha, checklist de conciliação, webinars com data e transcrição.

---

## 8. Acessibilidade e performance

**Acessibilidade**
- Contraste AA em todo texto e UI; AAA para corpo no marketing.
- Foco visível em todos os controles: anel azul de 2 px + offset 2 px + anel branco.
- Alvos de toque ≥ 32×32 px (WCAG 2.2), com 44 px recomendado em mobile.
- Tabelas com `<caption>`, `<th scope>`, ordenação anunciada por `aria-sort` e navegação por teclado.
- Gráficos com resumo textual, tabela alternativa e legenda; nunca dependem só de cor.
- Status sempre com ícone + texto; contraste mínimo de 3:1 para elementos gráficos.
- Formulários com label visível, `autocomplete`, erros vinculados e resumo no topo; não usar placeholder como label.
- Sidebar com navegação por teclado, `aria-current="page"` e skip link.
- `prefers-reduced-motion` remove fades e desenho de gráfico.
- Nenhum conteúdo essencial em tooltip ou hover; tooltips fecham com Esc.
- Zoom de 200% sem perda de conteúdo; layout resiste a 320 px de largura.

**Performance (metas)**
- LCP < 1,8 s em 4G; CLS < 0,05; INP < 200 ms.
- Peso da home < 1,3 MB; JS < 180 KB gzip; sem biblioteca de gráficos acima da dobra (SVG estático no hero, interativo sob demanda).
- Fontes WOFF2 com subset latino; preload de IBM Plex Sans 400/600 e Plex Mono 400.
- Imagens AVIF/WebP; nenhuma imagem decorativa pesada; logos em SVG.
- Tabelas renderizadas no servidor; sem layout shift ao carregar dados.
- Lighthouse ≥ 95 em Performance, Acessibilidade e SEO no mobile.

---

## 9. O que NÃO fazer

**Anti-padrões visuais proibidos**
- Gradiente roxo/azul de SaaS, glow, glassmorphism, ilustrações 3D flutuantes.
- Hero escuro com partículas, "data mesh" abstrato, linhas conectadas sem significado.
- Fotos de banco de imagem com aperto de mão, arranha-céus, terno e relógio.
- Tipografia display gigante, condensada ou serifada; texto em caixa alta em parágrafos.
- Cards com raio 24 px, sombras difusas, cores pastel, emojis.
- Números sem fonte, data ou metodologia; "milhares de empresas" sem quantidade.
- Copy com "revolucione", "disruptivo", "o futuro do dinheiro", "simples assim".
- Carrossel automático de depoimentos, contadores animados, urgência falsa.
- Tabela de preços escondida atrás de "fale com vendas" em todos os planos.
- Formulário de demo com mais de 8 campos ou pedido de dados financeiros sensíveis.
- Dark mode como padrão; a plataforma é clara para leitura prolongada.

---

## 10. Diferenciação vs os outros briefings

**Como esse site é diferente dos outros 4**

| Eixo | LASTRO (este) | CASULO | BRASA | TORNO | GIRA |
|---|---|---|---|---|---|
| Base cromática | Branco + navy + teal | Creme + sálvia + terracota | Preto + volt + vermelho | Marfim + espresso + ouro | Azul-céu + coral/amarelo/lilás |
| Tipografia | Sans técnica + mono | Serif humanista + sans calorosa | Condensada industrial | Serif editorial + sans geométrica | Rounded + sans arredondada |
| Forma | Grid modular, 8 px, sidebar | Curvas orgânicas, arcos | Diagonais, 0 raio | Hairlines, 0 raio | Blobs, cartões 28 px |
| Densidade | Alta, dados e tabelas | Baixa, respiro | Média-alta, tipo gigante | Muito baixa, vazio | Média, colagem |
| Ritmo de motion | Discreto (150–200 ms) | Lento (600–700 ms) | Rápido (120–180 ms) | Muito lento (800–1200 ms) | Saltitante (280–420 ms) |
| Emoção | Controle | Acolhimento | Urgência | Exclusividade | Diversão |

- **vs CASULO:** LASTRO não tem fotografia emocional, curvas ou serifa; CASULO não tem tabela, KPI, sidebar ou gráfico.
- **vs BRASA:** os dois são densos, mas BRASA é tipográfica e escura, com diagonais e urgência. LASTRO é claro, modular, frio e sem urgência.
- **vs TORNO:** LASTRO não tem vazio editorial, ouro ou hairlines decorativas; TORNO não tem dashboard nem densidade informacional.
- **vs GIRA:** LASTRO não tem cor saturada, ilustração, adesivo ou tipografia rounded; GIRA não tem tabela, status ou sidebar.

**Teste de diferenciação:** sem logo e sem texto, LASTRO é reconhecível pelo shell de console com sidebar, pela paleta navy/teal e por tabelas reais com status. É o único briefing com densidade alta e o único com tipografia monoespaçada.
