<script>
  import Topbar from '../lib/components/Topbar.svelte';
  import Sidebar from '../lib/components/Sidebar.svelte';
  import Footer from '../lib/components/Footer.svelte';
</script>

<div class="app">
  <Topbar />

  <main id="main">
    <slot />
  </main>

  <Sidebar />

  <Footer />
</div>

<style>
  /* Layout global */
  :global(html) {
    font-family: var(--sans);
    font-size: 1rem;
    line-height: 1.63;
    font-variant-numeric: tabular-nums;
    -webkit-font-smoothing: antialiased;
  }

  :global(body) {
    margin: 0;
    background: var(--bg);
    color: var(--ink);
  }

  :global(h1, h2, h3, p, dl, dd, figure, blockquote) {
    margin: 0;
  }

  :global(h1, h2, h3) {
    font-weight: 600;
  }

  :global(h1) {
    letter-spacing: -0.02em;
    line-height: 1.08;
  }

  :global(h2) {
    letter-spacing: -0.01em;
    line-height: 1.27;
  }

  :global(a) {
    color: inherit;
    text-decoration: none;
  }

  :global(ul) {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  :global(svg) {
    display: block;
    max-width: 100%;
  }

  :global(.mono) {
    font-family: var(--mono);
  }

  :global(:where(a, [tabindex]):focus-visible) {
    outline: 2px solid var(--blue);
    outline-offset: 2px;
    box-shadow: 0 0 0 2px var(--surface);
  }

  :global(.sr-only) {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0 0 0 0);
    white-space: nowrap;
    border: 0;
  }

  :global(.skip-link) {
    position: absolute;
    top: -100px;
    left: 8px;
    z-index: 100;
    padding: 10px 16px;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: var(--radius-sm);
    font-size: .875rem;
    font-weight: 500;
  }

  :global(.skip-link:focus) {
    top: 8px;
  }
</style>