"""
Dining Philosophers Problem Implementation

A classic concurrent programming problem demonstrating deadlock prevention
through lock ordering. Five philosophers sit at a round table with chopsticks
between them. Each philosopher needs two chopsticks to eat.

Key insight: Prevent deadlock by ordering lock acquisition based on memory address.
"""

from threading import Lock, Thread
import time
import random

class Table:
    def __init__(self, n):
        self.chopsticks = [Lock() for i in range(n)]

class Philosopher(Thread):
    def __init__(self, num, ch_s1, ch_s2):
        super().__init__()
        self.num = num
        # Critical deadlock prevention: order locks by memory address
        self.ch_l, self.ch_r = (ch_s1, ch_s2) if id(ch_s1) < id(ch_s2) else (ch_s2, ch_s1)

    def run(self):
        for _ in range(3):
            self.think()
            self.eat()

    def think(self):
        time.sleep(random.uniform(0.1, 0.5))
        print(f"Philosopher {self.num} finished thinking")

    def eat(self):
        # Nested lock acquisition in consistent order prevents deadlock
        with self.ch_l:
            print(f"Philosopher {self.num} grabbed left chopstick")
            with self.ch_r:
                print(f"Philosopher {self.num} grabbed right chopstick")
                time.sleep(random.uniform(0.1, 0.3))
                print(f"Philosopher {self.num} finished eating")

class Dinner:
    def __init__(self, philosopher_num=5):
        self.table = Table(philosopher_num)
        self.philosophers = [
            Philosopher(
                i, 
                self.table.chopsticks[i], 
                self.table.chopsticks[(i+1)%philosopher_num]
            ) 
            for i in range(philosopher_num)
        ]

    def dine(self):
        for ph in self.philosophers:
            ph.start()

        for ph in self.philosophers:
            ph.join()

if __name__ == "__main__":
    d = Dinner(philosopher_num=5)
    d.dine()
