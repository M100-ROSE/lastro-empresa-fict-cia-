<script>
  import Brand from './Brand.svelte';
  import Badge from './Badge.svelte';

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

<aside class="sidebar" aria-label="Navegação lateral">
  <Brand variant="default" />
  <p class="sidebar__meta mono">TESOURARIA · CONCILIAÇÃO</p>
  <nav class="sidebar__nav" aria-label="Seções da home">
    <ul>
      {#each items as item (item.id)}
        <li><a href={'#' + item.id} aria-current={item.id === 'visao-geral' ? 'page' : undefined}>{item.label}</a></li>
      {/each}
    </ul>
  </nav>
  <div class="sidebar__foot">
    <p class="status"><span class="status__dot" aria-hidden="true"></span>Todos os sistemas operacionais</p>
    <p class="sidebar__version mono">v2.4.1 · 26 OUT 2026</p>
  </div>
</aside>