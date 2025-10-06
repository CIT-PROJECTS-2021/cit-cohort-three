# CIT Python Course Documentation Site

This directory contains a documentation site built with [Fumadocs](https://fumadocs.dev/) and Next.js that aggregates all the Python lesson materials from the repository into a single, browsable website.

## Features

- 📚 **Organized Content**: Lessons organized by week with sidebar navigation
- 🔍 **Search Functionality**: Quick search across all documentation
- 📱 **Responsive Design**: Works on all devices
- 🌓 **Dark Mode**: Toggle between light and dark themes
- 📖 **Table of Contents**: Auto-generated TOC for each page

## Getting Started

### Prerequisites

- Node.js 20 or higher
- npm

### Installation

```bash
cd docs
npm install
```

### Development

Run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build

Build the production site:

```bash
npm run build
```

## Content Structure

The documentation content is located in `content/docs/` and is organized by weeks:

- `index.mdx` - Homepage/Introduction
- `week2/` - Control Flow
- `week3/` - Functions, OOP, Modules, Exceptions
- `week4/` - File Handling
- `week6/` - Data Structures and Algorithms
- `week8/` - Cryptography
- `assignments/` - Assignments and Solutions

## Deployment

This site can be deployed to:

- **Vercel** (recommended): Connect your GitHub repository and deploy automatically
- **Netlify**: Import the project and configure build settings
- **GitHub Pages**: Build and deploy the static output

### Deploy to Vercel

1. Push this repository to GitHub
2. Go to [Vercel](https://vercel.com)
3. Import your repository
4. Set the root directory to `docs`
5. Deploy!

## Technology Stack

- **Next.js 15** - React framework
- **Fumadocs** - Documentation framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **MDX** - Enhanced Markdown

## Project Structure

In the project, you can see:

- `lib/source.ts`: Code for content source adapter, [`loader()`](https://fumadocs.dev/docs/headless/source-api) provides the interface to access your content.
- `lib/layout.shared.tsx`: Shared options for layouts, optional but preferred to keep.

| Route                     | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| `app/(home)`              | The route group for your landing page and other pages. |
| `app/docs`                | The documentation layout and pages.                    |
| `app/api/search/route.ts` | The Route Handler for search.                          |

### Fumadocs MDX

A `source.config.ts` config file has been included, you can customise different options like frontmatter schema.

Read the [Introduction](https://fumadocs.dev/docs/mdx) for further details.

## Learn More

To learn more about Next.js and Fumadocs, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [Fumadocs](https://fumadocs.dev) - learn about Fumadocs

## License

Same as the main repository.
