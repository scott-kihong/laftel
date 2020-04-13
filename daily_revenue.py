from datetime import date
from datetime import datetime
from datetime import timedelta
from typing import List
from typing import Optional
from typing import Tuple

Period = Tuple[datetime, datetime]


def daily_revenue(price: int, period: Period, refund_date: Optional[datetime]) \
        -> List[Tuple[date, int]]:
    # Include typing
    total_days: int = (period[1].date() - period[0].date()).days + 1
    day_price: int = price // total_days
    last_price = price - (day_price * (total_days - 1))

    date_from: date = period[0].date()
    date_to: date = period[1].date()

    if refund_date:
        date_refund: date = refund_date.date()
        if date_from == date_refund:
            return []
        elif date_to >= date_refund:
            date_to = date_refund - timedelta(days=1)

    result = [
        (str(date_from + timedelta(days=i)), day_price)
        for i in range((date_to - date_from).days + 1)
    ]

    day_count: int = len(result)

    if total_days == day_count:
        result[-1] = (str(result[-1][0]), last_price)
    if refund_date:
        result.append((str(date_refund), -day_count * day_price))

    return result
