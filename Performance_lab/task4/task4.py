import sys


def main():
    if len(sys.argv) == 2:
        file = str(sys.argv[1])
    else:
        file = str(input())
    numbers = []

    with open(file, "r") as df:
        while True:
            line = df.readline()
            if line == "":
                break

            numbers.append(int(line))

    numbers = sorted(numbers)

    if len(numbers) %2 == 0:
        num_median = (numbers[len(numbers)//2] + numbers[len(numbers)//2 - 1]) // 2
    else:
        num_median = numbers[len(numbers) // 2]

    steps = 0
    for n in numbers:
        steps += abs(num_median - n)

    print(steps)


if __name__ == "__main__":
    main()