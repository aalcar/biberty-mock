"""
A venue stores ticket IDs as positive integers.
Two tickets are a matching pair if their IDs have the same digit sum (e.g. 18 and 36 both sum to 9).
Return the largest possible sum of a matching pair's IDs, or -1 if no pair exists.

Examples

[18, 43, 36, 13, 7] → 54
[10, 12, 19, 14] → -1
[51, 71, 17, 42] → 93

Constraints: 1 ≤ len(ids) ≤ 10^5, 1 ≤ ids[i] ≤ 10^9
"""

def max_pair_sum(ids):
    return None