# AGL IVI AI Lab Scaffold Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a compact, testable project scaffold for AGL IVI AI development and AI coding agents.

**Architecture:** Keep executable Python code in one source package and keep tests beside the project root. Store version-controlled settings separately from local model and data artifacts, while root documentation and `AGENTS.md` define the workflow for humans and coding agents.

**Tech Stack:** Python 3.11+, standard-library `unittest`, TOML project metadata, Git

---

### Task 1: Repository Rules And Metadata

**Files:**
- Create: `AGENTS.md`
- Create: `README.md`
- Create: `.gitignore`
- Create: `pyproject.toml`

- [ ] **Step 1: Add repository instructions**

Create `AGENTS.md` with the project scope, required checks, English-only rule,
function-header comment format, and artifact restrictions.

- [ ] **Step 2: Add project documentation**

Create `README.md` with the project purpose, directory map, setup commands, and
the first local validation command.

- [ ] **Step 3: Add project metadata and ignore rules**

Create `pyproject.toml` with Python 3.11 metadata and a `src` package layout.
Create `.gitignore` for Python caches, virtual environments, build output,
logs, local secrets, datasets, and model binaries.

- [ ] **Step 4: Validate TOML syntax**

Run:

```bash
python3 -c "import tomllib; tomllib.load(open('pyproject.toml', 'rb'))"
```

Expected: exit status 0 with no output.

- [ ] **Step 5: Commit repository metadata**

```bash
git add AGENTS.md README.md .gitignore pyproject.toml
git commit -m "chore: add project metadata and agent rules"
```

### Task 2: Minimal Python Package

**Files:**
- Create: `src/agl_ivi_lab/__init__.py`
- Create: `tests/test_package.py`

- [ ] **Step 1: Write the package test**

Create `tests/test_package.py`:

```python
import unittest

import agl_ivi_lab


class PackageTests(unittest.TestCase):
    def test_exposes_version(self) -> None:
        self.assertEqual(agl_ivi_lab.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test to verify it fails**

Run:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Expected: FAIL because `agl_ivi_lab` does not exist.

- [ ] **Step 3: Add the minimal package**

Create `src/agl_ivi_lab/__init__.py`:

```python
"""AGL IVI AI lab package."""

__version__ = "0.1.0"
```

- [ ] **Step 4: Run the test to verify it passes**

Run:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Expected: one passing test.

- [ ] **Step 5: Commit the package**

```bash
git add src tests
git commit -m "feat: add minimal AGL IVI lab package"
```

### Task 3: Supporting Project Areas

**Files:**
- Create: `configs/README.md`
- Create: `scripts/README.md`
- Create: `artifacts/README.md`
- Create: `artifacts/data/.gitkeep`
- Create: `artifacts/models/.gitkeep`
- Create: `docs/architecture.md`

- [ ] **Step 1: Document each supporting area**

Create focused README files describing which version-controlled configuration
files and scripts belong in their directories. Document that `artifacts/`
contains local data and model files that Git ignores.

- [ ] **Step 2: Add the architecture note**

Create `docs/architecture.md` describing the boundaries among application code,
AGL integration, configuration, scripts, and local artifacts.

- [ ] **Step 3: Verify the complete structure**

Run:

```bash
find . -maxdepth 3 -not -path './.git/*' -print | sort
```

Expected: all files listed in Tasks 1 through 3 are present.

- [ ] **Step 4: Run project validation**

Run:

```bash
python3 -c "import tomllib; tomllib.load(open('pyproject.toml', 'rb'))"
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Expected: TOML parsing succeeds and one test passes.

- [ ] **Step 5: Commit the supporting structure**

```bash
git add configs scripts artifacts docs/architecture.md
git commit -m "docs: add project area guidance"
```
