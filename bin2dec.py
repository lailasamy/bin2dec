import math

def bin2dec(binary_str):
    # Check for invalid characters
    if not all(char in '01' for char in binary_str):
        return "Invalid input. Please enter a binary number."
    
    decimal_value = 0
    length = len(binary_str)
    
    # Iterate through each character in the binary string
    for i, char in enumerate(binary_str):
        if char == '1':
            # Calculate the position's power of 2
            power = length - i - 1
            decimal_value += 2 ** power
    
    return decimal_value

def main():
    binary_str = input("Enter a binary number (up to 8 digits): ")
    if len(binary_str) > 8:
        print("Input exceeds 8 binary digits.")
    else:
        print(f"Decimal value: {bin2dec(binary_str)}")

if __name__ == "__main__":
    main()
