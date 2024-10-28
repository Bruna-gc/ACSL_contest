
# index letter
# print((ord("B") % 65) + 1)

list_letters = [chr((ord("A") + i)) for i in range(26)]
print(list_letters)

# set_letters = enumerate(list_letters, start=1)
# print(set_letters)

# swap letters chr(ord(previous_num) + (numerical_value % 26))
print(chr(ord("J") + (1 % 26)))



