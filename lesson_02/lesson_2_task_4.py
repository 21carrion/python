def fizz_buzz(n):
    for i in range(1, n + 1):
        out = ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "")
        print(out or i)


fizz_buzz(15)
