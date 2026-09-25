"""The four-period operator walk-through from Appendix B of the thesis."""
from dataclasses import dataclass


@dataclass(frozen=True)
class ScenarioStep:
    label: str
    blue_status: str
    red_status: str
    operator_task: str
    intelligence: str
    distance_km: int
    fuel_percent: int
    coverage_percent: int
    vulnerability_percent: int


SCENARIO_STEPS = (
    ScenarioStep(
        "Day 1 · 0001–1200",
        "One of two ground stations is offline. A payload issue requires attention at 0500.",
        "Red 1 executes a maneuver projected to bring it within 50 km of Blue 1.",
        "Review the pending payload issue and monitor Red 1's projected approach.",
        "Proximity maneuver detected; intent remains uncertain.",
        50, 72, 84, 45,
    ),
    ScenarioStep(
        "Day 1 · 1201–2400",
        "Payload issue resolved; both ground stations are fully operational.",
        "Red 1 is within 50 km and remains at least 50 km away for half of its orbital period.",
        "Review intelligence, compare four Red 1 options, then select “Most Time at Min” to plot 15 km minimum separation.",
        "Red 1 capability estimate supports four candidate approaches to Blue 1's vulnerability zone.",
        50, 72, 84, 55,
    ),
    ScenarioStep(
        "Day 2 · 0001–1200",
        "Complete operations-center outage: situation awareness and contact are lost. Estimated recovery: 12 hours.",
        "Red 1 maneuvers to within 5 km of Blue 1.",
        "Assess the outage and the loss of contact; prepare for recovery with an uncertain close approach.",
        "No current Blue 1 telemetry during the outage.",
        5, 72, 84, 95,
    ),
    ScenarioStep(
        "Day 2 · 1201–2400",
        "Operations center is fully restored. Red 1 is observed within 5 km.",
        "Red 1 takes no further action.",
        "Update Red 1 fuel estimates and compare emergency maneuvers that remove Blue 1 from observation distance.",
        "Emergency decision: Red 1 is close; its updated fuel estimate constrains likely future action.",
        5, 72, 84, 95,
    ),
)
