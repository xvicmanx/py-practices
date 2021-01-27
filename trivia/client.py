import requests

API_BASE = 'https://opentdb.com/api.php'

class Client:  
  def get_questions(self):
    params = {
      'amount': 10,
      'category': 27,
      'difficulty': 'easy',
      'type': 'boolean',
    }

    response = requests.get(API_BASE, params = params)
    response.raise_for_status()
    data = response.json()
    return data['results']