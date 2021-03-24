def search(li,f):
    a = []
    for i in range(len(li)):
        if f(li[i]):
            a.append(i)
    return a

def selection_sort(l, f):
    for i in range(len(l) - 1):
        mn = i
        for j in range(i + 1, len(l)):
            if f(l[j], l[mn]):
                mn = j
        if i < mn:
            l[i], l[mn] = l[mn], l[i]

"""
    def contains(self, v):
        for e in self.data:
            if e == v:
                return False
        return True

    def addVector(self, vector):
        for i in range(len(self.data)):
            if self.contains(self.data[i]) == True:
                raise ValueError("Vector already exists")
        self.data.append(vector)
"""