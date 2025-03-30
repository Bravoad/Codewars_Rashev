def solution(s: str) -> list:
    lst = []
    if len(s) % 2 != 0:
        s += '_'
    for i in range(0, len(s), 2):
        lst.append(s[i:i + 2])
    return lst
