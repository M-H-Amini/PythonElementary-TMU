class Number:
    def __init__(self, n):
        self.n = str(n)

    def bin2dec(self):
        digits = [int(i) for i in list(self.n)]
        s = 0
        for i in range(len(digits)):
            s += digits[i] * 2**(len(digits) - 1 - i)
        print('In decimal: ', s)
        return s

    def dec2bin(self):
        n = int(self.n)
        digits = []
        while n > 1:
            digits.append(n%2)
            n = n // 2
        digits.append(n)
        digits = digits[::-1]
        digits = ''.join([str(i) for i in digits])
        print(digits)
        return int(digits)

def isPrime(n):
    for i in range(2, int(n/2)):
        if not (n%i):
            return False
    return True

if __name__=='__main__':
    print(isPrime(10))
    print(isPrime(111))
    print(isPrime(125))
    print(isPrime(119))
    print(isPrime(997))