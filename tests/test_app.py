from eid_ui.app import create_app


def test_dashboard_explains_the_ecological_design_intent():
    client = create_app().test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Ecological Interface Design" in response.data
    assert b"Situation Awareness Timeline" in response.data
