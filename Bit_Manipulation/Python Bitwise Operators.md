# Python Bitwise Operators 

## Binary compliment ~x

Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1. You can use this way to get a negative number. 

**Example in python console:**

```
>>> ~128
-129
>>> ~-129
128
```

### Binary AND - &

And operation: Compare the bits, only both is 1, you can get 1, otherwise get 0

**Example in python console:**

```
>>> 12 & 13 
Result: 12
>>> 56 & 88
24
```

**Explanation**

12: 00001100

13: 00001101

& : 00001100,  it is $12_{10}$

## Reference:

[#15 Python Tutorial for Beginners | Python BitWise Operators](https://www.youtube.com/watch?v=PyfKCvHALj8)

[Python Bitwise Operators Example](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)

[Python documentation - Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)

