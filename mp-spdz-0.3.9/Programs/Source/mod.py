from Compiler.types import sint, cint
from Compiler.library import print_ln
from Compiler.comparison import LessThanZero
from Compiler.floatingpoint import BITLT

x = sint.get_input_from(0)
gamma = cint(10)

m = gamma.bit_length()
l = 64

r_prime, r_prime_bits = sint.get_edabit(m)
r_double_prime, r_double_prime_bits = sint.get_edabit(l - m)

c = (2**(l - 1) + x + gamma * r_double_prime + r_prime).reveal()

c_prime = c % gamma  

v_bits = BITLT(r_prime_bits, gamma, m)
v = 1 - v_bits.bit_compose()

diff = c_prime - r_prime
u = LessThanZero(diff, m)

x_mod_gamma = c_prime - r_prime + gamma * (v + u)

print_ln("x mod γ = %s", x_mod_gamma.reveal())
