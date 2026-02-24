'use client';

import { useEffect, useId, useMemo, useState } from 'react';
import { useTheme } from 'next-themes';

const renderCache = new Map<string, Promise<string>>();

async function renderMermaid(code: string, id: string, theme: string) {
  const mermaid = (await import('mermaid')).default;
  mermaid.initialize({
    startOnLoad: false,
    theme: theme === 'dark' ? 'dark' : 'default',
  });

  const { svg } = await mermaid.render(id, code);
  return svg;
}

export function Mermaid({
  code,
  children,
}: {
  code?: string;
  children?: string;
}) {
  const { resolvedTheme } = useTheme();
  const [svg, setSvg] = useState<string | null>(null);
  const diagramId = useId().replace(/[:]/g, '');

  const theme = resolvedTheme ?? 'light';
  const content = typeof code === 'string' ? code : children ?? '';
  const cacheKey = useMemo(() => `${theme}:${content}`, [theme, content]);

  useEffect(() => {
    let cancelled = false;

    if (!content.trim()) return;

    const promise =
      renderCache.get(cacheKey) ??
      renderMermaid(content, `mermaid-${diagramId}`, theme);

    renderCache.set(cacheKey, promise);

    promise.then((data) => {
      if (!cancelled) {
        setSvg(data);
      }
    });

    return () => {
      cancelled = true;
    };
  }, [cacheKey, content, diagramId, theme]);

  return (
    <div
      className="my-4 w-full overflow-x-auto rounded-lg border border-fd-border bg-fd-muted/30 p-3"
      dangerouslySetInnerHTML={{ __html: svg ?? '' }}
    />
  );
}
