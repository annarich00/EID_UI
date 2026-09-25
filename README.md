# Space Defense EID UI

A minimal interactive reconstruction of the Ecological Interface Design (EID) concepts in Chapter IV of *Specifying Space Defense Operator Interfaces Through the Application of Cognitive Systems Engineering and Prototyping* (Justin E. Oryschak, AFIT-ENV-MS-20-D-070, 2020).

It demonstrates goal-based maneuver selection, directly visible mission constraints, engagement/vulnerability zones, and a situation-awareness timeline. The figures and narrative in the thesis informed the interface; the numerical values and the simple planning model are illustrative and are **not** an orbital simulation.

## Run

```bash
uv run -- flask --app eid_ui.app:create_app run
```

Open <http://127.0.0.1:5000>. Run tests with `uv run pytest`.

## Appendix B scenario

The landing page now starts a four-period, guided Blue 1 / Red 1 walkthrough from Appendix B and Figure 53:

1. Day 1 0001–1200: ground-station outage, pending payload issue, and Red 1's projected 50 km approach.
2. Day 1 1201–2400: restored Blue 1 status; select the documented **Most Time at Min** Red 1 candidate (15 km minimum separation).
3. Day 2 0001–1200: 12-hour operations-center outage while Red 1 moves within 5 km.
4. Day 2 1201–2400: restored operations; assess emergency maneuvers after updating Red 1 fuel estimates.

The scenario text and distances are sourced from Appendix B; the visual meter values and maneuver model remain illustrative.
