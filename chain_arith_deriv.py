from math import log, sqrt
import time
from sympy.ntheory import factorint

def is_prime(num):
    """
  This function checks if a number is prime.
  """
    if num == 2:
        return True
    if num % 2 == 0 or num < 2:
        return False

    divisor_range = int(sqrt(num)) + 1

    for i in xrange(3, divisor_range, 2):
        if num % i == 0:
            return False
    return True

def get_factors(n):
    try:
        result = set(reduce(list.__add__,
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
    except TypeError:
        result = set([])

    return result

def factorize(num):
    # factor_list = factorint(num).items()

    factors = [x for x in get_factors(num) if is_prime(x)]

    factor_list = []
    for factor in factors:
        max_i = int(float(log(num)) / log(factor))
        max_power = max([i for i in xrange(max_i + 1) if num % factor ** i == 0])
        factor_list.append((factor, max_power))

    return factor_list


def chain_arith_deriv(start, k):
    temp = start
    result_list = [temp]

    if len(factorize(temp)) == 0:
        return str(start) + " is a prime number"

    for x in range(k - 1):
        print(temp)
        temp_fac = factorize(temp)

        if len(temp_fac) > 0:
            temp = int(round(sum([float(k) / p for p, k in temp_fac]) * temp))
        else:
            temp = 1
        if temp != 0:
            result_list.append(temp)

    print(result_list)
    return result_list

print(chain_arith_deriv(23477470, 5) == [23477470, 17179939, 5168254, 3804091])
# print(chain_arith_deriv(78218061, 9) == [78218061, 26103503, 1, 1, 1, 1, 1, 1, 1])
# print(chain_arith_deriv(76180898, 3) == [76180898, 38090451, 18661630])
# print(chain_arith_deriv(2524816, 12) == [2524816, 5410432, 19067840, 62754048, 322783488, 1645595136, 9050787072, 48270885120, 252674118144, 1461900932352, 7579328861952, 37896644316672])
# print(chain_arith_deriv(39603847, 17) == [39603847, 2084432, 4527120, 11820064, 29609104, 65191696, 132768400, 318644560, 725530192, 1457842752, 5917155840, 33727857408, 173457600768, 884423363328, 4446020406528, 22230102039552, 143528692967424])
# print(chain_arith_deriv(40065916, 12) == [40065916, 44002632, 82987876, 83220476, 83220480, 571401216, 3632643072, 21841920000, 192485376000, 1661899161600, 15101925949440, 137793779417088])


num = 53347720
# print(factorize((76180898)))
print(chain_arith_deriv(num, 5))
# print(factorint(num).items())