# Architecture

## Boundaries

`src/agl_ivi_lab/` owns application behavior, inference adapters, and AGL
integration code. New modules should represent a specific IVI use case or an
external system boundary.

`configs/` owns version-controlled settings. Source modules may read settings
from this directory, but configuration files must not contain executable
application logic.

`scripts/` owns repeatable developer and deployment commands. Scripts call
package APIs or external tools instead of duplicating application behavior.

`artifacts/` owns local datasets and model files. Source code may reference
artifact paths through configuration, but must not assume a developer has
undocumented files.

## Runtime Direction

Development should begin with a generic QEMU target for application and service
integration. Raspberry Pi 5 hardware remains the validation target for HDMI,
DRM/KMS, GPU acceleration, audio routing, and board-specific behavior.

## Growth Rule

Keep the initial package flat. Introduce a subpackage only when a feature has
multiple related modules with a stable boundary and focused tests.
