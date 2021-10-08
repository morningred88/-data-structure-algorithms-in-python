def count_bits (x):
  num_bits = 0
  while x:
    num_bits += x & 1
    x >>= 1
  return num_bits

def parity_bits(x):
  result = 0
  while x:
    x ^= x & 1
    x >>= 1

  return result

print(count_bits(100001))
print(parity_bits(1000011))