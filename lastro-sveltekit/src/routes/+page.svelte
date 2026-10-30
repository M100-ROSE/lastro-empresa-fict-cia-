<script>
  import Hero from "../lib/components/Hero.svelte";
  import Panel from "../lib/components/Panel.svelte";
  import Badge from "../lib/components/Badge.svelte";
  import Brand from "../lib/components/Brand.svelte";
</script>

<Hero />

<section class="section" id="conciliacao" aria-labelledby="conciliacao-title">
  <header class="section__head">
    <div>
      <p class="eyebrow">CONCILIAÇÃO · AMOSTRA</p>
      <h2 id="conciliacao-title">Toda baixa tem comprovante. Toda divergência tem dono.</h2>
    </div>
    <p class="section__meta mono">5 DE 1.284 TRANSAÇÕES<br>26 OUT 2026 · 08:42</p>
  </header>

  <div class="card tablecard">
    <div class="tablecard__head">
      <h3>Extrato conciliado — conta principal</h3>
      <span class="tablecard__meta mono">97,8% DO DIA</span>
    </div>
    <div class="table-scroll" tabindex="0" role="region" aria-label="Tabela de transações conciliadas, com rolagem horizontal">
      <table>
        <caption class="sr-only">Amostra de cinco transações de 26 de outubro de 2026, com data, banco, descrição, valor e status de conciliação.</caption>
        <thead>
          <tr>
            <th scope="col">Data</th>
            <th scope="col">Banco</th>
            <th scope="col">Descrição</th>
            <th scope="col" class="num">Valor</th>
            <th scope="col">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><time class="mono" datetime="2026-10-26T08:31">26/10 08:31</time></td>
            <td class="bank">Itaú</td>
            <td class="desc">Pix recebido — NF 4.812</td>
            <td class="num">—</td>
            <td><Badge variant="ok" label="Conciliado" /></td>
          </tr>
          <tr>
            <td><time class="mono" datetime="2026-10-26T08:29">26/10 08:29</time></td>
            <td class="bank">Bradesco</td>
            <td class="desc">TED enviada — fornecedor 221</td>
            <td class="num">—</td>
            <td><Badge variant="ok" label="Conciliado" /></td>
          </tr>
          <tr>
            <td><time class="mono" datetime="2026-10-26T08:14">26/10 08:14</time></td>
            <td class="bank">Santander</td>
            <td class="desc">Cartão — adquirente Cielo</td>
            <td class="num">—</td>
            <td><Badge variant="warn" label="Divergente" /></td>
          </tr>
          <tr>
            <td><time class="mono" datetime="2026-10-26T07:58">26/10 07:58</time></td>
            <td class="bank">Banco do Brasil</td>
            <td class="desc">Tarifa bancária — pacote</td>
            <td class="num">—</td>
            <td><Badge variant="pend" label="Pendente" /></td>
          </tr>
          <tr>
            <td><time class="mono" datetime="2026-10-26T07:42">26/10 07:42</time></td>
            <td class="bank">Itaú</td>
            <td class="desc">Pix enviado — folha 10/2026</td>
            <td class="num">—</td>
            <td><Badge variant="ok" label="Conciliado" /></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="tablecard__foot">
      <span class="mono">FONTE: EXTRATOS BANCÁRIOS · LOGS IMUTÁVEIS</span>
      <a href="#seguranca">Ver trilha de auditoria ?</a>
    </div>
  </div>
</section>

<section class="section" id="produto" aria-labelledby="produto-title">
  <header class="section__head">
    <div>
      <p class="eyebrow">MÓDULOS</p>
      <h2 id="produto-title">Três rotinas, um único lastro.</h2>
    </div>
    <p class="section__meta mono">PRODUTO / 3 MÓDULOS<br>IMPLEMENTAÇÃO ASSISTIDA</p>
  </header>

  <div class="cards">
    <article class="card product">
      <p class="product__index mono">MÓDULO 01</p>
      <h3>Conciliação</h3>
      <p>Bancos, Pix, cartões e adquirentes no mesmo extrato, com regra por contraparte e histórico de baixa.</p>
      <ul class="ticks">
        <li>Importação por OFX, CNAB e API</li>
        <li>Regra por contraparte e histórico</li>
        <li>Divergência com responsável e prazo</li>
      </ul>
      <p class="product__foot mono">12 BANCOS · PIX · CARTÕES</p>
    </article>

    <article class="card product">
      <p class="product__index mono">MÓDULO 02</p>
      <h3>Tesouraria</h3>
      <p>Saldo consolidado por empresa e conta, previsão de caixa de 90 dias e aprovação por alçada.</p>
      <ul class="ticks">
        <li>Saldo consolidado em tempo real</li>
        <li>Previsão de caixa de 90 dias</li>
        <li>Alçadas e segregação de função</li>
      </ul>
      <p class="product__foot mono">MULTIEMPRESA · MULTIBANCO</p>
    </article>

    <article class="card product">
      <p class="product__index mono">MÓDULO 03</p>
      <h3>Fechamento</h3>
      <p>Competência, provisões e trilha de auditoria no mesmo período, prontos para o ERP e para o balanço.</p>
      <ul class="ticks">
        <li>Competência e provisões automáticas</li>
        <li>Trilha de auditoria imutável</li>
        <li>Exportação para TOTVS e SAP B1</li>
      </ul>
      <p class="product__foot mono">FECHAMENTO EM 2,1 DIAS</p>
    </article>
  </div>
