import botocore.configprovider
import requests
import os

# set env varible
os.environ['SERVER_URL'] = "localhost"
os.environ['SERVER_PORT'] = "5001"


def test_get(url_to_test):
    response = requests.get(url_to_test)
    actual = response.text
    expected = open("car-list.txt", "r").read()
    assert actual == expected


def test_post(url_to_test):
    response = requests.post(url_to_test)
    actual = response.text
    expected = "saved new car"
    assert actual == expected


url = os.getenv("SERVER_URL")
port = os.getenv("SERVER_PORT")
test_get("http://" + url + ":" + port + "/cars")
test_post("http://" + url + ":" + port + "/cars")
