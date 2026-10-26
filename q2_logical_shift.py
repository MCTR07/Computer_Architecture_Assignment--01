def logical_left_shift(binary, positions):
    value = int(binary, 2)
    print("Original:", binary)
    for i in range(positions):
        value = (value << 1) & 0xFF
        print(f"After left shift {i + 1}: {value:08b}")
    return f"{value:08b}"

def logical_right_shift(binary, positions):
    value = int(binary, 2)
    print("Original:", binary)
    for i in range(positions):
        value >>= 1
        print(f"After right shift {i + 1}: {value:08b}")
    return f"{value:08b}"

print("Q2(a): Logical Left Shift")
r1 = logical_left_shift("10110110", 2)
print("Final result:", r1)
print("Decimal:", int(r1, 2))
print()

print("Q2(b): Logical Right Shift")
r2 = logical_right_shift("10101000", 2)
print("Final result:", r2)
print("Decimal:", int(r2, 2))
