import sys


def main():
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    else:
        n, m = map(int, input().split())

    current_step = 1

    while True:
        print(current_step, end="")
        current_step += m - 1
        while current_step > n:
            current_step -= n
        if current_step == 1:
            break


if __name__ == "__main__":
    main()
