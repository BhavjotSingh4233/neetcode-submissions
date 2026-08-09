from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        skipped = 0
        while queue: 
            if queue[0] == sandwiches[0]: 
                queue.popleft() 
                sandwiches.pop(0)
                skipped = 0
            else: 
                queue.append(queue.popleft())
                skipped += 1
            
            if skipped == len(queue):
                break

        return len(queue) 