import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

export function baseOptions(): BaseLayoutProps {
  return {
    nav: {
      title: 'CIT Python Course',
    },
    links: [
      {
        text: 'GitHub',
        url: 'https://github.com/CIT-PROJECTS-2021/cit-cohort-three',
      },
    ],
  };
}
