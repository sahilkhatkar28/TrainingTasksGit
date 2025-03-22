import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'



export default defineConfig({
  server: {
    proxy: {
      '/upload': 'http://localhost:5000',
      '/images': 'http://localhost:5000',
      '/delete': 'http://localhost:5000',
    },
  },
});
