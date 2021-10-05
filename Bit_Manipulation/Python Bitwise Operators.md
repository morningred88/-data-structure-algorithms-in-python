# Python Bitwise Operators 

## Binary compliment  (~)

Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1. You can use this way to get a negative number. 

**Example in python console:**

```
>>> ~128
-129
>>> ~-129
128
```

### Bitwise AND (&)

And operation: Compare the bits, only both is 1, you can get 1, otherwise get 0

**Example in python console:**

```
>>> 12 & 13 
Result: 12
>>> 56 & 88
24
```

**Explanation:**

56 = 32+16 + 8  	binary: 0 1 1 1 0 0 0

88 = 64 +16 + 8     binary: 1 0 1 1 0 0 0

​                                   And:  0 0 1 1 0 0 0 => Decimal: 16 + 8 = 24

## Bitwise OR (|) 

Or operation: Compare the bits, if any one  is 1, you can get 1, otherwise get 0

**Example in python console:**

```
>>> 75 | 21
95
```

**Explanation:**

75 = 64 + 8 + 2 + 1   binary: 1 0 0 1 0 1 1

21 = 16 + 4 + 1         binary:  0 0 1 0 1 0 1

​                                         Or:   1 0 1 1 1 1 1=> Decimal: 64 +16 + 8 + 4 + 2 + 1 = 95

## Bitwise exclusive or (^) 

Xor operation: If the bits are both 1 or 0, then 0; If one of the bits is 1, then 1

**Example in python console:**

```
>>> 75 ^ 21
94
```

**Explanation:**

75 = 64 + 8 + 2 + 1   binary: 1 0 0 1 0 1 1

21 = 16 + 4 + 1         binary:  0 0 1 0 1 0 1

​                                          Or:   1 0 1 1 1 1 0=> Decimal: 64 +16 + 8+ 4 +2 +1 = 94

    ## Bitwise Shift Operators

### Left Shift a << n

Returns a with the bits shifted to the left by n places (and new bits on the right-hand-side are zeros). 

**Example in python console:**

```
>>> 5<<1
10
>>> 5<<2
20
>>> 5<<3
40
```

**Explanation:**

5 = 4 + 1  Binary: 101 

=> 5<<1 =1010   		Decimal 10

=> 5<<2 =10100   	  Decimal 20

=> 5<<3 =101000       Decimal 40

In general, shifting bits to the left corresponds to multiplying the number by a **power of two**, with an exponent equal to the number of places shifted:
$$
a << n = a * 2^n
$$



## Reference:

[#15 Python Tutorial for Beginners | Python BitWise Operators](https://www.youtube.com/watch?v=PyfKCvHALj8)

[Python documentation - Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)

[Bitwise Operators in Python](https://realpython.com/python-bitwise-operators/)

