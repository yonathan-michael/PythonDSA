from Stack.stack import Stack


def reverse_String_Stack(input_string):
    s = Stack()
    reversed_string = ""
    for i in range(len(input_string)):
        s.push(input_string[i])
    while not s.is_empty():
        reversed_string += s.pop()
    return reversed_string


string_1 = "olleJ"
print(reverse_String_Stack(string_1))
