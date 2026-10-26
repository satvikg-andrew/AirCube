# Routing checkpoint 11 — not a fabrication release

Open `AirCube.kicad_pro` from this extracted folder, then open its PCB. Keep the supplied footprint folders and `fp-lib-table` alongside it. Press **B** to refill zones, save, and run the full DRC. Saved zone fills have intentionally been cleared.

Expected missing connections: **45 → 37** after refill. This is a geometric connectivity estimate; native KiCad DRC must confirm it.

Changes:
- Connected C23's 1.8 V decoupling supply, C38 ground, all four USB-C shield tabs to their resistor network, the remaining reset-switch contact, and U11 VBUS detect.
- Relocated U11 pin 5's ground return to permit VBUS-detect escape. Ground return remains connected.
- Removed the two obsolete dangling ground stubs left at the old C8/C9 locations.
- Hid C9 and S3 silkscreen reference text to resolve the four reported text overlaps/clipping warnings. References remain in PCB properties and assembly information.
- Added project-local copies of the two missing footprint libraries, recovered from the existing board, and enabled them in `fp-lib-table`. L1/L2/U11 pad geometry and board footprint IDs are unchanged. These address the three library-disabled warnings when this project is opened with its supplied table; library matching still needs native KiCad verification.

Independent geometric checks: no new different-net overlaps, clearance failures below 0.1524 mm, drill-spacing failures, keepout violations, or board-edge violations; no previously connected net was disconnected. Minimum new copper clearance is about 0.1648 mm. All new vias use the project default 0.508 mm diameter / 0.254 mm drill.

U11 VBUS detect is a static sense signal. Its 22.58 mm / four-via route can be shortened during final cleanup. It is not a USB data pair. RF and USB data routes remain incomplete and require impedance/return-path review. High-current supply trees remain incomplete. No manufacturing or electrical sign-off is implied by this checkpoint.

The detailed JSON is a custom geometric audit, not a KiCad DRC report. Return the refilled/saved PCB and full native DRC report for the next batch.
