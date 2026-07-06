# Scripts

Store short, repeatable project entry points in this directory.

Scripts may build an image, start QEMU, download a documented artifact, run a
demo, or deploy to a Raspberry Pi 5. Keep business and inference logic in
`src/`, not in shell scripts.

Every script must fail on errors, accept configuration through explicit
arguments or environment variables, and document its usage at the top.
