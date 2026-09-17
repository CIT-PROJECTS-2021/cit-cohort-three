import defaultMdxComponents from 'fumadocs-ui/mdx';
import type { MDXComponents } from 'mdx/types';
import { Callout } from 'fumadocs-ui/components/callout';
import { Steps, Step } from 'fumadocs-ui/components/steps';
import { Tabs, Tab } from 'fumadocs-ui/components/tabs';
import { Cards, Card } from 'fumadocs-ui/components/card';
import { Accordions, Accordion } from 'fumadocs-ui/components/accordion';
import { Files, File, Folder } from 'fumadocs-ui/components/files';
import { TypeTable } from 'fumadocs-ui/components/type-table';
import { Mermaid } from '@/components/mdx/mermaid';

// use this function to get MDX components, you will need it for rendering MDX
export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultMdxComponents,
    Callout,
    Steps,
    Step,
    Tabs,
    Tab,
    Cards,
    Card,
    Accordions,
    Accordion,
    Files,
    File,
    Folder,
    TypeTable,
    Mermaid,
    ...components,
  };
}
