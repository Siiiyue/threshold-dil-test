x = sint.get_input_from(0)
y = sint.get_input_from(1)

z = x + y

z_plain = z.reveal()

# print_ln("type of z_plain: %s", type(z_plain))

def append_to_file(filepath, data):
    with open(filepath, "r+") as file:

        file.seek(0, 2)
        

        if file.tell() > 0:
            file.seek(file.tell() - 1)
            last_char = file.read(1)
        
        file.write(str(data))

append_to_file("/home/spdz/Desktop/mp-spdz-0.3.9/Player-Data/Input-P0-0", "%s", z_plain)

a = sint.get_input_from(0)
b = sint.get_input_from(1)

c = a + b

print_ln("res = %s", c.reveal())
