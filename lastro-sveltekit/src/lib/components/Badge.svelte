<script>
  /**
   * @param {{ variant: 'ok' | 'warn' | 'pend'; label?: string }} props
   */
  let { variant, label = '' } = $props();
</script>

<span class="badge badge--{variant}">
  {#if variant === 'ok'}
    <span class="badge__icon" aria-hidden="true">✓</span>
  {:else if variant === 'warn'}
    <span class="badge__icon" aria-hidden="true">!</span>
  {:else if variant === 'pend'}
    <span class="badge__icon" aria-hidden="true">·</span>
  {/if}
  {label}
</span>