#static stack

class stack :
    def __init__ (self , size = 10) :
        self.size = size
        self.list = [None] * size
        self.top = -1

    def push(self , x) :
        if self.top >= self.size -1 :
            print('stack is full')
            return
        self.top = self.top+1
        self.list[self.top] = x
    def pop(self):
        if self.top == -1 :
            print('stack is empty')
            return
        itm = self.list[self.top ]
        self.top = self.top -1
        return itm
    def peak(self ):
        if self.top ==-1 :
            print ('stack is empty')
            return
        return self.list[self.top]

    def show_size_top(self):
        return self.top+1, (self.size - self.top-1)
    def is_empty (self):
        return self.top == -1
    def __len__(self):
        return self.top+1