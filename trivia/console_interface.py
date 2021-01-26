class ConsoleInterface:
  def __init__(self, quiz):
    self.__quiz = quiz

  def run(self):
    while self.__quiz.has_next_question():
      question = self.__quiz.get_next_question()
      answer = input(question + ' (True/False): ')
      correct = self.__quiz.check_answer(answer)

      if correct:
        print('Your answer is correct!\n\n')
      else:
        print('Your answer is wrong!\n\n')

    print('Your score is: ' + str(self.__quiz.get_score())) 