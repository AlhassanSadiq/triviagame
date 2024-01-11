# api_handler.py
import requests
import html

def get_trivia_questions(amount):
    base_url = "https://opentdb.com/api.php"
    params = {
        'amount': amount,
        'type': 'multiple'  # Multiple-choice questions
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        trivia_data = response.json()
        return trivia_data['results']
    else:
        print(f"Error fetching trivia questions. Status Code: {response.status_code}")
        return None
