"""

Task:
You have to create a function to check whether the argument passed is a Pronic Number and return true if it is & false otherwise.

Description:
Pronic Number -A pronic number, oblong number, rectangular number or heteromecic number, is a number which is the product of two consecutive integers, that is, n(n + 1).

The first few Pronic Numbers are - 0, 2, 6, 12, 20, 30, 42...

Explanation:
  0 = 0 × 1   // ∴  0 is a Pronic Number
  2 = 1 × 2   // ∴  2 is a Pronic Number
  6 = 2 × 3   // ∴  6 is a Pronic Number
 12 = 3 × 4   // ∴ 12 is a Pronic Number
 20 = 4 × 5   // ∴ 20 is a Pronic Number
 30 = 5 × 6   // ∴ 30 is a Pronic Number
 42 = 6 × 7   // ∴ 42 is a Pronic Number

Note:
Negative numbers are tested as well.
"""


def is_pronic(n: int) -> bool:
    if n == 0:
        return True
    for i in range(1, n + 1):
        if i * (i + 1) == n:
            return True
    return False


print(is_pronic(42))