def ari_prog(start, stop, step):
    while start < stop:
        yield start

        start += step


def geo_prog(start, stop, multiplier):
    while start < stop:
        yield start

        start *= multiplier


def fibonacci_prog(start, stop):
    while start < stop:
        flag = 1
        second = 1
        first = 0
        counter = 1
        yielded = False

        if start == 1 or start == -1:
            yield 1
            yielded = True
            start += 1
        if -2 < start < 2 and not yielded:
            yield start
            yielded = True
            start += 1
        if start < 0 and not yielded:
            if start % 2 == 0:
                flag = -1
            start *= -1
        while counter < start:
            next = first + second
            first = second
            second = next
            counter += 1
        yield next*flag
        start += 1


def factorial_prog(start, stop):
    while start < stop:
        yield factorial(start)

        start += 1


def factorial(value):
    return 1 if value < 2 else value * factorial(value - 1)


if __name__ == '__main__':  # pragma: no cover
    for i in factorial_prog(1, 10):
        print(i)
