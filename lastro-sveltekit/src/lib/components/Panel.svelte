<script>
  import Badge from './Badge.svelte';

  /** @type {{ badgeVariant?: 'ok' | 'warn' | 'pend'; badgeLabel?: string }} props */
  let { badgeVariant = 'ok', badgeLabel = 'Em dia' } = $props();
</script>

<div class="panel" role="group" aria-labelledby="panel-title">
  <div class="panel__head">
    <div>
      <p class="panel__title" id="panel-title">Painel de conciliação</p>
      <p class="panel__sub mono">FECHAMENTO OUT/2026 · SYNC 08:42</p>
    </div>
    <Badge variant={badgeVariant} label={badgeLabel} />
  </div>

  <dl class="kpis">
    <div class="kpi">
      <dt>Conciliação automática</dt>
      <dd><span class="kpi__value">98,4<span class="kpi__unit">%</span></span><span class="kpi__foot">+2,1 p.p. vs. set/26</span></dd>
    </div>
    <div class="kpi">
      <dd><span class="kpi__value">2,1<span class="kpi__unit">dias</span></span><span class="kpi__foot">meta interna: 3 dias</span></dd>
    </div>
    <div class="kpi">
      <dt>Volume conciliado</dt>
      <dd><span class="kpi__value">—</span><span class="kpi__foot">volume sob consulta · 12 bancos</span></dd>
    </div>
  </dl>

  <figure class="chart">
    <div class="chart__head">
      <span class="mono">CONCILIAÇÃO DIÁRIA · 30 DIAS</span>
      <span class="mono">MÉDIA 98,4%</span>
    </div>
    <svg class="chart__svg" viewBox="0 0 560 96" preserveAspectRatio="none" role="img" aria-labelledby="chart-title chart-desc">
      <title id="chart-title">Taxa de conciliação automática nos últimos 30 dias</title>
      <desc id="chart-desc">A taxa variou entre 96,9% e 99,1%, com média de 98,4%.</desc>
      <g stroke="#E8EDF2" stroke-width="1" vector-effect="non-scaling-stroke">
        <line x1="0" y1="8" x2="560" y2="8"></line>
        <line x1="0" y1="38" x2="560" y2="38"></line>
        <line x1="0" y1="68" x2="560" y2="68"></line>
        <line x1="0" y1="94" x2="560" y2="94"></line>
      </g>
      <path class="chart__area" d="M0 50 L40 46 L80 54 L120 42 L160 48 L200 36 L240 44 L280 30 L320 38 L360 26 L400 34 L440 20 L480 28 L520 16 L560 22 L560 96 L0 96 Z" fill="#0E7C86" fill-opacity="0.08"></path>
      <polyline class="chart__line" points="0,50 40,46 80,54 120,42 160,48 200,36 240,44 280,30 320,38 360,26 400,34 440,20 480,28 520,16 560,22" fill="none" stroke="#0E7C86" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"></polyline>
    </svg>
    <div class="chart__axis mono" aria-hidden="true"><span>01 OUT</span><span>12 OUT</span><span>26 OUT</span></div>
    <figcaption class="chart__note">Mínima de 96,9% em 12/10 · máxima de 99,1% em 21/10. Série ilustrativa, base 2026.</figcaption>
  </figure>

  <div class="panel__foot">
    <span class="mono">FONTE: EXTRATOS E ADQUIRENTES INTEGRADOS</span>
    <a href="#conciliacao">Abrir conciliação →</a>
  </div>
</div>
