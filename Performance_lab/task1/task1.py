def main():
    n = int(input())
    m = int(input())

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
