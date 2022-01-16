import math

UP_TO = 999999


def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1


if __name__ == '__main__':
    with open("PN_list.txt", 'w') as f:
        f.write("2")
        for n in range(3, UP_TO):
            if isPrime(n):
                f.write(',' + str(n))
