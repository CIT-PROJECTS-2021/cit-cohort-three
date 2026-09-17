import '@/app/global.css';
import { RootProvider } from 'fumadocs-ui/provider/next';
import { Fraunces, Source_Sans_3, JetBrains_Mono } from 'next/font/google';

const bodyFont = Source_Sans_3({
  subsets: ['latin'],
  variable: '--font-body',
  weight: ['300', '400', '500', '600', '700'],
});

const displayFont = Fraunces({
  subsets: ['latin'],
  variable: '--font-display',
  weight: ['400', '600', '700'],
});

const monoFont = JetBrains_Mono({
  subsets: ['latin'],
  variable: '--font-mono',
  weight: ['400', '500', '600'],
});

export default function Layout({ children }: LayoutProps<'/'>) {
  return (
    <html
      lang="en"
      className={`${bodyFont.variable} ${displayFont.variable} ${monoFont.variable}`}
      suppressHydrationWarning
    >
      <body className="flex flex-col min-h-screen">
        <RootProvider
          // The search index is prebuilt as a static file so search works on
          // static hosts such as GitHub Pages. The static client fetches the
          // index by a literal URL, so it needs the base path spelled out —
          // unlike `next/link`, it gets no prefix for free.
          search={{
            options: {
              type: 'static',
              api: `${process.env.NEXT_PUBLIC_BASE_PATH ?? ''}/api/search`,
            },
          }}
        >
          {children}
        </RootProvider>
      </body>
    </html>
  );
}
