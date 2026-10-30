# Especificação Técnica do Site LASTRO em Svelte

## Resumo
Transformação do site atual em componentes Svelte reutilizáveis, seguindo o design system do briefing — paleta, tipografia, grid modular de 8px e estados completos para acessibilidade e responsividade.

---

## 1. Componentes Svelte Necessários

### Núcleo
- **topbar.svelte** – barra superior fixa (consola e branding)
- **sidebar.svelte** – navegação lateral fixa (estado móvel: drawer)
- **skip-link.svelte** – skip link acessível
- **brand.svelte** – markup de branding (marca + título) reutilizável

### Área de Conteúdo Principal
- **hero.svelte** – hero split 5/7 (texto + painel de produto com KPIs, gráfico e tabela)
- **panel.svelte** – painel principal com: header, KPIs, gráfico, conteúdo e footer
- **kpi-card.svelte** – cartão de KPI (label, valor, variação, rodapé)
- **chart-line.svelte** – gráfico SVG com tooltip e tabela alternativa acessível
- **transactions-table.svelte** – tabela de dados com status e ação

### Seções Modulares
- **section-head.svelte** – cabeçalho de seção reutilizável (eyebrow, título, meta)
- **module-card.svelte** – card de módulo (índice, título, descrição, ticks, rodapé)
- **feature-card.svelte** – card com título, parágrafo e lista de características (usado no produto)

### Status e Indicadores
- **badge.svelte** – badge de status (OK, DIVERGENTE, PENDENTE) com ícone
- **status-dot.svelte** – indicador de status do sistema (verde)
- **uptime-display.svelte** – número de disponibilidade + label

### UI de Formulário e Ações
- **button-primary.svelte** – estado completo (default, hover, focus, active, disabled, loading)
- **button-secondary.svelte** – secundário (white, borda cinza)
- **button-tertiary.svelte** – link simples (text + sublinhado em hover)
- **form-field.svelte** – campo de input (label, error, helper, sucesso)
- **textarea-field.svelte** – campo de área de texto (se aplicável)
- **demo-form.svelte** – formulário de qualificação (nome, empresa, cargo, contas, ERP)

### Conteúdo e Layout
- **section-card.svelte** – card genérico com borda superior (usado em módulos)
- **clients-list.svelte** – lista de logos (estado de tema cinza)
- **quote-block.svelte** – citação com attribution
- **security-list.svelte** – lista de verificação de segurança com ano e descrição
- **integration-chips.svelte** – lista compacta de tags (estilo de chip)
- **comparison-table.svelte** – tabela comparativa de preços (Planos Essencial, Performance, Enterprise)
- **pricing-card.svelte** – card de plano individual (recursos, preços, CTA)

### Navegação e UI Interna
- **topnav.svelte** – navegação secundária (visível apenas desktop)
- **breadcrumbs.svelte** – indicador de caminho (Console / Visão geral)
- **lang-switcher.svelte** – seletor de idioma (PT-BR, futuro)
- **table-of-contents.svelte** – links de âncora laterais (se aplicável)

### Rodapé e Metadados
- **footer.svelte** – rodapé completo (4 colunas + legal, com CTA de demo)
- **microcopy.svelte** – small-text reutilizável (ex: "Demo de 30 min · sem instalação")
- **text-meta.svelte** – texto meta (font mono, pequeno, cinza)

### Componentes Auxiliares
- **skeleton-loader.svelte** – placeholder para dados (se usarmos loading)
- **tooltip.svelte** – tooltip com flecha (hover + foco, fechável com Esc)
- **tabs.svelte** – componente de tabs (indicações teal, navegação por setas)
- **modal.svelte** – modal (se precisarmos de diálogo de integração com engenharia)
- **popover.svelte** – popover (para rich tooltips)

### Layout e Estrutura
- **content-shell.svelte** – container principal (grid 1200px, padding 32px, gutter 16px)
- **section-container.svelte** – wrapper genérico com espaçamento 96px
- **feature-grid.svelte** – grid de features (3 colunas, auto ajuste)
- **tiles-grid.svelte** – grid de logos em escala de cinza (grade adaptativa)

