<script>
  import Brand from './Brand.svelte';

  /** @type {{ items?: Array<{ id: string; label: string }> }} props */
  let { items = [
    { id: 'visao-geral', label: 'Visão geral' },
    { id: 'produto', label: 'Produto' },
    { id: 'conciliacao', label: 'Conciliação' },
    { id: 'integracoes', label: 'Integrações' },
    { id: 'seguranca', label: 'Segurança' },
    { id: 'clientes', label: 'Clientes' },
    { id: 'demo', label: 'Demo' },
  ] } = $props();
</script>

<header class="topbar">
  <div class="topbar__bar">
    <Brand variant="compact" />
    <p class="crumbs"><span>Console</span><span aria-hidden="true">/</span><strong>Visão geral</strong></p>
    <div class="topbar__actions">
      <span class="lang">PT-BR</span>
      <a class="link-quiet" href="#demo">Entrar</a>
      <Button href="#demo" variant="primary">Agendar demo</Button>
    </div>
  </div>
  <nav class="topnav" aria-label="Navegação da home">
    {#each items as item (item.id)}
      <a href={'#' + item.id} aria-current={item.id === 'visao-geral' ? 'page' : undefined}>{item.label}</a>
    {/each}
  </nav>
</header>