</section>

<section class="section" id="clientes" aria-labelledby="clientes-title">
  <header class="section__head">
    <div>
      <p class="eyebrow">CLIENTES</p>
      <h2 id="clientes-title">Operações que fecham com lastro.</h2>
    </div>
    <p class="section__meta mono">6 EMPRESAS · 3 SETORES<br>FAIXAS SOB CONSULTA</p>
  </header>

  <ul class="clients">
    <li>GRUPO MERIDIANO</li>
    <li>NOVA AGRO</li>
    <li>ATLÂNTICO LOG</li>
    <li>VÉRTICE SAÚDE</li>
    <li>CASA FORTE</li>
    <li>PAMPA ENERGIA</li>
  </ul>

  <blockquote class="quote">
    <p>“Saímos de 11 dias de fechamento para 3, com a mesma equipe. A diferença foi parar de caçar extrato.”</p>
    <footer>Controller financeiro · Grupo Meridiano · 38 contas, 14 empresas</footer>
  </blockquote>
</section>

<section class="section" id="seguranca" aria-labelledby="seguranca-title">
  <header class="section__head">
    <div>
      <p class="eyebrow">SEGURANÇA E INTEGRAÇÕES</p>
      <h2 id="seguranca-title">Controle verificável, integração direta.</h2>
    </div>
    <p class="section__meta mono">SOC 2 TIPO II · ISO 27001<br>RELATÓRIOS SOB NDA</p>
  </header>

  <div class="security">
    <div class="card security__list">
      <ul>
        <li>
          <div class="security__item-head"><h3>SOC 2 Tipo II</h3><span class="mono">2026</span></div>
          <p>Relatório anual de controles com 12 meses de observação e escopo de operação.</p>
        </li>
        <li>
          <div class="security__item-head"><h3>ISO/IEC 27001</h3><span class="mono">2025</span></div>
          <p>Certificação de infraestrutura, desenvolvimento e suporte ao cliente.</p>
        </li>
        <li>
          <div class="security__item-head"><h3>LGPD</h3><span class="mono">CONTÍNUO</span></div>
          <p>DPA, registro de operações e lista de subprocessadores publicada.</p>
        </li>
        <li>
          <div class="security__item-head"><h3>Criptografia e acesso</h3><span class="mono">AES-256</span></div>
          <p>AES-256 em repouso, TLS 1.3 em trânsito, SSO/SAML e logs imutáveis.</p>
        </li>
      </ul>
    </div>

    <div class="card security__side" id="integracoes">
      <h3>Integrações homologadas</h3>
      <p>40+ bancos, Pix e adquirentes. ERPs com importação e exportação validadas por versão.</p>
      <ul class="chips">
        <li>Itaú</li>
        <li>Bradesco</li>
        <li>Banco do Brasil</li>
        <li>Santander</li>
        <li>TOTVS</li>
        <li>SAP Business One</li>
        <li>Omie</li>
        <li>Conta Azul</li>
      </ul>
      <div class="uptime">
        <span class="mono">DISPONIBILIDADE 12 MESES</span>
        <strong>99,95%</strong>
      </div>
      <p class="note mono">NÃO ENCONTROU SEU BANCO? <a href="#demo">FALE COM A ENGENHARIA ?</a></p>
    </div>
  </div>
</section>

<section class="section section--last" id="demo" aria-labelledby="demo-title">
  <div class="cta">
    <div class="cta__copy">
      <p class="eyebrow eyebrow--inverse">DEMO · 30 MINUTOS</p>
      <h2 id="demo-title">Veja seu fechamento em 30 minutos.</h2>
      <p>Traga um extrato e uma conta a conciliar. Mostramos a baixa, a divergência e a trilha de auditoria no seu cenário, sem instalação.</p>
    </div>
    <div class="cta__actions">
      <a class="btn btn--light" href="mailto:comercial@lastro.com.br">Agendar demo</a>
      <a class="btn btn--ghost" href="#seguranca">Ver segurança</a>
      <ul class="cta__meta mono">
        <li>RESPOSTA EM 1 DIA ÚTIL</li>
        <li>SÃO PAULO · REMOTO</li>
        <li>SEM INSTALAÇÃO</li>
      </ul>
    </div>
  </div>
</section>

