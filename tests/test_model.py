from eid_ui.model import MissionState, plan_for_goal


def test_separation_plan_increases_spacecraft_distance_and_consumes_fuel():
    state = MissionState()

    next_state = state.apply(plan_for_goal("separate"))

    assert next_state.distance_km > state.distance_km
    assert next_state.fuel_percent < state.fuel_percent
    assert next_state.vulnerability_percent < state.vulnerability_percent


def test_inspection_plan_reduces_distance_but_never_allows_negative_fuel():
    state = MissionState(distance_km=48, fuel_percent=4)

    next_state = state.apply(plan_for_goal("inspect"))

    assert next_state.distance_km < state.distance_km
    assert next_state.fuel_percent == 0


def test_unknown_goal_is_rejected():
    import pytest

    with pytest.raises(ValueError, match="Unknown goal"):
        plan_for_goal("teleport")
