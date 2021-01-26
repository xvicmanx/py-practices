import requests
from quiz import Quiz
from console_interface import ConsoleInterface


params = {
  'amount': 10,
  'category': 27,
  'difficulty': 'easy',
  'type': 'boolean',
}

response = requests.get('https://opentdb.com/api.php', params = params)
response.raise_for_status()
data = response.json()
quiz = Quiz(data['results'])
ConsoleInterface(quiz).run()
