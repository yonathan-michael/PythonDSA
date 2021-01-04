from Stack.stack import Stack


def convert_int_to_bin(dec_num):
    s = Stack()

    dec_num = dec_num

    while dec_num >= 1:
        bit = dec_num % 2
        dec_num = dec_num // 2
        s.push(bit)

    bit_string = ""

    while not s.is_empty():
        bit_string += str(s.pop())

    return bit_string


input_number = 242
print(convert_int_to_bin(input_number))
