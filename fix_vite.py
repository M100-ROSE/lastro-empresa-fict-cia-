from pathlib import Path
p = Path("C:/Users/kaike/Documents/lastro-empresa-fict-cia-/lastro-sveltekit/vite.config.js")
p.write_text("import { svelte } from \\\"@sveltejs/vite-plugin-svelte\\\";\\nimport { defineConfig } from \\\"vite\\\";\\n\\nexport default defineConfig({\\n  plugins: [svelte()],\\n});\\n")
