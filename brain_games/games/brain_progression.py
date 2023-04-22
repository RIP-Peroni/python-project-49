import random
from typing import Tuple
from brain_games.game_engine import launch_engine


def get_progression(start, diff, elements_count, concealed_index):
    progression = ''
    for i in range(elements_count):
        is_concealed = i == concealed_index
        if is_concealed:
            progression += ' ..'
        else:
            progression += f' {start + diff * i}'
    return progression.strip()


ELEMENTS_COUNT = 10


def start_game() -> None:
    description = 'What number is missing in the progression?'

    def get_question_and_answer() -> Tuple[int, str]:
        start = random.randint(0, 100)
        diff = random.randint(1, 10)
        concealed_index = random.randint(0, ELEMENTS_COUNT - 1)
        question = get_progression(start, diff, ELEMENTS_COUNT, concealed_index)
        correct_answer = str(start + diff * concealed_index)
        return (question, str(correct_answer))

    launch_engine(description, get_question_and_answer)
