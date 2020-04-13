from typing import List
import queue


def numbers_to_string(numbers: List[int]) -> str:
    ret = []
    tmp = []

    length = len(numbers)
    for i in range(length - 1):
        if numbers[i+1] - numbers[i] > 1:
            tmp.append(numbers[i])
            ret.append(tmp)
            tmp = []
            continue
        tmp.append(numbers[i])

    tmp.append(numbers[length-1])
    ret.append(tmp)

    return ', '.join([f'{r[0]}~{r[-1]}' if len(r) > 1 else f'{r[0]}' for r in ret])

