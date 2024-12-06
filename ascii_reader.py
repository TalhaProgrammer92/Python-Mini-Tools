def convert(statement: str, binary_reading: bool = False) -> str:
    result = ""
    if binary_reading:
        statement = statement.split(" ")

    if binary_reading:
        for binary in statement:
            value = 0
            for i, bit in enumerate(binary[::-1]):
                value += int(bit) * 2 ** i
            result += chr(value)
    else:
        for char in statement:
            binary = ""
            value = ord(char)

            while value > 0:
                binary = str(value % 2) + binary
                value = int(value / 2)

            for count in range(8 - len(binary)):
                binary = "0" + binary

            result += binary + " "

    return result

if __name__ == '__main__':
    message = """; Program to print hello world
.MODEL SMALL
.STACK 100H
.DATA
    MSG DB 'Hello World$'
.CODE
    MAIN PROC FAR
        MOV AX, @DATA
        MOV DS, AX
        MOV AH, 09H
        LEA DX, MSG
        INT 21H
        MOV AH, 4CH
        INT 21H
    MAIN ENDP
END MAIN"""
    encoded = convert(message)
    decoded = convert(encoded, True)
    print(encoded, decoded, sep='\n')