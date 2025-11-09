import math
def find_prime(n):
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



if __name__ == '__main__':
    for i in range(10):
        print(find_prime(i) , i)