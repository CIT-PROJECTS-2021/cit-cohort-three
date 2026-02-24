import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="relative flex flex-1 flex-col overflow-hidden px-6 py-16">
      <div className="pointer-events-none absolute inset-0 bg-[radial-gradient(circle_at_top_left,_rgba(59,130,246,0.16)_0%,_transparent_45%),radial-gradient(circle_at_top_right,_rgba(14,165,233,0.12)_0%,_transparent_40%),linear-gradient(180deg,_rgba(30,64,175,0.08),_transparent_65%)]" />
      <div className="pointer-events-none absolute -right-20 top-24 h-64 w-64 rounded-full bg-sky-500/10 blur-3xl" />
      <div className="pointer-events-none absolute -left-20 bottom-10 h-72 w-72 rounded-full bg-blue-500/10 blur-3xl" />

      <div className="mx-auto w-full max-w-6xl">
        <div className="grid items-center gap-10 lg:grid-cols-[1.1fr_0.9fr]">
          <div>
            <div className="inline-flex items-center gap-2 rounded-full border border-fd-border bg-fd-background/70 px-4 py-1 text-xs uppercase tracking-[0.18em] text-fd-muted-foreground">
              Cohort Three · Python Track
            </div>
            <h1 className="mt-6 text-4xl font-semibold leading-tight md:text-6xl">
              Build real software with Python.
              <span className="block text-fd-muted-foreground">
                Learn engineering, not just syntax.
              </span>
            </h1>
            <p className="mt-6 max-w-2xl text-lg text-fd-muted-foreground md:text-xl">
              A practical path from first script to structured software. Each
              week blends fundamentals, clean architecture, and hands‑on
              projects that feel like real engineering work.
            </p>

            <div className="mt-10 flex flex-col gap-4 sm:flex-row">
              <Link
                href="/docs"
                className="rounded-lg bg-fd-primary px-7 py-3 text-sm font-semibold uppercase tracking-wide text-fd-primary-foreground transition-colors hover:bg-fd-primary/90"
              >
                Start Learning
              </Link>
              <Link
                href="https://github.com/CIT-PROJECTS-2021/cit-cohort-three"
                target="_blank"
                rel="noopener noreferrer"
                className="rounded-lg border border-fd-border px-7 py-3 text-sm font-semibold uppercase tracking-wide text-fd-foreground transition-colors hover:bg-fd-accent"
              >
                View Repository
              </Link>
            </div>
          </div>

          <div className="relative">
            <div className="hero-editor rounded-2xl backdrop-blur">
              <div className="editor-bar flex items-center justify-between px-4 py-3">
                <div className="flex items-center gap-2">
                  <span className="h-2.5 w-2.5 rounded-full bg-red-400/80" />
                  <span className="h-2.5 w-2.5 rounded-full bg-yellow-400/80" />
                  <span className="h-2.5 w-2.5 rounded-full bg-green-400/80" />
                </div>
                <div className="rounded-full border border-fd-border/60 px-3 py-1 text-[10px] uppercase tracking-[0.2em] text-fd-muted-foreground">
                  Editor
                </div>
              </div>
              <div className="grid grid-cols-[160px_1fr]">
                <div className="editor-tree px-3 py-3 text-xs">
                  <div className="mb-2 text-[10px] uppercase tracking-[0.2em] text-fd-muted-foreground">
                    Explorer
                  </div>
                  <div className="space-y-1">
                    <div className="editor-tree-item">README.md</div>
                    <div className="editor-tree-item">week6/</div>
                    <div className="editor-tree-item">assignments/</div>
                    <div className="editor-tree-item active px-2 py-1">
                      engineering.py
                    </div>
                  </div>
                </div>
                <div>
                  <div className="editor-bar flex items-center justify-between px-4 py-2 text-xs text-fd-muted-foreground">
                    <span className="editor-tab rounded-md px-3 py-1">
                      engineering.py
                    </span>
                    <span className="text-[10px] uppercase tracking-[0.2em] text-fd-muted-foreground">
                      Python 3.12
                    </span>
                  </div>
                  <div className="grid grid-cols-[auto_1fr] gap-4 px-4 py-4 text-sm">
                    <div className="editor-gutter select-none text-right">
                      <div className="line-num">1</div>
                      <div className="line-num delay-1">2</div>
                      <div className="line-num delay-2">3</div>
                      <div className="line-num delay-3">4</div>
                      <div className="line-num delay-4">5</div>
                      <div className="line-num delay-4">6</div>
                      <div className="line-num delay-4">7</div>
                      <div className="line-num delay-4">8</div>
                    </div>
                    <div className="editor-code space-y-2">
                      <div className="editor-caret-line pl-2 editor-line">
                        <span className="editor-type done">
                          <span className="editor-keyword">def</span>{' '}
                          <span className="editor-func">ship</span>(feature):
                        </span>
                      </div>
                      <div className="pl-4 editor-line delay-1">
                        tests = run(feature)
                      </div>
                      <div className="pl-4 editor-line delay-2">
                        return deploy(tests)
                      </div>
                      <div className="mt-4 editor-callout rounded-lg px-3 py-2 editor-line delay-3">
                        $ python engineering.py
                        <span className="prompt" />
                      </div>
                      <div className="text-fd-muted-foreground terminal-line delay-1 flex items-center">
                        <span className="spinner" /> Running tests... OK
                      </div>
                      <div className="text-fd-muted-foreground terminal-line delay-2">
                        Deploying build... done
                      </div>
                      <div className="text-fd-muted-foreground terminal-line delay-3">
                        Build shipped ✓
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="absolute -bottom-6 -left-6 rounded-xl border border-fd-border/70 bg-fd-background/80 px-4 py-3 text-xs text-fd-muted-foreground shadow-md">
              Structured notes · Projects · Recaps
            </div>
          </div>
        </div>

        <div className="mt-14 grid gap-6 md:grid-cols-3">
          <div className="rounded-2xl border border-fd-border/80 bg-fd-background/70 p-6 text-left shadow-sm">
            <h3 className="text-xl font-semibold">Engineering mindset</h3>
            <p className="mt-3 text-sm text-fd-muted-foreground">
              Learn the why behind design choices, not just the how.
            </p>
          </div>
          <div className="rounded-2xl border border-fd-border/80 bg-fd-background/70 p-6 text-left shadow-sm">
            <h3 className="text-xl font-semibold">Python first</h3>
            <p className="mt-3 text-sm text-fd-muted-foreground">
              Clear syntax, strong fundamentals, and real problem‑solving.
            </p>
          </div>
          <div className="rounded-2xl border border-fd-border/80 bg-fd-background/70 p-6 text-left shadow-sm">
            <h3 className="text-xl font-semibold">Weekly momentum</h3>
            <p className="mt-3 text-sm text-fd-muted-foreground">
              Recaps, quizzes, and practice keep progress steady.
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}
