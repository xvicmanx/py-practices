class Quiz:
  def __init__(self, questions):
    self.__questions = questions
    self.__index = 0
    self.__score = 0

  def has_next_question(self):
    return self.__index < len(self.__questions) - 1
  
  def get_next_question(self):
    question = self.__questions[self.__index]
    self.__index += 1
    return question['question']
  
  def check_answer(self, answer):
    self.__score += 1
    return self.__questions[self.__index]['correct_answer'] == answer

  def get_score(self):
    return self.__score
