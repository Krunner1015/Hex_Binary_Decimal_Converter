def menu(): #defines a function that will print the menu of options the user can select from
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")
    print()

def hex_char_decode(digit): #defines a function that will convert a single hexadecimal digit to its value in decimal notation
    if digit == "a":
        return 10
    elif digit == "b":
        return 11
    elif digit == "c":
        return 12
    elif digit == "d":
        return 13
    elif digit == "e":
        return 14
    elif digit == "f":
        return 15
    else:
        return int(digit)

def hex_string_decode(hex): #defines a function that will convert an entire hexadecimal string to its value in decimal notation
    result = 0
    if hex.startswith("0x"):
        hex = hex[2:]
    for i in range (len(hex)):
        digit_value = hex_char_decode(hex[i])
        result += digit_value * (16 ** (len(hex) - 1 - i))
    return result
def binary_string_decode(binary): #defines a function that will convert a binary string to its value in decimal notation
    result = 0
    if binary.startswith("0b"):
        binary = binary[2:]
    for i in range (len(binary)):
        result += int(binary[i]) * (2 ** (len(binary) - 1 - i))
    return result
def binary_to_hex(binary): #defines a function that will convert a string into its value in a hexadecimal string
    decimal = binary_string_decode(binary)
    if decimal == 0:
        return "0"  # Handle the case for zero
    result = ""
    hex_digits = "0123456789ABCDEF"
    while decimal > 0:
        remainder = decimal % 16
        result = hex_digits[remainder] + result
        decimal //= 16
    return result.zfill(4)

while True:
    menu()
    choice = int(input("Please enter an option: "))

    if choice == 1:
        hex = input("Please enter the numeric string to convert: ").lower()
        result = hex_string_decode(hex)
        print(f"Result: {result}")
        print()
    elif choice == 2:
        binary = input("Please enter the numeric string to convert: ").lower()
        result = binary_string_decode(binary)
        print(f"Result: {result}")
        print()
    elif choice == 3:
        binary = input("Please enter the numeric string to convert: ").lower()
        result = binary_to_hex(binary)
        print(f"Result: {result}")
        print()
    elif choice == 4:
        print("Goodbye!")
        quit()
    else:
        print("Invalid option")
        print()