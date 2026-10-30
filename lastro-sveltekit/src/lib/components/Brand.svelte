<script>
  /** @param {'default' | 'compact'} variant */
  let { variant = 'default' } = $props();
</script>

<a class="brand {variant === 'compact' ? 'brand--compact' : ''}" href="#visao-geral" aria-label="LASTRO — início">
  <span class="brand__mark" aria-hidden="true"></span>
  LASTRO
</a>