from typing import Tuple
from random import randint

Numbers = Tuple[int, int, int]


class GuessResult:
    """이 함수는 수정 하지 않는 것을 권장합니다. (약간의 기능을 추가하는 정도는 괜찮습니다)"""

    def __init__(self, count_of_correct_position: int, count_of_incorrect_position: int):
        self.count_of_correct_position = count_of_correct_position
        self.count_of_incorrect_position = count_of_incorrect_position

    def is_success(self):
        return self.count_of_correct_position == 3

    def __str__(self):
        return (f'A well-positioned number : {self.count_of_correct_position}, '
                f'Wrong-positioned number : {self.count_of_incorrect_position}')


def make_numbers():
    numbers = [randint(1, 9), ]

    while len(numbers) < 3:
        num = randint(0, 9)
        if num in numbers:
            continue
        numbers.append(num)

    return tuple(numbers)


class GameHost:

    def __init__(self):
        self.answer_numbers = make_numbers()

    def guess(self, guess_numbers: Numbers) -> GuessResult:
        count_of_correct_pos = 0
        count_of_incorrect_pos = 0

        if len(guess_numbers) > 3:
            print("Please check your input numbers.")
            return

        for i in range(len(guess_numbers)):
            if guess_numbers[i] == self.answer_numbers[i]:
                count_of_correct_pos += 1
                continue
            if guess_numbers[i] in self.answer_numbers:
                count_of_incorrect_pos += 1

        return GuessResult(count_of_correct_pos, count_of_incorrect_pos)


class GameGuest:

    def __init__(self):
        self.guess_number = make_numbers()

    def guess(self) -> Numbers:
        return self.guess_number

    def feedback(self, numbers: Numbers, result: GuessResult):
        # implement game logic
        pass
