import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get("https://api.github.com/zen")
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get("https://api.github.com/users/defunkt")
    body = r.json()
    header = r.headers
    # print(f"Response Body is {r.json()}")
    # print(f"Response Status code is {r.status_code}")
    # print(f"Response Headers are {r.headers}")
    assert r.status_code == 200
    assert body['name'] == 'Chris Wanstrath'
    assert header['Server'] == 'GitHub.com'


@pytest.mark.http
def test_status_code_request():
    r = requests.get("https://api.github.com/users/dimitri_pasmore")
    assert r.status_code == 404