---

## 2. Mapeamento de Design System → Tokens

### Paleta (CSS custom properties)
```css
:root {
  /* Background */
  --bg: #F7F9FB;
  --surface: #FFFFFF;

  /* Texto */
  --ink: #0B1F33;          /* Título, corpo, números */
  --ink-soft: #5A6B7B;     /* Labels, metadados */
  --ink-mid: #33475B;

  /* Borda e Linha */
  --line: #D7DEE6;          /* Bordas card 1px */
  --line-soft: #E8EDF2;
  --line-strong: #C9D3DD;

  /* Ações */
  --teal: #0E7C86;          /* Primário, hover 0A646C, active 085158 */
  --blue: #1D4ED8;           /* Secundário, focus, links */
  --amber: #B45309;          /* Divergências, atenção */
  --green: #157347;          /* Sucesso, conciliado */

  /* Complementar */
  --navy: #0B1F33;
}
```

### Tipografia
```css
/* Fonte importada no layout Head */
--font-sans: "IBM Plex Sans", system-ui, sans-serif;
--font-mono: "IBM Plex Mono", ui-monospace, monospace;

/* Escala 16px base (desktop) */
--fs-display: 3rem;          /* 48px */
--fs-h1: 2.25rem;            /* 36px */
--fs-h2: 1.875rem;           /* 30px */
--fs-h3: 1.5rem;             /* 24px */
--fs-lead: 1.25rem;          /* 20px */
--fs-body: 1rem;             /* 16px */
--fs-body-small: 0.875rem;   /* 14px */
--fs-label: 0.8125rem;       /* 13px */
--fs-micro: 0.75rem;         /* 12px */
--fs-mono: 0.875rem;         /* 14px */

/* Altura de linha e espaçamento */
--lh-tight: 1.08;
--lh-base: 1.63;
--lh-relaxed: 1.5;

/* Peso */
--weight-normal: 400;
--weight-medium: 500;
--weight-semibold: 600;
```

### Grid e Layout
```css
/* Espaçamento base 8px */
--space-1: 8px;   --space-2: 16px;  --space-3: 24px;
--space-4: 32px;  --space-6: 48px;  --space-8: 64px;  --space-12: 96px;

/* Raios */
--radius: 8px; --radius-sm: 6px;

/* Sombras */
--shadow: 0 1px 2px rgba(11,31,51,0.06);

/* Breakpoints */
--xs: 360px; --sm: 480px; --md: 768px; --lg: 1024px; --xl: 1200px; --2xl: 1440px;
```

### Estado dos Componentes (parâmetros CSS)
```css
/* Button Primary */
--btn-primary-bg: var(--teal);
--btn-primary-hover: var(--teal-dark);
--btn-primary-active: var(--teal-deep);
--btn-primary-text: #fff;

/* Badge */
--badge-ok-bg: #EAF3EE;
--badge-ok-text: var(--green);
--badge-warn-bg: #FBF0E4;
--badge-warn-text: var(--amber);
--badge-pend-bg: #EEF2F6;
--badge-pend-text: #44586B;
```

---

## 3. Considerações de Acessibilidade (anotações por componente)

### SkipLink
- `href="#conteudo"`, foco visível com `top:8px`
- Ordem de tabulação preservada, `position: absolute`
- `prefers-reduced-motion: disable`

### Topbar/Sidebar
- `aria-current="page"` em links ativos
- `aria-label` para a finalidade da navegação (consola, seções)
- `role="navigation"`, `aria-labelledby` onde necessário
- Foco visível em links: anel azul 2px + offset 2px + anel branco
- Target de toque ≥ 44px (WCAG 2.2)

