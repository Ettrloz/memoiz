import { djangoVitePlugin } from 'django-vite-plugin';
import fs from 'node:fs';
import path from 'node:path';
import { NodePackageImporter } from 'sass-embedded';
import { defineConfig, loadEnv } from 'vite';

export default defineConfig(({ command, mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  const devHost = env.DEV_HOST || 'localhost';
  const djangoPort = env.DJANGO_PORT || 9001;
  const vitePort = Number(env.VITE_PORT) || 9002;
  const devOrigin = devHost + ':' + djangoPort;

  const possiblePaths = [
    '.vercel/python/.venv/bin/python',
    '.venv/Scripts/python.exe',
    '.venv/bin/python',
    'python3',
    'python'
  ];

  const pyPath =
    possiblePaths.find(p => {
      // Jika path absolut/relatif, cek keberadaannya
      if (p.includes('/') || p.includes('\\')) {
        return fs.existsSync(path.resolve(import.meta.dirname, p));
      }

      return true;
    }) || 'python';

  return {
    base: command === 'build' ? '/static' : '/',
    css: {
      preprocessorOptions: {
        scss: {
          importers: [new NodePackageImporter()]
        }
      }
    },
    build: {
      outDir: path.resolve(import.meta.dirname, 'static'),
      emptyOutDir: true
    },
    server: {
      port: vitePort,
      host: true,
      hmr: {
        host: devHost
      },
      cors: {
        origin: [
          `http://${devOrigin}`,
          `http://localhost:${djangoPort}`,
          `http://127.0.0.1:${djangoPort}`
        ]
      },
      strictPort: true,
      allowedHosts: true
    },
    plugins: [
      djangoVitePlugin({
        input: ['resources/main.ts', 'resources/styles/index.scss'],
        pyPath: pyPath
      })
    ]
  };
});
