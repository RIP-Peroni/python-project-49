import random
from typing import Tuple
from brain_games.game_engine import launch_engine


def is_even(number: int) -> bool:
    return number % 2 == 0


def start_game() -> None:
    description = 'Answer "yes" if the number is even, otherwise answer "no".'

    def get_question_and_answer() -> Tuple[int, str]:
        question = random.randint(1, 100)
        correct_answer = 'yes' if is_even(question) else 'no'
        return (question, correct_answer)
    launch_engine(description, get_question_and_answer)
