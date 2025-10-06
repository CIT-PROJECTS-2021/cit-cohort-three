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

### Start Production Server

```bash
npm start
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

## Contributing

To add new content:

1. Create a new `.mdx` file in the appropriate week folder
2. Add frontmatter with `title` and `description`
3. Update `meta.json` to include the new page in navigation
4. Rebuild the site

## License

Same as the main repository.
