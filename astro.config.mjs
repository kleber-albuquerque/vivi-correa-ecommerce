import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import pagefind from 'astro-pagefind';

export default defineConfig({
  // Usa base apenas se a variável de ambiente existir (build do GitHub Pages)
  base: process.env.GITHUB_PAGES === 'true' ? '/vivi-correa-ecommerce/' : '/',
  output: 'static',
  integrations: [pagefind()],
  vite: {
    plugins: [tailwindcss()],
  },
});
