# The Dijkstra's Dinner Party That Explains Concurrency

*Originally published on [Medium](https://ironengineer.medium.com/the-dijkstras-dinner-party-that-explains-concurrency-e8a06c469d07) - Free access version*

## Overview

I recently joined [Phil Eaton's book club](https://eatonphil.com/2025-art-of-multiprocessor-programming.html), where we are reading [The Art of Multiprocessor Programming](https://amzn.to/4oHoc9R) by Herlihy, Shavit, Luchangco, and Spear. This post is my reflection on Chapter 1.

Most of us know Edsger W. Dijkstra from his famous shortest path algorithm. But he also gave us another gem: the **Dining Philosophers Problem**, a simple story that reveals the challenges of concurrent programming.

Here is the setup:

* Five philosophers sit around a table.
* Each has one chopstick to the left and one to the right.
* To eat, they need both chopsticks.
* After eating, they think, and then repeat.

![Dining Philosophers](https://diningphilosophers.eu/pictures/dining.png)
*Image source: [diningphilosophers.eu](https://diningphilosophers.eu/)*

It sounds harmless, until everyone gets hungry at the same time.

---

## The Challenges

### 1. Shared Objects and Mutual Exclusion

Each chopstick is a **shared resource**. Only one philosopher can hold it at a time. If it is taken, others must wait.

This is the same idea as a **lock** in programming:

* A thread acquires a lock to enter a critical section.
* If another thread tries to acquire the same lock, it must wait.
* The operating system blocks and wakes threads as needed.

Philosophers waiting on chopsticks are like threads waiting on locks.

---

### 2. Deadlock

Imagine all five philosophers grab the chopstick on their left at the same time. Now each has one chopstick and is waiting for the second. Nobody can eat.

This is **deadlock**, when threads are stuck waiting for each other and cannot make progress.

---

### 3. Starvation

Suppose philosophers agree to release a chopstick if they cannot get the second. Deadlock is avoided, but a new problem emerges:

A philosopher may repeatedly grab and release a chopstick, while neighbors finish and eat again. Eventually, this philosopher may never eat.

This is **starvation**, when some threads are perpetually denied access to shared resources, even though the system as a whole is making progress.

---

## Python Simulation

Here is a Python version of the Dining Philosophers problem using `threading.Lock` and `Thread`.

```python
from threading import Lock, Thread
import time, random

class Table:
    def __init__(self, n):
        self.chopsticks = [Lock() for _ in range(n)]

class Philosopher(Thread):
    def __init__(self, num, left, right):
        super().__init__()
        # Always pick locks in a consistent order to avoid deadlock
        self.num = num
        self.ch_l, self.ch_r = (left, right) if id(left) < id(right) else (right, left)

    def run(self):
        for _ in range(3):
            self.think()
            self.eat()

    def think(self):
        time.sleep(random.uniform(0.1, 0.5))
        print(f"Philosopher {self.num} finished thinking")

    def eat(self):
        with self.ch_l:
            print(f"Philosopher {self.num} grabbed left chopstick")
            with self.ch_r:
                print(f"Philosopher {self.num} grabbed right chopstick")
                time.sleep(random.uniform(0.1, 0.3))
                print(f"Philosopher {self.num} finished eating")

class Dinner:
    def __init__(self, n=5):
        self.table = Table(n)
        self.philosophers = [
            Philosopher(i, self.table.chopsticks[i], self.table.chopsticks[(i+1)%n])
            for i in range(n)
        ]

    def dine(self):
        for p in self.philosophers: p.start()
        for p in self.philosophers: p.join()

Dinner().dine()
```

---

## How Deadlock is Avoided

The trick is **ordering resources consistently**. Each philosopher always picks the lower-id chopstick first. This prevents the circular waiting that causes deadlock.

Other approaches include:

* Letting odd and even philosophers pick in different orders.
* Assigning numbers to resources and always acquiring in increasing order.

---

## Takeaways

The Dining Philosophers problem teaches three fundamental concurrency concepts:

* **Mutual exclusion**: safely sharing resources.
* **Deadlock**: threads stuck waiting for each other.
* **Starvation**: threads repeatedly denied access.

A simple dinner party turns out to be a timeless lesson in concurrent programming, thanks to E.W. Dijkstra.
