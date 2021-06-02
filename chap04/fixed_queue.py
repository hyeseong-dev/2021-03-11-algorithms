# 고정 길이 큐 클래스 FixedQueue 구현하기

from typing import Any


class FixedQueue:

    class Empty(Exception):
        '''비어 있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외 처리'''
        pass
    
    
    class Full(Exception):
        '''가득 차 있는 FixedQueue에서 인큐할 때 내보내는 예외처리'''
        pass

    def __init__(self, capacity: int) -> None:
        '''initializing Queue'''
        self.no = 0                     # Current Number of Data
        self.front = 0                  # The Very Front of Element of Cursor 
        self.rear = 0                   # The Very Rear of Element of Cursor 
        self.capacity = capacity        # Size of Queue
        self.que = [None] * capacity    # Queue itself

    def __len__(self) -> int:
        '''return numbers of data in Queue '''
        return self.no

    def is_empty(self) -> bool:
        '''Return True or False if Queue is empty or not '''
        return self.no <= 0 

    def is_full(self) -> bool:
        '''Return True or False if Queue is full or not '''
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        '''Enque data "X"'''
        if self.is_full():
            raise FixedQueue.Full # Raise `FixedQueue.Full` Error in case of being full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
    
    def deque(self) -> Any:
        """데이터를 디큐합니다"""
        if self.is_empty():
            raise FixedQueue.Empty  # 큐가 비어 있는 경우 예외처리를 발생
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
    
    def peek(self) -> Any:
        '''Peek data in Queue(see in front of data) '''
        if self.is_empty():
            raise FixedQueue.Empty # Raise Error in case of being empty
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        '''Return Index after looking ofr value in Queue(return -1 if Can\'t find  ) '''
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:              # succeed to search
                return idx
        return -1                                   # fail to search

    def count(self, value: Any) -> bool:
        '''Return  the numbers of values in Queue'''
        c = 0
        for i in range(self.no): # linear Search in Queue data
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        """큐에 value가 포함되어 있는지 판단합니다"""
        return self.count(value)

    def clear(self) -> None:
        '''Empty all Data'''
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        '''모든 데이터를 맨 앞부터 맨 끝 순으로 출력'''
        if self.is_empty():
            print("큐가 비어있습니다.")
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) %self.capacity], end='')
            print()
    
    

