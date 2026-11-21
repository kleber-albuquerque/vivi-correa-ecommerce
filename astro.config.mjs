import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import pagefind from "astro-pagefind";

export default defineConfig({
  site: 'https://vivicorrea.com.br',
  integrations: [pagefind()],
  vite: {
    plugins: [tailwindcss()]
  }
});