from test_conf import client


def test_sample_ticket_success():
    json_request = {
        "first_name": "erfan",
        "last_name": "ehsany",
        "gender": "helicopter",
        "date": "2077-09-21",
    }
    response = client.post("/sample/ticket", json=json_request)
    assert response.status_code == 200


def test_sample_ticket_unsuccess():
    json_request = {}
    response = client.post("/sample/ticket", json=json_request)
    assert response.status_code == 422
