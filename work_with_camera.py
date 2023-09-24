# import cv2
#
# cap = cv2.VideoCapture(0)
# fourcc = cv2.CAP_PROP_FOURCC
# out = cv2.VideoWriter(
#     'output.avi',
#     fourcc,
#     20.0,
#     (640, 480)
# )
#
# while True:
#     ret, frame = cap.read()
#     out.write(frame)
#
#     face_cascade = cv2.CascadeClassifier('xmls/haarcascade_frontalface_default.xml')
#
#     faces = face_cascade.detectMultiScale(
#         frame,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         maxSize=(30, 30)
#     )
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     cv2.imshow('Video', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()


# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def push(self, item):
#         self.items.append(item)
#         return self.items
#
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError('Stack is empty')
#
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError('Stack is empty')
#
#     def size(self):
#         return len(self.items)
#
# stack = Stack()
#
# while (stack) < 10:
from collections import deque

# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def __str__(self):
#         return ', '.join(str(item) for item in self.items)
#
#     def __len__(self):
#         return len(self.items)
#
#     def __getitem__(self, index):
#         return self.items[index]
#
#     def __setitem__(self, index, value):
#         self.items[index] = value
#
#     def __is_empty__(self):
#         return len(self.items) == 0
#
#     def __enquere__(self, item):
#         self.items.append(item)
#         return self.items
#
#     def dequere(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         raise IndexError('Quere is empty')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return 'LinkedList: []'
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next

        return 'LinkedList: [' + ', '.join(elements) + ']'

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __getitem__ (self, index):
        if index < 0 or index >= len(self):
            raise IndexError ('!!!')

        current = self.head
        for i in range(index):
            current = current.next
        return  current.data

    def __setitem__(self, index, data):
        if index < 0 or index >= len(self):
            raise IndexError('!!!')

        current = self.head
        for i in range(index):
            current = current.next

        current.data = data

    def is_empty(self):
        return  self.head is None

    def append(self):
        pass

    def prepend(self):
        pass

    def delete(self):
        pass




