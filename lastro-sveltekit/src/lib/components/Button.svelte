<script>
  /**
   * @param {{
   *   variant?: 'primary' | 'secondary' | 'light' | 'ghost',
   *   size?: 'sm' | 'md',
   *   disabled?: boolean,
   *   loading?: boolean,
   *   href?: string,
   *   loadingText?: string,
   *   children?: any,
   *   ...rest
   * }} props
   */
  let {
    variant = 'primary',
    size = 'md',
    disabled = false,
    loading = false,
    href = undefined,
    loadingText = 'Agendando…',
    children,
    ...rest
  } = $props();

  const classes = `btn btn--${variant} ${size === 'sm' ? 'btn--sm' : ''} ${disabled ? 'btn--disabled' : ''}`;
</script>

{#if href}
  <a class={classes} href={href} disabled={disabled} aria-disabled={disabled} aria-busy={loading} {...rest}>
    {#if loading}
      <span class="btn__spinner" aria-hidden="true"></span>
      <span>{loadingText}</span>
    {:else}
      {@render children()}
    {/if}
  </a>
{:else}
  <button class={classes} type="button" disabled={disabled} aria-busy={loading} {...rest}>
    {#if loading}
      <span class="btn__spinner" aria-hidden="true"></span>
      <span>{loadingText}</span>
    {:else}
      {@render children()}
    {/if}
  </button>
{/if}