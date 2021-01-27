from quiz import Quiz
from console_interface import ConsoleInterface
from client import Client

questions = Client().get_questions()
quiz = Quiz(questions)
ConsoleInterface(quiz).run()
