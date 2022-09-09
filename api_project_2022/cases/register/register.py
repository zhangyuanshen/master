import requests

def test_example(base_url):
    assert 200 ==requests.get(base_url).status_code