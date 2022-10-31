from sys import argv


def wages():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"wages: {time,rate, bonus}")
    except ValueError:
        print("Вводимые значения должны быть числами!")

wages()