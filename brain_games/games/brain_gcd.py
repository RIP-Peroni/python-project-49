import random
from typing import Tuple
from brain_games.game_engine import launch_engine


def calculate_gcd(a: int, b: int) -> int:
    num1 = a
    num2 = b
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 + num2


def start_game() -> None:
    description = 'Find the greatest common divisor of given numbers.'

    def get_question_and_answer() -> Tuple[int, str]:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        question = f"{num1} {num2}"
        correct_answer = str(calculate_gcd(num1, num2))
        return (question, correct_answer)
    launch_engine(description, get_question_and_answer)
