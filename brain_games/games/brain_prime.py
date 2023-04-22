import random
from typing import Tuple
from brain_games.game_engine import launch_engine


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for j in range(2, int(num / 2) + 1):
        if num % j == 0:
            return False
    return True


def start_game() -> None:
    descript = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def get_question_and_answer() -> Tuple[int, str]:
        question = random.randint(1, 100)
        correct_answer = 'yes' if is_prime(question) else 'no'
        return (question, correct_answer)
    launch_engine(descript, get_question_and_answer)
