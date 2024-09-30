import unittest
import logging
import traceback
from runner import Runner  # Предполагаем, что класс Runner находится в файле runner.py

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования INFO
    filename='runner_tests.log',  # Лог будет записываться в этот файл
    filemode='w',  # Режим записи с заменой
    encoding='utf-8',  # Кодировка UTF-8
    format='%(asctime)s | %(levelname)s | %(message)s'  # Формат с временем, уровнем и сообщением
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            # Создаем объект Runner с некорректной скоростью
            runner = Runner(name="Вася", speed=-5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")
            logging.error(traceback.format_exc())  # Логирование traceback

    def test_run(self):
        try:
            # Создаем объект Runner с некорректным типом для name
            runner = Runner(name=2, speed=5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")
            logging.error(traceback.format_exc())  # Логирование traceback

if __name__ == '__main__':
    unittest.main()
