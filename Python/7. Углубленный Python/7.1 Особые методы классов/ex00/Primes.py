class Primes:
    def __init__(self, end) -> None:
        self._end = end
        self._current = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self._is_prime(self._current) == False:
            self._current += 1
        if (self._current >= self._end):
            raise StopIteration
        self._current += 1
        return self._current - 1

    @staticmethod
    def _is_prime(num):
        if num == 1:
            return True
        if num == 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

#Main
prime_nums = Primes(50)

for i_elem in prime_nums:

    print(i_elem, end=' ')