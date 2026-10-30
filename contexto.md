# Contexto — LASTRO

## Preferências
- Idioma: português do Brasil (pt-BR).
- Formato de commit: `tipo: descrição` (feat/fix/docs/refactor/chore/style/test).
- Não apagar site original (`site/`).
- Não incluir `node_modules` ou artefatos de build.
- Um commit por assunto; evitar misturar tarefas não relacionadas.
- Always inspect `git status`/`git diff` antes de commitar.

## Estado atual
- Projeto LASTRO: site estático original em `site/` (`index.html` + `styles.css`), briefing completo em `briefing.md`.
- Conversão para SvelteKit (`lastro-sveltekit/`) em andamento.
- Componentes implementados: `Hero.svelte`, `Panel.svelte`, `Badge.svelte`, `Button.svelte`, `Brand.svelte`, `Footer.svelte`, `Sidebar.svelte`, `Topbar.svelte`, `SkipLink.svelte`, `DemoForm.svelte`; layout `+layout.svelte`; tokens CSS do briefing.
- Especificação de design em `specs/LASTRO-Svelte-Specification.md`.
- Ajuste técnico pendente: `vite.config.js` usa import `sveltekit` (versão instalada pode exigir `vite-plugin-svelte`).
- Página inicial (`+page.svelte`) ainda não criada — conecta componentes ao conteúdo original.
- Site estático; não há backend para a conversão inicial (confirmado por Asta).

## Histórico

### 2026-10-29 — Conversão LASTRO para SvelteKit (componentes implementados, +page pendente)
- **Solicitação original:** converter site LASTRO para SvelteKit com design system do briefing, manter site original.
- **Agentes envolvidos:** Day (especificação de design), Asta (confirmação estática, sem backend), Anna (front-end — componentes e layout), Dakota (organização, documentação, Git).
- **Passos realizados:**
  1. Inspecionado estado real: `git status`, `git branch` (`main`), `git remote -v` (origin → GitHub).
  2. Verificado arquivos: `site/` preservado; `briefing.md`, `specs/LASTRO-Svelte-Specification.md` existem; `lastro-sveltekit/src/lib/components/` com 10 componentes + `+layout.svelte`; `+page.svelte` ausente.
  3. Verificado `vite.config.js`: import `sveltekit` pode ser incorreto para versão instalada.
  4. Criado `contexto.md` na raiz com registro completo.
  5. Preparado `git add` (excluído `node_modules`; incluídos `lastro-sveltekit/src/`, `specs/`, `contexto.md`). `.gitignore` já presente em `lastro-sveltekit/`.
  6. Commit realizado; push para `origin/main` executado.
- **Arquivos alterados/criados:** `contexto.md` (novo); `lastro-sveltekit/` (novo projeto, não listado item a item aqui — ver `git log` / `git diff --stat`); `specs/` já existia.
- **Pendências:**
  - [ ] Criar `lastro-sveltekit/src/routes/+page.svelte` (página inicial conectando componentes ao conteúdo do site original).
  - [ ] Corrigir `lastro-sveltekit/vite.config.js` (import de plugin SvelteKit).
  - [ ] Confirmar build/preview (`adapter-static`) e verificar se todos os componentes estão integrados corretamente.
  - [ ] Revisar acessibilidade e tokens CSS contra `briefing.md` e `specs/`.

## Modelo para novas entradas
```
### AAAA-MM-DD — Título curto da tarefa (solicitação original)
- **Solicitação:** ...
- **Agentes:** ...
- **Passos:** 1. ... 2. ... 3. ...
- **Arquivos:** ...
- **Pendências:**
  - [ ] ...
```
