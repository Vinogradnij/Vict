from random import choice, shuffle
import psycopg2
from psycopg2 import Error, sql


class HandlerQuestions:
    def __init__(self, topic: int):
        self.__topic = topic
        self.__records = self.__connect()
        self.__keys = list(self.__records.keys())
        self.__points = 0
        self.__right_answer = ''

    def __connect(self) -> dict:
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="BackToTheFuture",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="bd_quiz")
            cursor = connection.cursor()
            cursor.execute(sql.SQL("select * from questions where topic=%s"), [self.__topic])
            records = {}
            for record in cursor:
                records[record[0]] = {'question': record[2], 'right_answer': record[3], 'wrong_answers': list(record[4:])}
            connection.close()
            return records
        except (Exception, Error) as e:
            print('Error! ', e)

    def __shuffle_answers(self, right_answer: str, wrong_answers: list) -> list:
        result = wrong_answers.copy()
        result.append(right_answer)
        shuffle(result)
        return result

    @property
    def points(self):
        return self.__points

    def get_question(self) -> dict:
        if self.__keys:
            number_of_question = choice(self.__keys)
            record = self.__records.pop(number_of_question)
            self.__keys.remove(number_of_question)
            self.__right_answer = record['right_answer']
            record['wrong_answers'] = self.__shuffle_answers(record['right_answer'], record['wrong_answers'])
            return record
        else:
            return {}

    def check_answer(self, user_answer: str) -> None:
        if user_answer.lower() == self.__right_answer.lower():
            self.__points += 1
