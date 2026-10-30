<script>
  import Badge from './Badge.svelte';
  import Panel from './Panel.svelte';
</script>

<section class="hero" id="visao-geral" aria-labelledby="hero-title">
  <div class="hero__copy">
    <p class="eyebrow">CONCILIAÇÃO · TESOURARIA · FECHAMENTO</p>
    <h1 id="hero-title">Tesouraria sem planilha. Fechamento sem surpresa.</h1>
    <p class="lead">Concilie bancos, Pix e cartões em uma única trilha. Cada baixa com comprovante, cada divergência com responsável, cada fechamento com lastro.</p>
    <div class="hero__actions">
      <Button href="#demo" variant="primary">Agendar demo</Button>
      <Button href="#integracoes" variant="secondary">Ver integrações</Button>
    </div>
    <p class="micro">Demo de 30 min · sem instalação · resposta em 1 dia útil</p>
    <p class="hero__trust mono">SOC 2 TIPO II · ISO 27001 · LGPD · DISPONIBILIDADE 99,95%</p>
  </div>
  <Panel badgeVariant="ok" badgeLabel="Em dia" />
</section>
