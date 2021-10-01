# Binomial coefficient

## What is n Choose k Formula?

It is also known as a binomial coefficient. "n choose k formula" is used to find the number of ways selecting k things out of n things. Sometimes we prefer selecting but we do not care about ordering them. 

For example, you are packing luggage for a trip, and you want to carry 5 dresses out of 10 new dresses you have. This can be done in various ways, it doesn't matter in which order you have chosen them but it all matters what dresses you have chosen. Let us learn the n choose k formula along with a few solved examples.

## Calculation of n choose k formula

"n choose k" is denoted by C (n, k)  or  $\binom{n}{k}$.


The n choose k formula is also known as combinations formula (as we call a way of choosing things to be a combination). This formula involves factorials.

The n Choose k Formula is:

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

## Prove the formula using a simple Examples 

Find the number of ways of forming a team of 2 members out of 4 members.

The available combination is:

(1, 2) (1, 3) (1, 4)

​          (2, 3) (2, 4)

​                   (3, 4)

There is 6 ways to select 2 out of 4 members. 

We can get the same result using the formula:
$$
\binom{4}{2} = \frac{4!}{2!(4-2)!}
$$


## Solved Example

There are 50 people at a party. Among them, each person shakes hand with each of the others exactly once. Then how many handshakes are supposed to happen there?
Solution

To find: The total number of shake hands at the party.

The total number of people at the party is n = 50.

For a shaking hand to happen, there must be two people.

So the number of shake hands is equal to the number of ways of selecting 2 people out of 50 people. So k = 2.

Using the n choose k formula,

C (n , k) = n! / [ (n-k)! k! ]

C (50, 2) = 50! / [ (50 - 2)! 2! ]

C (50, 2) = (50 × 49 × 48!) / (48! 2!)

C (50, 2) = (50 × 49) / (2 × 1)

C (50, 2) = 1225.

Answer: The number of shake hands = 1,225.

## Asymptotic behavior related to binomial coefficient 
### Question

For each of the following sets of five functions, order them so that if fa appears before fb in your sequence, then $f_a = O(f_b)$. If $f_a = O(f_b)$ and $f_b = O(f_a)$ (meaning $f_a$ and $f_b$ could appear in either order), indicate this by enclosing fa and fb in a set with curly braces.
$$
f_1 = 2^n
$$

$$
f_2 = n^3
$$

$$
f_3 = \binom{n}{n/2}
$$

$$
f_4 = n!
$$

$$
f_5 = \binom{n}{3}
$$

### mathematical formulas used in the problem

We need to know a few mathematical formula before we start solving the problem:

* $({a}{b})^n = {a^n}{b^n}$, $(\frac{a}{b})^n = \frac{a^n}{b^n}$

* In the big O world, the slow growing function can be ignored. If $f_1= f_a + f_b$  and $f_a=o(f_b)$, then $f_1=O(f_b)$; If $f2= fa fb$ and $f_a=o(f_b)$, you cannot ignore $f_a$, $f_1=O(f_a f_b)$. 

* Sterling approximation: **Stirling's approximation**  is an approximation for [factorials](https://en.wikipedia.org/wiki/Factorial).
  $$
  n!\sim {\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}
  $$

### Working procedure to the solution

Without any calculation but with the help of Stirling's approximation, we know $O(f_2) < O(f_1) < O(f_4)$



## 



## Reference

[n Choose k Formula](https://www.cuemath.com/n-choose-k-formula/)

[Stirling's approximationrling's approximation](https://en.wikipedia.org/wiki/Stirling%27s_approximation)

# 

