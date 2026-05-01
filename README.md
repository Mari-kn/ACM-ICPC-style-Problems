# ACM Competitive Programming Solutions in Python

A beginner-friendly roadmap to learn data structures, algorithms, and competitive programming through 69 classic ACM/ICPC-style problems.

A comprehensive collection of **69 classic algorithm problems** solved in Python, organized by topic. Each solution follows ACM contest format with stdin/stdout I/O, multiple approaches, complexity analysis, and edge case handling.

---

## Who Is This For?

- Python beginners who want to learn through problem solving
- Students preparing for ICPC, university exams, or coding interviews
- Developers practicing data structures and algorithms
- Anyone who wants ACM-style stdin/stdout Python solutions

---

## Start Here

If you are new, follow the 5-phase learning plan below.
If you already know Python, jump directly to:
- Arrays
- Graphs
- Dynamic Programming
- Advanced Data Structures

---

## Beginner's Guide: Learn Python Through This Repo

If you're new to Python and want to learn programming through problem-solving, this repo is a structured way to do it. Below is a **5-phase learning plan** that takes you from zero to competitive programming level, using the problems in this repo.

### Prerequisites

- Install Python 3 on your machine
- Know how to run a `.py` file from the terminal: `python3 filename.py`
- A text editor (VS Code recommended)

### Phase 1: Python Basics (Week 1-2)

Start here. These problems use basic Python: variables, loops, conditionals, and simple math.

| # | Problem | File | What You'll Learn |
|---|---------|------|-------------------|
| 1 | FizzBuzz | `arrays/fizzbuzz.py` | `if/elif/else`, `for` loop, `print()`, modulo `%` |
| 2 | Factorial | `arrays/factorial.py` | Loops vs recursion, function definitions |
| 3 | Fibonacci | `arrays/fibonacci.py` | Recursion, memoization, building sequences |
| 4 | Palindrome Number | `arrays/palindrome_number.py` | While loops, integer operations |
| 5 | Reverse Integer | `arrays/reverse_integer.py` | Digit manipulation, overflow awareness |
| 6 | GCD & LCM | `math/gcd_lcm.py` | Euclidean algorithm, `while` loops |

**Tips for Phase 1:**
- Read each file top to bottom. Every file starts with a problem description.
- Type the code yourself instead of copy-pasting. This builds muscle memory.
- Try solving the problem on your own before reading the solution.
- Run the code with the example inputs and verify the output.

### Phase 2: Data Structures Fundamentals (Week 3-4)

Learn Python's built-in data structures: lists, dictionaries, sets, and stacks.

| # | Problem | File | What You'll Learn |
|---|---------|------|-------------------|
| 1 | Two Sum | `arrays/two_sum.py` | Dictionaries (hash maps), `enumerate()` |
| 2 | Valid Anagram | `strings/valid_anagram.py` | Frequency counting, string iteration |
| 3 | Find All Pairs | `arrays/find_all_pairs.py` | Sets, complement searching |
| 4 | Remove Duplicates | `arrays/remove_duplicates.py` | Two-pointer technique, in-place modification |
| 5 | Move Zeroes | `arrays/move_zeroes.py` | Array partitioning, swapping |
| 6 | Valid Parentheses | `arrays/valid_parentheses.py` | Stacks (using lists), matching patterns |
| 7 | String Compression | `strings/string_compression.py` | String building, run-length encoding |
| 8 | Min Stack | `stacks_queues/min_stack.py` | Stack design, tracking auxiliary state |
| 9 | Queue Using Stacks | `stacks_queues/queue_using_stacks.py` | Queue vs stack behavior, amortized analysis |

**Tips for Phase 2:**
- Focus on understanding *when* to use which data structure.
- Dictionary = fast lookups by key. Set = fast membership checks. List = ordered sequence.
- Draw out what happens at each step on paper.

### Phase 3: Core Algorithms (Week 5-7)

Now tackle sorting, searching, and fundamental algorithmic techniques.

| # | Problem | File | What You'll Learn |
|---|---------|------|-------------------|
| 1 | Binary Search | `sorting_searching/binary_search.py` | Divide and conquer, `while` with bounds |
| 2 | Merge Sort | `sorting_searching/merge_sort.py` | Recursion, divide and conquer, stable sorting |
| 3 | Quick Sort | `sorting_searching/quick_sort.py` | Partitioning, pivot selection |
| 4 | Maximum Subarray | `arrays/maximum_subarray.py` | Kadane's algorithm, dynamic thinking |
| 5 | Container With Most Water | `arrays/container_with_most_water.py` | Two-pointer greedy strategy |
| 6 | Three Sum / Four Sum | `arrays/three_sum_four_sum.py` | Sorting + two pointers, deduplication |
| 7 | Longest Substring No Repeat | `strings/longest_substring_no_repeat.py` | Sliding window technique |
| 8 | Kth Largest Element | `sorting_searching/kth_largest.py` | Quickselect, heaps (`heapq`) |
| 9 | Sieve of Primes | `math/sieve_primes.py` | Sieve of Eratosthenes, prime number theory |
| 10 | Evaluate RPN | `stacks_queues/evaluate_rpn.py` | Stack-based expression evaluation |

**Tips for Phase 3:**
- Learn to analyze time complexity. Each file includes Big-O analysis — study it.
- Understand *why* an approach is O(n) vs O(n^2). This is the core skill of competitive programming.
- Try the brute force approach first, then read the optimized solution.

