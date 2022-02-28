import requests

api_param = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=api_param)
# get json data from api source
question_data = response.json()["results"]
