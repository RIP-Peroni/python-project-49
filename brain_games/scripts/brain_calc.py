#!/usr/bin/env python3

import random
from typing import Tuple
from brain_games.game_engine import launch_engine


def start_game() -> None:
    description = 'What is the result of the expression?'

    def get_question_and_answer() -> Tuple[int, str]:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        math_sign = random.choice("+-*")
        question = f"{num1} {math_sign} {num2}"
        operators = {
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
        }
        correct_answer = operators[math_sign](num1, num2)
        return (question, str(correct_answer))

    launch_engine(description, get_question_and_answer)


def main():
    start_game()


if __name__ == '__main__':
    main()
