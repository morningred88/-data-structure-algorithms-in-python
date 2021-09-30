# Word RAM Model of Computation
RAM - random access memory

## Byte-Oriented Memory Organization

### How do we find data in memory?
Memory is organized in bytes, a collection of sequential 8 bits. Each of the bytes has an index or address that we can use to refer with. So the modern computer is addressed in **bytes**. We start the index with all 0s and end end the index with all 1s. Basically we have a byte at the start, followed by another byte, another byte, ..., all the way to the end. How many bytes do we have? That depends on how many bits we have in the address. If we have 32 bits machines, we use 32 bits of addresses. And more modern 64 bits machine, use 64 bits of addresses. 

### Compiler + run-time system control memory allocation
Where did those numbers go in these bytes of memory, it depends on the compiler and run time system of our machine. It decide where the numbers are stored and allocates them. 

## Machine Words
A **word** is the bit size of memory address, in order to define how big a chunk of memory that CPU can take out of the memory and operate on. The width of machine word is w, in real computer it is 64.

* If the word size is 32 bit, it can indext 2^64 memory addresses, so limits 4 Gb of memory.  
* The word size is 64 bits in most current computer system, which means it can indext 2^64 memory addresses. 
 * Potential address space: 2^64= 1.8 x 10^19 bytes (18 EB - exabytes)
* For backward-compatibility, many CPU support different word sizes
 * Alway a power-of-2 in the number of bytes: 1, 2, 4, 8, ...

## Definition of Word RAM model

* Memory is divided into words of lenght w bits. 
* For size-n input, always assume w >= log n. It sounds weird, the size of our computer hardware depends on the input? We should think the machine grows bigger over time. If we want to process a larger input, we need to buy more RAM to make sure the input n can be put into the word. Eventually, if the n grow really really big, we have to incrase the w to address that RAM. With theory of algorithm, we care about the scalbility for very large n. 
* Costs constant time "1" to do the basic operation on w bits. The basic operation include: addition; substraction; bitwise AND, OR, NOT; shift left or right
The machine is designed to work on the w-bits words in constant time

## Reference:
1. Memory & Data, Video 2: Bits, bytes, words; By Luis Ceze; https://www.youtube.com/watch?v=VP03XyUhZk4
2. The Word RAM Model || @ CMU || Lecture 6c of CS Theory Toolkit; By Ryan O'Donnell; https://www.youtube.com/watch?v=yMcgAzeWDi0

