# The Art of Multiprocessor Programming - Study Notes & Exercises

This repository contains my reflections, notes, and code exercises while studying [The Art of Multiprocessor Programming](https://amzn.to/4oHoc9R) by Maurice Herlihy and Nir Shavit.

## About the Book

[The Art of Multiprocessor Programming](https://amzn.to/4oHoc9R) is a comprehensive guide to the principles and practice of multiprocessor programming. It covers fundamental concepts of concurrent programming, synchronization primitives, lock-free data structures, and the theoretical foundations of parallel computing.

## Study Approach

This repository documents my journey through the book with:
- **Chapter-by-chapter reflections** on key concepts and insights
- **Code implementations** of algorithms and data structures presented in the book
- **Exercises and experiments** to deepen understanding of concurrent programming
- **Performance analysis** and benchmarking of different synchronization approaches

## Repository Structure

```
art-of-multiprocessor-programming/
├── README.md
├── chapters/
│   ├── chapter-01-introduction/
│   ├── chapter-02-mutual-exclusion/
│   ├── chapter-03-concurrent-objects/
│   └── [Additional chapters as studied]
├── exercises/
│   ├── locks/
│   ├── lock-free/
│   └── algorithms/
├── benchmarks/
│   └── performance-tests/
└── notes/
    ├── key-concepts.md
    └── implementation-patterns.md
```

## Learning Goals

- **Understand fundamental principles** of multiprocessor programming
- **Master synchronization primitives** and their trade-offs
- **Implement lock-free data structures** and algorithms
- **Analyze performance characteristics** of concurrent programs
- **Build intuition** for designing scalable parallel systems

## Progress Tracking

### Completed Chapters
- [x] Chapter 1: Introduction
- [ ] Chapter 2: Mutual Exclusion
- [ ] Chapter 3: Concurrent Objects
- [ ] Chapter 4: Foundations of Shared Memory
- [ ] Chapter 5: The Relative Power of Primitive Synchronization Operations
- [ ] [Additional chapters to be added as studied]

### Key Implementations
- [x] Dining Philosophers (Lock Ordering)
- [ ] Peterson's Algorithm
- [ ] Bakery Algorithm
- [ ] Test-and-Set Lock
- [ ] Queue Lock
- [ ] Lock-Free Stack
- [ ] Lock-Free Queue
- [ ] [Additional implementations to be added]

## Development Environment

- **Languages**: Java, C++, and potentially other languages for specific examples
- **Tools**: Performance profiling tools, concurrent testing frameworks
- **Platform**: Multi-core systems for realistic concurrent execution testing

## Academic Context

This study complements my work on CMU 15-213 (Introduction to Computer Systems) by diving deeper into the theoretical and practical aspects of concurrent programming. While 15-213 provides the systems foundation, this book explores the algorithmic and theoretical aspects of multiprocessor programming.

## References

- Herlihy, Maurice, and Nir Shavit. *The Art of Multiprocessor Programming*. Morgan Kaufmann, 2020.
- Related academic papers and research as encountered during study

---

*This repository serves as both a learning journal and a reference for concurrent programming concepts and implementations.*
