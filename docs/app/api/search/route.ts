import { source } from '@/lib/source';
import { createFromSource } from 'fumadocs-core/search/server';

// `staticGET` emits the whole search index as a static file at build time, so
// search keeps working on GitHub Pages, which cannot run server code.
export const revalidate = false;

export const { staticGET: GET } = createFromSource(source, {
  // https://docs.orama.com/docs/orama-js/supported-languages
  language: 'english',
});
