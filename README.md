# AGL IVI AI Lab

A compact development lab for AI/ML features intended for an Automotive Grade
Linux in-vehicle infotainment environment.

The repository supports application and inference development in QEMU while
keeping hardware-specific Raspberry Pi 5 validation separate.

## Structure

```text
.
├── src/          Python application and integration code
├── tests/        Automated behavior tests
├── configs/      Version-controlled runtime and QEMU settings
├── scripts/      Build, run, download, and deployment entry points
├── artifacts/    Local datasets and model files
└── docs/         Architecture and engineering documentation
```

## Requirements

- Python 3.10 or newer
- Git
- QEMU and AGL build tools when an emulator target is introduced

## Validate

```bash
python3 -c "from pip._vendor import tomli; tomli.loads(open('pyproject.toml').read())"
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

## Development Direction

Start with one measurable IVI use case, such as voice intent recognition,
driver monitoring, or media recommendation. Select an inference framework only
after the target model and deployment constraints are known.
