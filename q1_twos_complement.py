def to_8bit_twos_complement(n):
    return format(n & 0xFF, "08b")

def from_8bit_twos_complement(binary):
    value = int(binary, 2)
    return value - 256 if value & 0x80 else value

def signed_add(a, b):
    a_bin = to_8bit_twos_complement(a)
    b_bin = to_8bit_twos_complement(b)
    result = (a + b) & 0xFF
    result_bin = format(result, "08b")
    result_dec = from_8bit_twos_complement(result_bin)
    overflow = not (-128 <= a + b <= 127)

    print(f"Operand 1: {a:>4} -> {a_bin}")
    print(f"Operand 2: {b:>4} -> {b_bin}")
    print(f"Result    : {result_dec:>4} -> {result_bin}")
    print("Overflow  :", "Yes" if overflow else "No")
    print()

print("Q1(a): 25 + 18")
signed_add(25, 18)

print("Q1(b): (-25) + (-18)")
signed_add(-25, -18)
