# Configurations

Store version-controlled runtime settings in this directory.

Suitable files include:

- QEMU machine and device settings
- AGL service endpoints
- Model input and output settings
- Feature flags for local experiments

Do not store credentials or machine-specific secrets here. Use a local `.env`
file based on a committed `.env.example` when secrets are introduced.
