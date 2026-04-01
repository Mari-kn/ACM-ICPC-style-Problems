# ACM Competitive Programming Solutions (Python)

A comprehensive collection of **55+ classic algorithm problems** solved in Python, organized by topic. Each solution follows ACM contest format with stdin/stdout I/O, multiple approaches, complexity analysis, and edge case handling.

---

## Repository Structure

```
acm-python-solutions/
│
├── arrays/                         # Arrays & Two Pointers
│   ├── two_sum.py                  # Hash map — O(n)
│   ├── reverse_integer.py          # Math-based digit reversal + overflow check
│   ├── palindrome_number.py        # Half-reversal without string conversion
│   ├── valid_parentheses.py        # Stack-based bracket matching
│   ├── fizzbuzz.py                 # Single pass, check %15 first
│   ├── factorial.py                # Iterative O(1) space & recursive O(n) space
│   ├── fibonacci.py                # Bottom-up DP vs naive recursion
│   ├── find_all_pairs.py           # Hash set for complements — O(n)
│   ├── remove_duplicates.py        # Two-pointer in-place — O(1) space
│   ├── move_zeroes.py              # Two-pointer swap — O(1) space
│   ├── container_with_most_water.py# Two-pointer greedy — O(n)
│   ├── trapping_rain_water.py      # Two-pointer left_max/right_max — O(n)
│   ├── three_sum_four_sum.py       # Sort + two-pointer — O(n^2) / O(n^3)
│   └── maximum_subarray.py         # Kadane's algorithm — O(n)
│
├── strings/                        # String Algorithms
│   ├── longest_substring_no_repeat.py  # Sliding window + hash map — O(n)
│   ├── valid_anagram.py            # Frequency count array — O(n)
│   ├── string_compression.py       # Run-length encoding — O(n)
│   ├── kmp_pattern_matching.py     # KMP with LPS table — O(n + m)
│   ├── rabin_karp.py               # Rolling hash — O(n + m) avg
│   └── longest_palindromic_substring.py # Expand-around-center + Manacher's
│
├── backtracking/                   # Backtracking & Recursion
│   ├── generate_permutations.py    # In-place swap backtracking — O(n * n!)
│   ├── generate_subsets.py         # Backtracking + bitmask approaches
│   ├── n_queens.py                 # Column/diagonal set tracking — O(n!)
│   ├── sudoku_solver.py            # Constraint propagation + backtracking
│   └── combination_sum.py          # Variants I (reuse) & II (no reuse + dedup)
│
├── sorting_searching/              # Sorting & Searching
│   ├── binary_search.py            # Classic + lower_bound + upper_bound
│   ├── merge_sort.py               # Divide-and-conquer + in-place variant
│   ├── quick_sort.py               # Lomuto & Hoare + median-of-three pivot
│   ├── kth_largest.py              # Quickselect O(n) + min-heap O(n log k)
│   └── search_rotated_sorted.py    # Modified binary search + pivot finder
│
├── stacks_queues/                  # Stacks & Queues
│   ├── min_stack.py                # Auxiliary min-stack — O(1) all ops
│   ├── evaluate_rpn.py             # Stack-based postfix evaluation
│   ├── sliding_window_maximum.py   # Monotonic decreasing deque — O(n)
│   ├── largest_rectangle_histogram.py # Monotonic increasing stack — O(n)
│   └── queue_using_stacks.py       # Two-stack lazy transfer — O(1) amortized
│
├── graphs/                         # Graph Algorithms
│   ├── dfs.py                      # Recursive + iterative implementations
│   ├── bfs.py                      # Level-order + shortest distance (unweighted)
│   ├── connected_components.py     # DFS + Union-Find (DSU)
│   ├── dijkstra.py                 # Min-heap + path reconstruction
│   ├── bellman_ford.py             # V-1 relaxations + negative cycle detection
│   ├── floyd_warshall.py           # All-pairs DP + path reconstruction
│   ├── topological_sort.py         # Kahn's BFS + DFS post-order
│   └── detect_cycle.py             # Directed (coloring) + undirected (parent/DSU)
│
├── trees/                          # Tree Algorithms
│   ├── binary_tree_traversals.py   # Inorder/preorder/postorder (recursive + iterative) + level-order
│   ├── lowest_common_ancestor.py   # Recursive DFS + binary lifting O(log n)
│   ├── diameter_binary_tree.py     # Single DFS pass (recursive + iterative)
│   ├── balanced_binary_tree.py     # DFS with early termination
│   └── serialize_deserialize_tree.py # Preorder + BFS serialization
│
├── dp/                             # Dynamic Programming
│   ├── climbing_stairs.py          # Bottom-up O(1) space + k-steps variant
│   ├── coin_change.py              # Min coins + combinations + permutations
│   ├── lis.py                      # O(n^2) DP + O(n log n) patience sorting
│   ├── lcs.py                      # Full table reconstruction + space-optimized
│   ├── knapsack_01.py              # Full reconstruction + O(W) optimized
│   ├── edit_distance.py            # Operation trace + space-optimized
│   └── matrix_chain_multiplication.py # Interval DP + parenthesization output
│
├── greedy/                         # Greedy Algorithms
│   ├── activity_selection.py       # Sort by finish time + weighted DP variant
│   ├── huffman_coding.py           # Min-heap tree + encode/decode
│   ├── minimum_coins_greedy.py     # Greedy (canonical) + DP fallback
│   └── gas_station.py              # Single-pass surplus tracking — O(n)
│
├── math/                           # Number Theory & Math
│   ├── gcd_lcm.py                  # Euclidean + extended GCD + multi-element
│   ├── sieve_primes.py             # Eratosthenes + linear sieve + SPF factorization
│   ├── modular_arithmetic.py       # mod ops + Fermat inverse + nCr + CRT
│   ├── fast_exponentiation.py      # Binary exponentiation + matrix power
│   └── fibonacci_matrix.py         # Matrix exponentiation + fast doubling — O(log n)
│
├── advanced_ds/                    # Advanced Data Structures
│   ├── union_find.py               # Path compression + rank + rollback variant
│   ├── segment_tree.py             # Point update + lazy propagation
│   ├── fenwick_tree.py             # 1D + 2D Binary Indexed Tree
│   ├── minimum_spanning_tree.py    # Kruskal (DSU) + Prim (heap)
│   └── max_flow.py                 # Edmonds-Karp + Dinic's algorithm
│
└── README.md
```

