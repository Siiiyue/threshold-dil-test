# this tests secure 2 party summation

x = sint.get_input_from(0)
y = sint.get_input_from(1)

z = x + y

print_ln("%s", z.reveal())
