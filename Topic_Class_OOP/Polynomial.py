class Poly:
    def __init__ (self, x):
        self.tup = tuple(x)

    def add(self, p):
        add_list = []
        if len(self.tup) >= len(p.tup):
            lenght = len(self.tup)
        else: lenght = len(p.tup)  
        for j in range(0, lenght):
            if j < len(self.tup):
                val1 = self.tup[j]
            else: val1 = 0
            if j < len(p.tup):
                val2 = p.tup[j]
            else: val2 = 0
            add_list.append(val1 + val2) 
        return Poly(add_list) 

    def scalar_multiply(self, n):
        scmul_list = []
        for i in range(0, len(self.tup)):
            num = round(n * self.tup[i], 3)
            if num % 1 == 0:
                num = int(num)
            scmul_list.append(num)
        return Poly(scmul_list)

    def multiply(self, p):
        list_len = len(self.tup) + len(p.tup) - 1
        mul_list = [0] * list_len
        for i in range(0, len(self.tup)):
            for j in range(0, len(p.tup)):
                mul_list[i + j] += self.tup[i] * p.tup[j]
                
        return Poly(mul_list)
    
    def power(self, n):
        if n == 0:
            return Poly(self.tup)
        for i in range(1, n):
            res = Poly(self.tup).multiply(self)
        return res

    def diff(self):
        diff_list = []
        for i in range(0, len(self.tup)):
            if i == 0: continue
            num = round(i * self.tup[i], 3)
            if num % 1 == 0:
                num = int(num)
            diff_list.append(num)
        return Poly(diff_list)

    def integrate(self):   
        int_list = []
        for i in range(0, len(self.tup)):
            if i == 0:
                int_list.append("c")
            num = round(self.tup[i] / (i+1),3)
            if num % 1 == 0:
                num = int(num)
            int_list.append(num)
        return Poly(int_list)

    def eval(self, p):
        sum = 0
        for i in range(0,len(self.tup)):
            if i == 0: 
                sum = sum + self.tup[i]
                continue
            sum = sum + (self.tup[i] * pow(p, i))
        print(sum) 
        return sum

    def print(self):
        for a in range(0, len(self.tup)):
            if self.tup[a] == 0: continue      
            elif a == 0:
                print(f"{self.tup[a]}", end=" ")
            else:
                if a == 1:              
                    if self.tup[a] < 0:
                        print(f"- {self.tup[a]*-1}x", end=" ")
                        continue
                    print(f"+ {self.tup[a]}x", end=" ")
                else:
                    if self.tup[a] < 0:
                        print(f"- {self.tup[a]*-1}x^{a}", end=" ") 
                        continue
                    print(f"+ {self.tup[a]}x^{a}", end=" ")                  
        print("") 

    def print2(self):
        print(self.tup)          

# print("Test Case 1")
# p = Poly((1,0,-2))
# p.print()
# q = p.power(2)
# q.print()
# p.eval(3)
# r = p.add(q)
# r.print()
# r.diff().print()


# print("Test Case 2")
# p1 = Poly((1, 0, -2))
# p2 = Poly((3, 4, -5, 6))
# p1.print()  
# p2.print()  
# p_add = p1.add(p2)
# p_add.print()  
# p_scalar = p1.scalar_multiply(3)
# p_scalar.print()  
# p3 = Poly((3, 4))
# p_mul = p1.multiply(p3)
# p_mul.print()  
# p_pow0 = p1.power(0)
# p_pow0.print()  
# p_pow2 = p1.power(2)
# p_pow2.print()  
# p_pow3 = p1.power(3)
# p_pow3.print()  
# p_diff = p2.diff()
# p_diff.print()  
# p_int = p_diff.integrate()
# p_int.print()  
# val1 = p1.eval(3)
# val2 = p2.eval(2)