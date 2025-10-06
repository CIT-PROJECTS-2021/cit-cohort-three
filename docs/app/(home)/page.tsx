import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="flex flex-1 flex-col justify-center px-4 py-12">
      <div className="mx-auto max-w-4xl text-center">
        <h1 className="mb-6 text-4xl font-bold md:text-5xl lg:text-6xl">
          CIT Python Cloud Software Engineering
        </h1>
        <p className="mb-8 text-lg text-fd-muted-foreground md:text-xl">
          Master Python programming and AWS Cloud technologies through comprehensive, 
          hands-on lessons organized week by week.
        </p>
        
        <div className="mb-12 flex flex-col gap-4 sm:flex-row sm:justify-center">
          <Link
            href="/docs"
            className="rounded-lg bg-fd-primary px-6 py-3 font-semibold text-fd-primary-foreground transition-colors hover:bg-fd-primary/90"
          >
            Get Started
          </Link>
          <Link
            href="https://github.com/CIT-PROJECTS-2021/cit-cohort-three"
            target="_blank"
            rel="noopener noreferrer"
            className="rounded-lg border border-fd-border px-6 py-3 font-semibold transition-colors hover:bg-fd-accent"
          >
            View on GitHub
          </Link>
        </div>

        <div className="grid gap-6 md:grid-cols-3">
          <div className="rounded-lg border border-fd-border p-6">
            <h3 className="mb-2 text-xl font-semibold">📚 Comprehensive Curriculum</h3>
            <p className="text-fd-muted-foreground">
              From Python basics to advanced topics like data structures, OOP, and cloud engineering
            </p>
          </div>
          <div className="rounded-lg border border-fd-border p-6">
            <h3 className="mb-2 text-xl font-semibold">💻 Hands-on Learning</h3>
            <p className="text-fd-muted-foreground">
              Practical examples, code snippets, and real-world projects to reinforce concepts
            </p>
          </div>
          <div className="rounded-lg border border-fd-border p-6">
            <h3 className="mb-2 text-xl font-semibold">🚀 Career Ready</h3>
            <p className="text-fd-muted-foreground">
              Build a portfolio-worthy final project and prepare for AWS and Python certifications
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}
