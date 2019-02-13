# instructions
# create a vector class
# that should...
# add vectors
# scale vector
# norm or len
# dot product
# override __str__ and __repr__


class Vector:

    def __init__(self, *args):
        self.v = args
        self.len = len(args)

    def __str__(self):
        return "vector is {} and dimension is {}".format(self.v, self.len)

    def __repr__(self):
        return self.__str__()

    def scale(self, scale):
        scale_vec = []
        for v in self.v:
            scale_vec.append(v * scale)
        return Vector(*scale_vec)

    def __add__(self, vec):
        add_vec = []
        for i in range(len(self.v)):
            add_vec.append(self.v[i] + vec.v[i])
        return Vector(*add_vec)

    def length(self):
        ans = 0
        for n in self.v:
            ans = ans + n**2
        return ans**(1 / 2)

    def dot(self, vec):
        dot_prod = 0
        for i in range(len(self.v)):
            dot_prod += self.v[i] * vec.v[i]
        return dot_prod


# a = Vector(2, 3)
# print(a)
# b = a.scale(2)
# print(b)
# c = a + b
# print(c)
# print(a.length())
# print(a.dot(b))
