"""Small, transparent mission-planning model used by the EID prototype."""
from dataclasses import dataclass


@dataclass(frozen=True)
class ManeuverPlan:
    label: str
    distance_delta_km: int
    fuel_cost_percent: int
    coverage_delta_percent: int
    vulnerability_delta_percent: int


PLANS = {
    "separate": ManeuverPlan("Radial separation burn", 30, 8, -4, -35),
    "inspect": ManeuverPlan("Close approach / inspection", -25, 12, -8, 20),
    "coverage": ManeuverPlan("Coverage-preserving adjustment", 5, 5, 10, -8),
}


@dataclass(frozen=True)
class MissionState:
    distance_km: int = 48
    fuel_percent: int = 72
    coverage_percent: int = 84
    vulnerability_percent: int = 65

    def apply(self, plan: ManeuverPlan) -> "MissionState":
        return MissionState(
            distance_km=max(0, self.distance_km + plan.distance_delta_km),
            fuel_percent=max(0, self.fuel_percent - plan.fuel_cost_percent),
            coverage_percent=max(0, min(100, self.coverage_percent + plan.coverage_delta_percent)),
            vulnerability_percent=max(
                0, min(100, self.vulnerability_percent + plan.vulnerability_delta_percent)
            ),
        )


def plan_for_goal(goal: str) -> ManeuverPlan:
    try:
        return PLANS[goal]
    except KeyError as error:
        raise ValueError(f"Unknown goal: {goal}") from error
