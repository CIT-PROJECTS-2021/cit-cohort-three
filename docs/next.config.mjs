import { createMDX } from 'fumadocs-mdx/next';

const withMDX = createMDX();

// GitHub Pages serves this repository at https://<owner>.github.io/<repo>/,
// so the site needs a base path and a fully static build. Both are opted into
// by the deployment workflow and stay off for local development, where
// `npm run dev` and `npm run start` behave exactly as before.
const isGitHubPages = process.env.GITHUB_PAGES === 'true';
const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? '';

/** @type {import('next').NextConfig} */
const config = {
  reactStrictMode: true,
  ...(isGitHubPages
    ? {
        output: 'export',
        basePath,
        // Pages has no image optimisation server.
        images: { unoptimized: true },
        // Emit `about/index.html` rather than `about.html` so static hosting
        // resolves nested routes without extra rewrite rules.
        trailingSlash: true,
      }
    : {}),
};

export default withMDX(config);
