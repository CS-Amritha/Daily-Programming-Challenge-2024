import math
def count_divisors(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                cnt += 1
            else:  
                cnt += 2
    return cnt
def main():
    print("Total distinct divisors of 100 are:", count_divisors(100))
if __name__ == "__main__":
    main()
