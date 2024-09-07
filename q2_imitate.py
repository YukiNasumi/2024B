import random
import numpy as np
import copy
cases = [
    {"p1_rate": 0.1, "p1_cost": 4, "p1_test": 2,
     "p2_rate": 0.1, "p2_cost": 18, "p2_test": 3, 
     "product_rate":0.1,"assemble": 6, "product_test": 3,"market": 56, 
     "adjustment_loss": 6, "disassemble_cost": 5},

]
class part():
    def __init__(self,fail_rate):
        if np.random.rand()<fail_rate:
            self.ok = False
        else:
            self.ok=True
        self.exist = True
    def test(self):
        return self.ok
    def dump(self):
        self.exist=False
        
class product():
    def __init__(self,part1,part2,fail_rate):
        self.part1 = part1
        self.part2 = part2
        if part1 and part2:
            self.ok = False if np.random.rand()<=fail_rate else True
        else:
            self.ok=False
    def test(self):
        return self.part1.ok and self.part2.ok and self.ok
    
def decision(num_part,case,*,test1,test2,test_product,disassemble):
    failure_in_market=0

    cost=0
    income=0
    part1s=[]
    part2s=[]
    #购买配件12
    for _ in range(num_part):
        p1 = part(case['p1_rate'])
        p2 = part(case['p2_rate'])
        cost = cost + case['p1_cost']
        cost = cost + case['p2_cost']
        
        if test1:
            cost = cost + case['p1_test']
            if p1.test():
                part1s.append(copy.copy(p1))
            else:
                p1.dump()
        else:
            part1s.append(copy.copy(p1))
        if test2:
            cost = cost+case['p2_test']
            if p2.test():
                part2s.append(copy.copy(p2))
            else:
                p2.dump()
        else:
            part2s.append(copy.copy(p2))
            
    #现在开始装配,在part1s和part2s中随机选取一个零件
    len1,len2 = len(part1s),len(part2s)
    while len1 and len2:
        idx1 = random.randint(0,len1-1)
        idx2 = random.randint(0,len2-1)
        cost = cost + case['assemble']
        assembled_product = product(copy.copy(part1s[idx1]),copy.copy(part2s[idx2]),fail_rate=case['product_rate'])
        len1 = len1-1
        len2 = len2-1
        del part1s[idx1]
        del part2s[idx2]
    
    
        if test_product:
            cost += case['product_test']
            if assembled_product.test():
                income = income + case['market']
            elif disassemble:
                cost = cost+case['disassemble_cost']
            
                part1s.append(copy.copy(assembled_product.part1))
                len1=len1+1
                part2s.append(copy.copy(assembled_product.part2))
                len2 = len2+1
                del assembled_product
        else:
            income = income + case['market']
            if not assembled_product.test():#如果不合格，则需要退货
                failure_in_market = failure_in_market + 1
                print(failure_in_market)
                income = income - case['market']
                cost = cost + case['adjustment_loss']
                if disassemble:       
                    cost = cost+case['disassemble_cost']
                    part1s.append(copy.copy(assembled_product.part1))
                    len1=len1+1
                    part2s.append(copy.copy(assembled_product.part2))
                    len2 = len2+1
                    del assembled_product
                
    return income - cost,failure_in_market

to_bi = lambda i:format(i,'04b')
plans=[{'test1':to_bi(i)[0],'test2':to_bi(i)[1],'test_product':to_bi(i)[2],'disassemble':to_bi(i)[3]} for i in range(16) ]
for case in cases:
    """p1_rate = case['p1_rate']
    p1_cost = case['p1_cost']
    p1_test = case['p1_test']
    p2_rate,p2_cost,p2_test = case["p2_rate"], case["p2_cost"], case["p2_test"]
    product_rate, assemble, product_test, market =case["product_rate"],case["assemble"], case["product_test"],case["market"]
    adjustment_loss, disassemble_cost = case["adjustment_loss"], case["disassemble_cost"]"""
    for plan in plans:
        print('plan:',plan)
        profit,failure = decision(num_part=10,case=case,**plan)
        print('profit:'+str(profit),'failed product in market:{}'.format(failure))