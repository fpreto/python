
#
# Calculate e ^ x using power series
#
# e ^ x = sum from 0 to INF of (x ^ n / n!) -> 1 + x + x^2/2! + x^3/3! + x^4/4! + ...
#

EPSILON = 0.0000000001

def exp(x):
    cur_sum = 1.0
    cur_pow = 1.0
    cur_fat = 1.0
    fat_counter = 0.0
    delta = EPSILON + 1

    while delta > EPSILON:
        prev_sum = cur_sum
        cur_pow *= x
        fat_counter += 1.0
        cur_fat *= fat_counter
        cur_sum += cur_pow / cur_fat
        delta = abs(cur_sum - prev_sum)
    
    return cur_sum



