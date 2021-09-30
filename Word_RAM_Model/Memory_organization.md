# Word RAM Model

## Byte-Oriented Memory Organization

### How do we find data in memory?
Memory is organized in bytes. Each of the bytes has an index or address that we can use to refer with. We start the index with all 0s and end end the index with all 1s. Basically we have a byte at the start, followed by another byte, another byte, ..., all the way to the end. How many bytes do we have? That depends on how many bits we have in the address. If we have 32 bits machines, we use 32 bits of addresses. And more modern 64 bits machine, use 64 bits of addresses. 

### Compiler + run-time system control memory allocation
Where did those numbers go in these bytes of memory, it depends on the compiler and run time system of our machine. It decide where the numbers are stored and allocates them. 
