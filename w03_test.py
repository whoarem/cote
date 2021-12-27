import queue

a = queue.PriorityQueue()
a.put((10, '캠퍼스'))
a.put((1, '패스트'))

print(' '.join([a.get()[1], a.get()[1]]))
