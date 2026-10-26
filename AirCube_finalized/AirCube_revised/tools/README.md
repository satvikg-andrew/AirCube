# Read-only review scripts

Use Python 3 with numpy, scipy and shapely for the copper mesh, and shapely for the USB reference audit. The impedance screen uses the standard library. Run scripts from any directory; they locate Base/ relative to their own path.

- `python tools/usb_reference_audit.py`: filled-ground overlap check, with the own-net pad/via exclusions visible in the script.
- `python tools/dc_power_estimate.py .03`: positive-path copper mesh.
- `python tools/dc_power_estimate.py .06 --ground`: ground-path estimates.
- `python tools/impedance_screen.py`: preliminary calculation described in docs/IMPEDANCE.md.

These do not modify the KiCad source. The native DRC/ERC reports were produced with KiCad 10.0.7. Use native KiCad to refill and check any future edits, then regenerate manufacturing outputs; analysis scripts are not substitutes for DRC or factory review.