### Phase 4: Intermediate Techniques (Week 8-11)

Graphs, trees, dynamic programming, and backtracking. This is where problem-solving gets serious.

**Graphs & Trees — start here:**

| # | Problem | File | What You'll Learn |
|---|---------|------|-------------------|
| 1 | DFS | `graphs/dfs.py` | Depth-first traversal, recursion on graphs |
| 2 | BFS | `graphs/bfs.py` | Breadth-first traversal, shortest path (unweighted) |
| 3 | Binary Tree Traversals | `trees/binary_tree_traversals.py` | Inorder, preorder, postorder, level-order |
| 4 | Connected Components | `graphs/connected_components.py` | Graph structure, Union-Find basics |
| 5 | Detect Cycle | `graphs/detect_cycle.py` | Graph coloring, cycle detection |
| 6 | Topological Sort | `graphs/topological_sort.py` | DAGs, dependency ordering |
| 7 | Dijkstra | `graphs/dijkstra.py` | Priority queues, shortest path (weighted) |
| 8 | LCA | `trees/lowest_common_ancestor.py` | Tree queries, binary lifting |

**Dynamic Programming — then move here:**

| # | Problem | File | What You'll Learn |
|---|---------|------|-------------------|
| 1 | Climbing Stairs | `dp/climbing_stairs.py` | DP basics, overlapping subproblems |
| 2 | Coin Change | `dp/coin_change.py` | Classic DP, multiple problem variants |
| 3 | LIS | `dp/lis.py` | 1D DP + binary search optimization |
| 4 | LCS | `dp/lcs.py` | 2D DP table, reconstruction |
| 5 | 0/1 Knapsack | `dp/knapsack_01.py` | Subset selection, space optimization |
| 6 | Edit Distance | `dp/edit_distance.py` | String DP, operation tracking |

**Backtracking:**

| # | Problem | File | What You'll Learn |
|---|---------|------|-------------------|
| 1 | Generate Subsets | `backtracking/generate_subsets.py` | Recursion trees, bitmask enumeration |
| 2 | Generate Permutations | `backtracking/generate_permutations.py` | Swap-based backtracking |
| 3 | N-Queens | `backtracking/n_queens.py` | Constraint satisfaction |
| 4 | Combination Sum | `backtracking/combination_sum.py` | Pruning, candidate reuse |

**Tips for Phase 4:**
- Draw the graphs and trees on paper. Trace through DFS/BFS by hand.
- For DP: always define what `dp[i]` represents before coding. Write the recurrence relation first.
- Backtracking = "try everything, undo if it doesn't work." Visualize the recursion tree.

### Phase 5: Advanced Topics (Week 12+)

Once you're comfortable with Phase 4, tackle these for contest-level preparation.

| # | Problem | File | What You'll Learn |
|---|---------|------|-------------------|
| 1 | Trapping Rain Water | `arrays/trapping_rain_water.py` | Advanced two-pointer |
| 2 | Sliding Window Maximum | `stacks_queues/sliding_window_maximum.py` | Monotonic deque |
| 3 | Largest Rectangle in Histogram | `stacks_queues/largest_rectangle_histogram.py` | Monotonic stack |
| 4 | KMP Pattern Matching | `strings/kmp_pattern_matching.py` | Prefix function, string algorithms |
| 5 | Matrix Chain Multiplication | `dp/matrix_chain_multiplication.py` | Interval DP |
| 6 | Bellman-Ford | `graphs/bellman_ford.py` | Negative weights, cycle detection |
| 7 | Floyd-Warshall | `graphs/floyd_warshall.py` | All-pairs shortest path |
| 8 | Segment Tree | `advanced_ds/segment_tree.py` | Range queries, lazy propagation |
| 9 | Fenwick Tree | `advanced_ds/fenwick_tree.py` | Binary indexed tree, prefix sums |
| 10 | Union-Find | `advanced_ds/union_find.py` | Disjoint set union, path compression |
| 11 | MST | `advanced_ds/minimum_spanning_tree.py` | Kruskal's and Prim's algorithms |
| 12 | Max Flow | `advanced_ds/max_flow.py` | Network flow, Edmonds-Karp, Dinic's |
| 13 | Greedy Problems | `greedy/*.py` | Activity selection, Huffman coding, gas station |
| 14 | Modular Arithmetic | `math/modular_arithmetic.py` | Mod inverse, CRT, nCr under mod |
| 15 | Fast Exponentiation | `math/fast_exponentiation.py` | Binary exponentiation, matrix power |
| 16 | Sudoku Solver | `backtracking/sudoku_solver.py` | Heavy constraint propagation |

**Tips for Phase 5:**
- These problems appear in ICPC regionals and Codeforces Div 1-2.
- Focus on understanding the data structure before the problem. Read segment tree theory before solving segment tree problems.
- Practice on online judges: [Codeforces](https://codeforces.com), [LeetCode](https://leetcode.com), [AtCoder](https://atcoder.jp).

### How to Study Each Problem

For every problem file in this repo, follow this process:

1. **Read the problem description** at the top of the file
2. **Try to solve it yourself** for 20-30 minutes
3. **If stuck**, read only the approach/comments, then try again
4. **Read the full solution** and compare with yours
5. **Study the complexity analysis** — understand why it's O(n), O(n log n), etc.
6. **Run it** with the example inputs: `echo "input" | python3 path/to/file.py`
7. **Modify the code** — change something, break it, fix it. This builds understanding.

---

## Repository Structure

```
ACM/
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