---

## What Makes This Repo Stand Out

Every solution includes:

- **Problem description** — concise explanation at the top of each file
- **Multiple approaches** — brute force to optimized (e.g., O(n^2) DP + O(n log n) binary search for LIS)
- **Complexity analysis** — time and space for every approach
- **ACM-style I/O** — stdin input with test cases, ready for online judges
- **Edge case handling** — overflow checks, empty inputs, negative numbers, boundary conditions
- **Reconstruction** — not just the answer, but the actual path/sequence/items where applicable

---

## How to Run

Each file is standalone. Feed input via stdin:

```bash
# Example: Two Sum
echo "1
4 9
2 7 11 15" | python3 arrays/two_sum.py

# Example: Dijkstra
echo "5 6 0
0 1 4
0 2 1
2 1 2
1 3 1
2 4 5
3 4 3" | python3 graphs/dijkstra.py

# Example: Knapsack
echo "1
4 7
1 1
3 4
4 5
5 7" | python3 dp/knapsack_01.py
```

---

## Topics Covered

| Category | Problems | Key Techniques |
|---|---|---|
| **Arrays** | 14 | Two pointers, sliding window, hash map, Kadane's |
| **Strings** | 6 | KMP, Rabin-Karp, Manacher's, sliding window |
| **Backtracking** | 5 | Permutations, subsets, constraint satisfaction |
| **Sorting & Searching** | 5 | Binary search variants, quickselect, merge/quick sort |
| **Stacks & Queues** | 5 | Monotonic stack/deque, RPN, two-stack queue |
| **Graphs** | 8 | BFS, DFS, Dijkstra, Bellman-Ford, Floyd-Warshall, topo sort |
| **Trees** | 5 | Traversals, LCA, diameter, serialization |
| **Dynamic Programming** | 7 | Knapsack, LIS, LCS, edit distance, interval DP |
| **Greedy** | 4 | Activity selection, Huffman, gas station |
| **Number Theory** | 5 | GCD, sieve, modular inverse, CRT, matrix exponentiation |
| **Advanced DS** | 5 | Segment tree, Fenwick tree, DSU, MST, max flow |

**Total: 69 problems across 11 categories**

---

## License

Free to use for learning, practice, and competitive programming.
