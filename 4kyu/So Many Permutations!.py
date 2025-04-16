from itertools import permutations as permut


def permutations(s: str) -> list[str]:
    perms = permut(s)
    unique_perms = {''.join(p) for p in perms}
    return list(unique_perms)
