import type { Metadata } from "next";
import { RootProvider } from 'fumadocs-ui/provider';
import { Inter } from 'next/font/google';
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "CIT Python Cloud Software Engineering",
  description: "Documentation for CIT Python Cloud Software Engineering Course",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={inter.className} suppressHydrationWarning>
      <body>
        <RootProvider>{children}</RootProvider>
      </body>
    </html>
  );
}
