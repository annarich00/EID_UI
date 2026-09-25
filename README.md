# Space Defense EID UI

A minimal interactive reconstruction of the Ecological Interface Design (EID) concepts in Chapter IV of *Specifying Space Defense Operator Interfaces Through the Application of Cognitive Systems Engineering and Prototyping* (Justin E. Oryschak, AFIT-ENV-MS-20-D-070, 2020).

It demonstrates goal-based maneuver selection, directly visible mission constraints, engagement/vulnerability zones, and a situation-awareness timeline. The figures and narrative in the thesis informed the interface; the numerical values and the simple planning model are illustrative and are **not** an orbital simulation.

## Run

```bash
uv run -- flask --app eid_ui.app:create_app run
```

Open <http://127.0.0.1:5000>. Run tests with `uv run pytest`.
