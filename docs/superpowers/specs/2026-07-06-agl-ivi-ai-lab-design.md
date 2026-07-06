# AGL IVI AI Lab Design

## Purpose

Create a compact project for developing and testing AI/ML features intended for
an Automotive Grade Linux in-vehicle infotainment environment. The project must
also be easy for AI coding agents to understand and modify safely.

## Project Structure

```text
agl-ivi-lab/
├── AGENTS.md
├── README.md
├── .gitignore
├── pyproject.toml
├── src/
├── tests/
├── configs/
├── scripts/
├── artifacts/
│   ├── data/
│   └── models/
└── docs/
```

- `src/` contains application, inference, and AGL integration code.
- `tests/` mirrors the behavior exposed by `src/`.
- `configs/` contains version-controlled runtime, model, and QEMU settings.
- `scripts/` contains short build, run, download, and deployment entry points.
- `artifacts/` contains generated or downloaded datasets and models.
- `docs/` contains architecture, setup, and engineering decisions.
- `AGENTS.md` defines repository rules for AI coding agents.

Nested directories should only be introduced when a component has enough files
to justify a clear boundary.

## Language And Comment Rules

All source code, identifiers, documentation, commit-facing text, and comments
must be written in English.

Function comments must:

- Appear immediately before the function.
- Be concise.
- Use `Brief`, `Params`, and `Returns` fields when those fields apply.
- Omit `Params` for functions without parameters.
- Omit `Returns` for functions that do not return a value.

Comments must not appear inside function bodies. Code should instead use clear
names and small functions to explain its behavior.

Example:

```c
/**
 * Brief: Loads an inference model from disk.
 * Params:
 *   path: Path to the model artifact.
 * Returns: Zero on success, otherwise a negative error code.
 */
int load_model(const char *path);
```

## Tooling

Python project metadata belongs in `pyproject.toml`. Initial tooling should stay
minimal and provide formatting, linting, and tests without choosing an AI
framework before the first use case is known.

Large datasets, trained models, generated images, logs, and build output must
not be committed. Placeholder files may keep required artifact directories in
Git, and local setup instructions must explain how artifacts are obtained.

## Agent Workflow

`AGENTS.md` will instruct coding agents to:

1. Read `README.md` and relevant documents before editing.
2. Keep changes scoped to the requested behavior.
3. Add or update focused tests.
4. Run the documented checks before reporting completion.
5. Follow the English-only function comment convention.
6. Never commit secrets, datasets, model binaries, logs, or build output.

## Validation

The initial scaffold is complete when:

- The documented directory structure exists.
- Root documentation explains the project purpose and first development steps.
- Ignore rules protect large and generated artifacts.
- Python metadata is syntactically valid.
- A minimal test command can run successfully.
- AI-agent instructions contain the language and comment rules.
