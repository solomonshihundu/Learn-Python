flag = 4
print(bin(flag))

mask = 8
print(bin(mask))

flag &= ~mask
print(bin(flag))

flag |= mask
print(bin(flag))

flag2 = 16
print(bin(flag2))

mask2 = 8
print(bin(mask2))

flag2 ^= mask2
print(bin(flag2))
