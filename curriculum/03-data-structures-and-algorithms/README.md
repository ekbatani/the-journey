# 🧠 Stage 03: Data Structures & Algorithms in Java

> **Roadmap**: [roadmap.sh/datastructures-and-algorithms](https://roadmap.sh/datastructures-and-algorithms)

---

## 🎯 Learning Objectives
By the end of this stage, you should:
- Analyze time and space complexity with Big-O notation with mathematical rigor.
- Understand low-level array allocation, contiguous memory vs pointer dereferencing in Java.
- Implement custom data structures from scratch (`ArrayList`, `LinkedList`, `HashMap`, `BinarySearchTree`).
- Understand hashing, hash collisions, load factors, and red-black tree bucket trees in `java.util.HashMap`.
- Implement and benchmark sorting and searching algorithms.

---

## 📚 Core Topics & Complexity Table

| Data Structure | Access | Search | Insertion | Deletion | Java Class |
|---|---|---|---|---|---|
| **Array** | $O(1)$ | $O(N)$ | $O(N)$ | $O(N)$ | `int[]`, `T[]` |
| **Dynamic Array** | $O(1)$ | $O(N)$ | $O(1)$ amortized | $O(N)$ | `ArrayList<T>` |
| **Singly/Doubly Linked List** | $O(N)$ | $O(N)$ | $O(1)$ (at head/tail) | $O(1)$ | `LinkedList<T>` |
| **Hash Table** | $N/A$ | $O(1)$ avg | $O(1)$ avg | $O(1)$ avg | `HashMap<K, V>` |
| **Binary Search Tree** | $O(\log N)$ avg | $O(\log N)$ avg | $O(\log N)$ avg | $O(\log N)$ avg | `TreeSet<T>`, `TreeMap<K, V>` |
| **Heap / Priority Queue** | $O(1)$ (peek) | $O(N)$ | $O(\log N)$ | $O(\log N)$ | `PriorityQueue<T>` |

### Tree & Graph Traversals
- **Breadth-First Search (BFS)**: Uses a `Queue` for level-order traversal.
- **Depth-First Search (DFS)**: Pre-order, In-order, Post-order using recursion or an explicit `Stack`.

---

## 🧪 Assigned Exercises
Navigate to [`exercises/03-dsa-java/`](../../exercises/03-dsa-java/):
* **`EX-03-1`**: Custom ArrayList & LinkedList
* **`EX-03-2`**: Custom HashMap with Collision Handling
* **`EX-03-3`**: Binary Search Tree & BFS/DFS Traversals
* **`EX-03-4`**: Big-O Profiler & Algorithm Benchmarks

---

## 🌟 Milestone 1 Checkpoint
Upon completing this stage, proceed to **[Milestone 1: CLI Analytics & Expense Engine](../../milestones/milestone-1-cli-task-engine/README.md)**.
