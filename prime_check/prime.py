import math
def prime_check(n):
    if n >= 2:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
            else:
                continue
        else:
            return True
    else:
        return False

print(prime_check(6))

if __name__ == '__main__':
    for i in range(10):
        print(prime_check(i) , i)