### Tabelas (TransactionsTable)
- `<caption>` oculto via `sr-only` (semelhante ao existente)
- `<th scope="col">` para semântica de dados
- `aria-sort` quando ordenação é adicionada
- Navegação por teclado em `table-scroll` com `tabindex="0"`
- Tabela alternativa para gráfico de linha (via <caption> + <thead>)
- `role="region"` + `aria-label` para tabela rolável

### Gráficos (ChartLine)
- `<svg>` com `role="img"` + `aria-labelledby` (id="chart-title", id="chart-desc")
- `<title>` e `<desc>` para acessibilidade
- Tabela alternativa acessível (display com `display: none` em desktop, `<table>` em mobile)
- Legenda com descrição completa: "Mínima de 96,9% em 12/10 · máxima de 99,1% em 21/10. Série ilustrativa, base 2026."

### Badges
- Status sempre com ícone + texto (com classe visual)
- Cor contrastante mínima de 3:1 para texto sobre fundo
- `aria-label` completo (ex: "Status: Conciliado ✓")
- Sem rely apenas em cor (adicionar ícone)

### Formulários
- Labels visíveis, sem usar `placeholder` como label
- `autocomplete` para campos (email, nome, empresa, etc.)
- Mensagem de erro vinculada via `aria-describedby`
- `aria-invalid="true"` para estado de erro
- Foco anel azul 2px + offset 2px + anel branco (mesmo padrão)

### Modal / Overlay (se adicionado)
- `role="dialog"`, `aria-modal="true"`, `aria-labelledby` para título
- `trap focus` dentro do diálogo
- Fechar com `Esc`, focar primeiro controle interno
- Overlay com `background-color: rgba(11,31,51,0.6)` sem blur

### Accordions / Toggle
- `role="button"` ou `<button>` com `aria-expanded`
- IDs consistentes entre toggle e conteúdo

### Navegação (Sidebar, Topnav)
- `aria-current="page"`
- `aria-label="Navegação da home"` para navegação principal

### Aviso de Movimento Reduzido
- `prefers-reduced-motion: disable` em:
  - Animações de entrada de seção
  - Desenho de gráfico de linha (stroke-dashoffset: 0)
  - `translateY(8px)` em `rise` keyframe

### Contraste de Texto
- Corpo (16px) sobre fundo: ≥ 16,7:1 (AAA)
- Texto de label (13px) sobre fundo: ≥ 5:1 (AA)
- Texto mono (12px) sobre fundo: ≥ 5:2 (AA)

### Roteiro (focus-visible)
```css
:where(a,[tabindex]):focus-visible {
  outline:2px solid var(--blue);
  outline-offset:2px;
  box-shadow:0 0 0 2px var(--surface);
}
```

---

## 4. Pendências de Conteúdo (divergências briefing vs site atual)

### Páginas Faltantes (baseado no briefing.md)
- **Página Plataforma** — por módulo (Conciliação, Tesouraria, Fechamento)
- **Página Integrações** — catálogo por categoria (banco, ERP, adquirente, planilha)
- **Página Segurança** — certificações + arquitetura de segurança (diagrama de blocos)
- **Página Clientes** — versão completa com citação de caso
- **Página Preços** — tabela comparativa com taxas de implementação e FAQ
- **Página Recursos** — guia de fechamento, calculadora de custo de planilha, checklist, webinar
- **Página Status** — status e login (links externos ao app)
- **Página Demo** — formulário de 6 campos, qualificação por faixa

### Conteúdo Faltante no Site (home atual)
- **Painel Produtos** — sem tabelas reais, sem grid de módulos 3 (Conciliação/Tesouraria/Fechamento)
- **Integrações** — sem logos, sem busca, sem aviso "não encontrou?"
- **Segurança** — sem certificações SOC 2 / ISO 27001 / LGPD com ano e escopo
- **Clientes** — sem caso de cliente com números antes/depois e citação com cargo
- **Preços** — sem tabela comparativa, sem CTA de demo por plano
- **CTA final** — sem campo de formulário curto e tagline centralizada

### Componentes Não Presentes (no briefing vs site)
- Slider de logos (integrações) — placeholder: `integration-tile`
- Modal para "Não encontrou? Fale com engenharia"
- FAQ (se adicionarmos preços)

