# AGENTS.md

These instructions apply to the entire repository.

## Project Scope

This repository hosts AI/ML features and integration experiments for an
Automotive Grade Linux in-vehicle infotainment environment.

Keep the repository compact. Add a directory only when it establishes a useful
ownership boundary for multiple files.

## Working Rules

- Read `README.md` and relevant documents before editing.
- Keep changes focused on the requested behavior.
- Write all source code, names, documentation, and comments in English.
- Add or update focused tests for behavior changes.
- Run the documented validation commands before reporting completion.
- Do not commit secrets, logs, datasets, model binaries, or build output.

## Function Comments

Place comments immediately before a function. Keep them brief and use `Brief`,
`Params`, and `Returns` when those fields apply.

Omit `Params` when a function has no parameters. Omit `Returns` when a function
does not return a value. Do not place comments inside function bodies.

```c
/**
 * Brief: Loads an inference model from disk.
 * Params:
 *   path: Path to the model artifact.
 * Returns: Zero on success, otherwise a negative error code.
 */
int load_model(const char *path);
```

Prefer clear names and small functions over explanatory comments.

## Validation

Run from the repository root:

```bash
python3 -c "from pip._vendor import tomli; tomli.loads(open('pyproject.toml').read())"
PYTHONPATH=src python3 -m unittest discover -s tests -v
```
