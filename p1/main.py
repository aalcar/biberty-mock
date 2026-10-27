"""
You have two ropes of integer lengths a and b.
Cut them into pieces that are all the same integer length L.
Any leftover scrap shorter than L is thrown away.
Return the largest L that gives you at least k pieces in total, or 0 if no length works.

Examples

a=10, b=7, k=4 → 3 (3 + 2 = 5 pieces; at L=4 you'd only get 3 pieces)
a=6, b=6, k=2 → 6
a=5, b=5, k=11 → 0

Constraints: 1 ≤ a, b ≤ 10^4, 1 ≤ k ≤ 10^4
"""


def solution(a, b, k) -> int:
    for length in range(max(a, b), 0, -1):
        pieces = a // length + b // length
        if pieces >= k:
            return length
    return 0


print(solution(10, 7, 4))
print(solution(6, 6, 2))
print(solution(5, 5, 11))