from ctypes import py_object

from exceptions import ArrayInitialisationException
from exceptions import IteratorException

class Array:
    def __init__(self, size, value=None):
        if (size <= 0):
            raise ArrayInitialisationException()
        else:            
            self.elements = (py_object * size)()
             
            if value is not None:
                self.clear(value)
            
    
    def __len__(self):
        return len(self.elements)
    
    
    def __getitem__(self, index):
        return self.elements[index]
    
    
    def __setitem__(self, index, value):
        self.elements[index] = value
        return self.elements
    
    
    def clear(self, value):
        if len(self) is 1:
            self.elements[0] = value
        
        else:
            for i in range(0, len(self) - 1):
                self.elements[i] = value
            
            
    def __iter__(self):
        self.next = -1
        return self
    
    
    def __next__(self):
        if self.next < len(self) - 1:
            self.next += 1
            return self.elements[self.next]
        else:
            raise IteratorException 
    
    
    def __str__(self):
        s = "["
        
        for i in range(0, self.length() - 2):
            s += str(self.elements[i]) + " "
        s += str(self.elements[self.length() - 1])
        
        return s