### Espaçamento e Grid
- Sidebar em mobile: atualmente none, mas o briefing espera drawer (xs/sm). "sidebar" atual é `display:none` até `md:`.

---

## 5. Comentários de Implementação: Migração do CSS Atual para Svelte

### Tokens CSS (via <style> global)
- Usar `<style>` global no `+layout.svelte` para `--:*` variáveis.
- Manter ordem: normalize/reset → variables → estilos base → componentes.
- Importar fontes no layout: `<link>` para Google Fonts.

### Estilos Escopos (Componentes)
- Adicionar `<style lang="scss">` (ou CSS) com nome de classe local (ex: `.kpi-card`);
- Combinar com classes existentes (`.kpi`) para aproveitar a specificidade;
- Usar `css` vars para variação de tokens: `.kpi-card { --kpi-bg: var(--surface); }`
- Manter anotações BEM-like existentes como classes principais:
  ```svelte
  <style>
  .panel { background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow); }
  .panel__head { display: flex; ... }
  </style>
  <div class="panel">
    <div class="panel__head">
      …
    </div>
  </div>
  ```

### Propriedades CSS Personalizadas de Entrada de Componente
- Passar props CSS como `style` por contexto (ex: `--kpi-bg`, `--kpi-text`) para permitir overrides visuais.
- Usar `class:` prefixo do Svelte (`class="kpi {props.class}"`).

### Breakpoints: Reutilizar Media Queries existentes
- Manter media queries da `styles.css` original como CSS global nos componentes:
  ```svelte
  <style>
  .chart { ... }
  @media (min-width: 768px) {
    .chart { height: 84px; }
  }
  </style>
  ```

### Animações (Keyframe)
- Manter `@keyframes rise` e `@keyframes draw` em `<style>` global.
- Usar `.chart__line` e `.hero__copy` com animações existentes, adicionar classe `.reduced-motion` via `motion: false` no Svelte para `prefers-reduced-motion`.

### Pré-processador vs CSS Puro
- Sem necessidade de SCSS, mas usando módulos CSS para componentes de menor tamanho (`.svelte.css` com `?lang=css`).
- Manter estilização consistente com 8px, raio 8px, `box-sizing:border-box`.

### Réplicas de Utilidade (ex: skip-link)
- Encapsular no componente reutilizável, preservar `_focus-visible` e ordem de tabulação.

### Composição (Composition Patterns)
- Reutilizar as composições existentes:
  - `panel` = header + kpis + chart + footer
  - `section` = header + content
  - `hero` = copy + panel (split 5/7)

### Reactivos vs Estático
- Mantendo carregamento lento (lazy) com <svelte:component> vs `<Suspense>` se usarmos carregamento de dados.

---

## 6. Métricas e Qualidade Esperadas (em pronto para implementação)

- Responsivo: todos os breakpoints mantidos (xs/sm/md/lg/xl/2xl)
- Acessibilidade: contraste AA (AAA em marketing), roteiro, navegação por teclado
- Performance: atomic components, CSS-in-SJS mín., sem JS desnecessário
- Consistência: paleta, espaçamento, escalas tipográficas
- Manutenção: componentes modulares, componentes auxiliares reutilizáveis

---

## 7. Passos de Migração Sugeridos

1. **Layout base:** `+layout.svelte` com `<style>` global (tokens + reset base)
2. **Componentes de maior tamanho:** topbar, sidebar, skip-link, hero, panel
3. **Atoms:** button, badge, card, form-field, badge, chart-line
4. **Templates:** page shells (home, plataforma, integrações, etc.) — composições por página
5. **Testes:** alinhar as regras existentes para verificação visual
6. **CSS custom property hooks:** adicionar prop types (ex: `--bg: var(--prop-bg, var(--bg-default));`)

---

*Esta especificação está pronta para implementação pelo dev front-end. Nenhuma lógica de negócio ou escrita de componente foi criada.*