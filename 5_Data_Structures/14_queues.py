from collections import deque
deque = deque([])
deque.append(1)
deque.append(2)
deque.append(3)
deque.popleft()
print(deque)

if not deque:
    print("Empty")
