# Selection and Insertion Sort

The logic for both algorithms is quite similar. Both insertion sort and selection sort have an outer loop (over every  index), and an inner loop (over a subset of indices).  Each pass of the  inner loop expands the sorted region by one element, at the expense of  the unsorted region, until it runs out of unsorted elements.

Both of sorting has $O(n^2)$.

The difference is in what the inner loop does:

- In selection sort, the inner loop is over the **unsorted** elements.  Each pass selects one element, and moves it to its final location (at the current end of the sorted region).
- In insertion sort, each pass of the inner loop iterates over the **sorted** elements. Sorted elements are displaced until the loop finds the correct place to insert the next unsorted element.



## Reference

[Insertion Sort vs. Selection Sort](https://stackoverflow.com/questions/15799034/insertion-sort-vs-selection-sort)

[Java: SelectionSort animated demo with code](https://www.youtube.com/watch?v=cqh8nQwuKNE)

[Java: Insertion Sort sorting algorithm](https://www.youtube.com/watch?v=lCDZ0IprFw4)



# 



