from eid_ui.scenario import SCENARIO_STEPS


def test_appendix_b_scenario_has_four_time_periods_in_order():
    assert [step.label for step in SCENARIO_STEPS] == [
        "Day 1 · 0001–1200",
        "Day 1 · 1201–2400",
        "Day 2 · 0001–1200",
        "Day 2 · 1201–2400",
    ]


def test_second_period_offers_the_documented_red_1_maneuver_option():
    step = SCENARIO_STEPS[1]

    assert "Most Time at Min" in step.operator_task
    assert step.distance_km == 50


def test_third_period_represents_loss_of_contact_and_close_approach():
    step = SCENARIO_STEPS[2]

    assert step.distance_km == 5
    assert "outage" in step.blue_status.lower()
