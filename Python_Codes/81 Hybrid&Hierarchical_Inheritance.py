
# Hybrid inheritance means combination of any two type of inheritance


class A:
    def method_A(self):
        print("Method in class A")

# B and C are the Hierarchical Inheritance
class B(A):
    def method_B(self):
        print("Method in class B")

class C(A):
    def method_C(self):
        print("Method in class C")

# Hybrid: Combining Multiple (D) and Hierarchical Inheritance
class D(B, C):
    def method_D(self):
        print("Method in class D")

# Object of Class D
obj = D()
obj.method_A()  # From class A
obj.method_B()  # From class B
obj.method_C()  # From class C
obj.method_D()  # From class D


# Hierarchical inheritance

# class C and B follows Class A it is the example of herirachy inheirtance

class AA:
    pass
class BB(AA):
    pass
class CC(AA):
    pass
                           
class ZZ(BB):                                           
    pass
class XX(BB):
    pass

class AB(CC):
    pass
class BC(CC):
    pass



#         AA
#        /  \
#      BB    CC
#     /  \   /  \
#   ZZ   XX AB  BC


# Author : Jenis Surani
# Topic  : Hybrid & Hierarchical_Inheritance
# Date   : 24/02/2025