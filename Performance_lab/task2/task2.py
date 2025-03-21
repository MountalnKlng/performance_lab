def main():
    circle_file = str(input())
    dots_file = str(input())

    with open(circle_file, "r") as cf:
        x_circle, y_circle = map(int, cf.readline().split())
        r = int(cf.readline())

    with open(dots_file, "r") as df:
        while True:
            line = df.readline()
            if line == "":
                break

            x_dot, y_dot = map(int, line.split())
            x = (x_dot - x_circle)
            y = (y_dot - y_circle)

            if x ** 2 + y ** 2 == r ** 2:
                print(0)
            elif x ** 2 + y ** 2 < r ** 2:
                print(1)
            else:
                print(2)


if __name__ == "__main__":
    main()
