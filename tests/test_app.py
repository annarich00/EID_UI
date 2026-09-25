from eid_ui.app import create_app


def test_dashboard_explains_the_ecological_design_intent():
    client = create_app().test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Ecological Interface Design" in response.data
    assert b"Situation Awareness Timeline" in response.data
    assert b"Appendix B guided scenario" in response.data


def test_scenario_endpoint_returns_all_four_appendix_b_periods():
    client = create_app().test_client()

    response = client.get("/api/scenario")

    assert response.status_code == 200
    assert len(response.json["steps"]) == 4
    assert response.json["steps"][2]["distance_km"] == 5
