import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
// import pagefind from 'astro-pagefind'; // Descomente se usar o Pagefind

export default defineConfig({
  base: '/vivi-correa-ecommerce/',
  output: 'static',
  integrations: [
    // pagefind(), // Mantenha suas outras integrações aqui
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});
