# 🧠 Exercises: Stage 03 (Data Structures & Algorithms in Java)

### `EX-03-1`: Custom ArrayList & LinkedList
* **Goal**: Understand internal memory management, dynamic array resizing, and pointer linking.
* **Tasks**:
  1. Implement `CustomArrayList<E>`:
     - Internal `Object[]` array with default capacity of 10.
     - Automatic geometric resizing (growth factor 1.5x) when full.
     - `add(E e)`, `get(int index)`, `remove(int index)`, `size()`.
     - Bounds checking with `IndexOutOfBoundsException`.
  2. Implement `CustomLinkedList<E>`:
     - Doubly-linked list with `Node<E>` (prev, next, value).
     - `addFirst(E e)`, `addLast(E e)`, `removeFirst()`, `removeLast()`.
  3. Write complete JUnit 5 test suites verifying edge cases (empty list, removing only element, resizing).

---

### `EX-03-2`: Custom HashMap with Collision Handling
* **Goal**: Demystify how `java.util.HashMap` works under the hood.
* **Tasks**:
  1. Implement `CustomHashMap<K, V>`:
     - An array of buckets (array of linked list entries).
     - Custom hash function calculating bucket index: `Math.abs(key.hashCode()) % buckets.length`.
     - `put(K key, V value)`, `get(K key)`, `remove(K key)`.
     - Handle collisions via separate chaining.
     - Dynamic rehash when load factor exceeds `0.75`.
  2. Write unit tests with intentional hash collisions to prove chaining works.

---

### `EX-03-3`: Binary Search Tree & BFS/DFS Traversals
* **Goal**: Master recursive and iterative tree algorithms.
* **Tasks**:
  1. Implement `BinarySearchTree<T extends Comparable<T>>`:
     - `insert(T val)`, `contains(T val)`, `delete(T val)`.
  2. Implement traversal methods:
     - `inOrderTraversal()` (returns sorted list).
     - `breadthFirstTraversal()` (level-order traversal using a `Queue`).
     - `findHeight()` (calculates maximum depth recursively).
  3. Verify with unit tests against balanced and unbalanced trees.

---

### `EX-03-4`: Big-O Profiler & Algorithm Benchmarks
* **Goal**: Observe algorithmic growth rates in practice.
* **Tasks**:
  1. Implement three sorting algorithms: Bubble Sort $O(N^2)$, Merge Sort $O(N \log N)$, and Java's `Arrays.sort()` (Dual-Pivot Quicksort).
  2. Run benchmarks with input sizes: $N = 1,000$, $10,000$, $100,000$.
  3. Measure elapsed time in milliseconds and graph the results in `benchmarks.md`.
