import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
      port: 3000, // The port number should match the one exposed by your Docker container
      host: '0.0.0.0',
  },
})
