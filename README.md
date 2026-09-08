# Movera Driver

This repository is the canonical source of truth for the **Movera Driver** Flutter application.

## Architecture

- `lib/features/driver/` — Driver-only product features and screens
- `lib/core/constants/` — app-wide constants, colors, assets and typography configuration
- `lib/core/services/` — Driver app services
- `lib/shared/models/` — Driver data models used across features
- `lib/shared/widgets/` — reusable UI widgets
- `lib/shared/presentation/` — shared presentation such as splash/onboarding
- `assets/` — original app assets, kept intact

Rider application code belongs only in the separate Movera Rider repository.
Generated Flutter/Gradle files, temporary upload ZIPs, and build output are intentionally not source-controlled.

## Google Maps configuration

Never commit Maps API keys. Android reads `MAPS_API_KEY` from a Gradle property or environment variable. iOS reads `GOOGLE_MAPS_API_KEY` from the Xcode build setting exposed through `Info.plist`.
