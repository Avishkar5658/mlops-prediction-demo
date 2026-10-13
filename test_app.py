from app import app

def test_home_page_loads():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"PredictLab" in response.data

def test_prediction_is_displayed():
    response = app.test_client().post("/", data={"hours": "5", "practice": "3"})
    assert response.status_code == 200
    assert b"Sample model prediction" in response.data
