#! usr/bin/python
"""Unit tests associated with priority_queue.py

NOTE: This is WIP."""

import priority_queue
import unittest

class PriorityQueueTest(unittest.TestCase):
    
    def testPriorityQueue_DuplicateTask(self):
        queue = ([
            [0, 3],
            [1, 5],
            [2, 1],
            [0, 2]])

        self.assertRaises(priority_queue.PriorityQueueDuplicateTaskException,
                priority_queue.PriorityQueue, queue)

    def testPriorityQueue_PopEmptyQueue(self):
        queue = priority_queue.PriorityQueue()
        self.assertRaises(priority_queue.EmptyPriorityQueueException, 
                priority_queue.PriorityQueue.pop, queue)

    def testPriorityQueue_FromTuple(self):
        queue = priority_queue.PriorityQueue([
            [0, 5],
            [1, 3],
            [2, 8],
            [3, 6],
            [4, 2],
            [5, 7],
            [6, 1],
            [7, 5]])

        expected = [
            [6, 1],
            [1, 3],
            [4, 2],
            [7, 5],
            [0, 5],
            [2, 8],
            [5, 7],
            [3, 6]]

        self.assertEqual(expected, queue.pq)

    def testPriorityQueue_Pop(self):
        queue = priority_queue.PriorityQueue([
            [0, 5],
            [1, 3],
            [2, 8],
            [3, 6],
            [4, 2],
            [5, 7],
            [6, 1],
            [7, 5]])

        expected_task = [6, 1]
        expected_remaining_queue = [
            [4, 2],
            [1, 3],
            [3, 6],
            [7, 5],
            [0, 5],
            [2, 8],
            [5, 7]]

        task = queue.pop()
        self.assertEqual(expected_task, task)
        self.assertEqual(expected_remaining_queue, queue.pq)
