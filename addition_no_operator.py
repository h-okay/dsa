def add(num1, num2):
    while num2 != 0:
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1
    return num1


if __name__ == "__main__":
    print("156 + 52 =", add(156, 52))

    # 10011100 & 00110100 = 00010100 -> 10100 -> 20
    # 10011100 ^ 00110100 = 10101000 -> 10101000 -> 168
    # 00010100 << 1 = 00101000 -> 40

    # 10101000 & 00101000 = 00101000 -> 40
    # 10101000 ^ 00101000 = 10000000 -> 128
    # 00101000 << 1 = 01010000 -> 80

    # 10000000 & 01010000 = 00000000 -> 0
    # 10000000 ^ 01010000 = 11010000 -> 208
    # 00000000 << 1 = 00000000 -> 0