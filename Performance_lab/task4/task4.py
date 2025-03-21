def main():
    file = str(input())
    numbers = []

    with open(file, "r") as df:
        while True:
            line = df.readline()
            if line == "":
                break

            numbers.append(int(line))

    num_mean = round(sum(numbers)/len(numbers))

    steps = 0
    for n in numbers:
        steps += abs(num_mean - n)

    print(steps)


if __name__ == "__main__":
    main()