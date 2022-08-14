from random import choice, shuffle
import psycopg2
from psycopg2 import Error, sql


class HandlerQuestions:
    def __init__(self, topic: int):
        self.__topic = topic
        self.__records = self.__connect()
        self.__keys = list(self.__records.keys())
        self.__len_records = len(self.__keys)

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
            print(records[0])
            print(records[0]['wrong_answers'])
            return records
        except (Exception, Error) as e:
            print('Error! ', e)

    def __shuffle_answers(self, right_answer: str, wrong_answers: list) -> list:
        wrong_answers.append(right_answer)
        shuffle(wrong_answers)
        return wrong_answers

    def get_question(self) -> dict:
        number_of_question = choice(self.__keys)
        record = self.__records[number_of_question]
        del self.__records[number_of_question]
        record['wrong_answers'] = self.__shuffle_answers(record['right_answer'], record['wrong_answers'])
        return record
