class c2dVec:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    
    def __str__(self) :
        return f"{self.i} + {self.j} "


class c3dvec(c2dVec):
    def __init__(self, i, j,k):
        super().__init__(i,j)
        self.k=k

    def __str__(self) :
        return f"{self.i} + {self.j}  + {self.k}"


v2d= c2dVec(1,3)

v3d= c3dvec(1,3,3)

print(v2d)
print(v3d)