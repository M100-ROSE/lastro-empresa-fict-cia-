<script>
  import { onMount } from 'svelte';

  let formData = {
    nome: '',
    email: '',
    empresa: '',
    cargo: '',
    contas: '',
    erp: ''
  };

  let errors = {};
  let submitting = false;
  let submitted = false;

  onMount(() => {
    const form = document.querySelector('form');
    if (form) {
      const observer = new window.IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add('animate');
            }
          });
        },
        { threshold: 0.1 }
      );
      observer.observe(form);
    }
  });

  function validateField(field, value) {
    let error = '';
    switch (field) {
      case 'nome':
        if (!value.trim()) error = 'Nome é obrigatório';
        break;
      case 'email':
        if (!value.trim()) {
          error = 'E-mail é obrigatório';
        } else if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(value)) {
          error = 'E-mail inválido';
        }
        break;
      case 'empresa':
        if (!value.trim()) error = 'Empresa é obrigatória';
        break;
      case 'cargo':
        if (!value.trim()) error = 'Cargo é obrigatório';
        break;
      case 'contas':
        if (!value.trim()) error = 'Número de contas é obrigatório';
        break;
      case 'erp':
        if (!value.trim()) error = 'ERP é obrigatório';
        break;
    }
    return error;
  }

  function handleInput(e) {
    const { name, value } = e.target;
    errors = { ...errors, [name]: validateField(name, value) };
    formData = { ...formData, [name]: value };
  }

  async function handleSubmit(e) {
    e.preventDefault();

    const newErrors = {};
    Object.keys(formData).forEach((key) => {
      newErrors[key] = validateField(key, formData[key]);
    });

    if (Object.values(newErrors).some((err) => err)) {
      errors = newErrors;
      return;
    }

    submitting = true;

    await new Promise((resolve) => setTimeout(resolve, 1000));

    submitting = false;
    submitted = true;

    formData = {
      nome: '',
      email: '',
      empresa: '',
      cargo: '',
      contas: '',
      erp: ''
    };
    errors = {};
  }
</script>

{#if submitted}
  <div class="demo-form-success">
    <h3>✅ Recebido. Nosso time comercial responde em até 1 dia útil com uma agenda.</h3>
  </div>
{:else}
  <form class="demo-form" on:submit|preventDefault={handleSubmit} novalidate>
    <h3 class="demo-form__title mono">Agendar demo</h3>

    <div class="demo-form__fields">
      <div class="form-group">
        <label for="nome">Nome *</label>
        <input type="text" id="nome" name="nome" value={formData.nome} on:input={handleInput} class:error={errors.nome} />
        {#if errors.nome}
          <span class="error-message">{errors.nome}</span>
        {/if}
      </div>

      <div class="form-group">
        <label for="email">E-mail corporativo *</label>
        <input type="email" id="email" name="email" value={formData.email} on:input={handleInput} class:error={errors.email} />
        {#if errors.email}
          <span class="error-message">{errors.email}</span>
        {/if}
      </div>

      <div class="form-group">
        <label for="empresa">Empresa *</label>
        <input type="text" id="empresa" name="empresa" value={formData.empresa} on:input={handleInput} class:error={errors.empresa} />
        {#if errors.empresa}
          <span class="error-message">{errors.empresa}</span>
        {/if}
      </div>

      <div class="form-group">
        <label for="cargo">Cargo *</label>
        <input type="text" id="cargo" name="cargo" value={formData.cargo} on:input={handleInput} class:error={errors.cargo} />
        {#if errors.cargo}
          <span class="error-message">{errors.cargo}</span>
        {/if}
      </div>

      <div class="form-group">
        <label for="contas">Quantas contas bancárias a operação movimenta? *</label>
        <select id="contas" name="contas" value={formData.contas} on:change={handleInput} class:error={errors.contas}>
          <option value="">Selecione...</option>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="6+">6 ou mais</option>
        </select>
        {#if errors.contas}
          <span class="error-message">{errors.contas}</span>
        {/if}
      </div>

      <div class="form-group">
        <label for="erp">Quais ERPs utiliza? *</label>
        <select id="erp" name="erp" value={formData.erp} on:change={handleInput} class:error={errors.erp}>
          <option value="">Selecione...</option>
          <option value="totvs">TOTVS</option>
          <option value="sap">SAP Business One</option>
          <option value="omie">Omie</option>
          <option value="conta-azul">Conta Azul</option>
          <option value="micro-siga">MicroSiga</option>
          <option value="outro">Outro</option>
        </select>
        {#if errors.erp}
          <span class="error-message">{errors.erp}</span>
        {/if}
      </div>
    </div>

    <button type="submit" class="btn btn--primary" disabled={submitting} aria-busy={submitting}>
      {#if submitting}
        <span class="btn__spinner" aria-hidden="true"></span>
        <span>Enviando…</span>
      {:else}
        <span>Enviar</span>
      {/if}
    </button>
  </form>
{/if}