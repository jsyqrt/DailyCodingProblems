def WaysToGo(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return WaysToGo(rows - 1, columns) + WaysToGo(rows, columns - 1)

def main():
    a = (1, 1)
    b = (2, 2)
    c = (3, 3)
    d = (4, 4)
    e = (5, 5)

    x = (a, b, c, d, e)

    for i in x:
        print i, WaysToGo(i[0], i[1])


if __name__ == "__main__":
    main()
