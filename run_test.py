from datetime import datetime
from time import sleep

from coupon_codes import create_coupon
from daily_revenue import daily_revenue
from guess_numbers import GameGuest
from guess_numbers import GameHost
from numbers_to_string import numbers_to_string


def run():
    """테스트를 위한 함수입니다.
    이 파일은 작성하지 않으셔도 평가에 영향을 미치지 않습니다.
    """
    print("==============number_to_string==============")
    print(numbers_to_string([4, 5, 6, 9, 11, 12, 13]))
    print(numbers_to_string([-5, -4, -3, -1, 0, 1, 4, 5, 6, 9, 11]))

    print("================coupon_codes================")
    print(create_coupon({'test: test'}))

    print("===============daily_revenue================")
    start_date = datetime(2019, 9, 1, 17, 10, 21)
    end_date = datetime(2019, 10, 1, 8, 35, 48)
    refund_date = datetime(2019, 9, 4, 12, 13, 20)
    print(daily_revenue(9900, (start_date, end_date), refund_date))

    print("===============guess_numbers================")
    # feedback에 힌트를 기반을 번호를 맞추는 로직 구현 안됨
    # 따라서 현재 버전은 무한루프 상태에 빠짐
    game_host = GameHost()
    game_guest = GameGuest()

    while True:
        guess_result = game_host.guess(game_guest.guess())
        print(guess_result)
        if guess_result.is_success():
            break
        game_guest.feedback(game_guest.guess_number, guess_result)
        sleep(1)


if __name__ == '__main__':
    run()
