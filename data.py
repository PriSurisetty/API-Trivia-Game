import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 19
}


response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

data = response.json()
question_data = data["results"]


"""What this module does:
- Imports the requests module in order to request for api data (with url) and provides appropriate parameters
- Saves the data into a variable called 'data'
- Saves the question data into a variable called 'question_data' by tapping into the 'results' key which stores all
of the information

"""