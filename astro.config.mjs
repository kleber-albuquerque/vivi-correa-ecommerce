import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  // Define o caminho base para funcionar no GitHub Pages
  base: '/vivi-correa-ecommerce/',
  output: 'static'
});
