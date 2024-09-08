# -*- coding: gbk -*-
from case_dict import case
import numpy as np
import copy
import random
CROSSOVER_RATE = 0.6
MUTATION_RATE = 0.01
cost=0
income=0
class part():
    def __init__(self,idx,fail_rate):
        self.idx = idx
        if np.random.rand()<fail_rate:
            self.ok = False
        else:
            self.ok=True
        self.tested = False
    def test(self):
        self.tested = True
        return self.ok

        
class half_product12():
    def __init__(self,part1,part2,part3,fail_rate):
        self.part1 = copy.deepcopy(part1)
        self.part2 = copy.deepcopy(part2)
        self.part3 = copy.deepcopy(part3)
        self.parts = (self.part1,self.part2,self.part3)
        if part1.ok and part2.ok and part3.ok:
            self.ok = False if np.random.rand()<=fail_rate else True
        else:
            self.ok=False
    def test(self):
        return self.ok

class half_product3():
    def __init__(self,part1,part2,fail_rate):
        self.part1 = copy.deepcopy(part1)
        self.part2 = copy.deepcopy(part2)
        self.parts = (self.part1,self.part2)
        if part1.ok and part2.ok:
            self.ok = False if np.random.rand()<=fail_rate else True
        else:
            self.ok=False
        self.tested = False
    def test(self):
        self.tested = True
        return self.ok

class product():
    def __init__(self,half1,half2,half3,fail_rate):
        self.half1 = copy.deepcopy(half1)
        self.half2 = copy.deepcopy(half2)
        self.half3 = copy.deepcopy(half3)
        self.halfs = [self.half1,self.half2,self.half3]
        if half1.ok and half2.ok and half3.ok:
            self.ok = False if np.random.rand()<=fail_rate else True
        else:
            self.ok = False
    def test(self):
        return self.ok
        
def makehalf(lens,parts,halfs,ths,dhs):

    global cost,income,case
    empty = lambda l:0 in l
    while(not empty(lens)):
        #�Ӵ��������������װ����Ʒ
        for i,(a,b,c) in enumerate(((1,2,3),(4,5,6),(7,8,None)),1):#װ����Ʒ
            idx1 = random.randint(0,lens[a-1]-1)
            idx2 = random.randint(0,lens[b-1]-1)
            if c:
                idx3 = random.randint(0,lens[c-1]-1)
            cost += case['h{}'.format(i)]['cost']
            if c:
                half = half_product12(parts[a-1][idx1],parts[b-1][idx2],parts[c-1][idx3],case['h{}'.format(i)]['fail'])
                lens[a-1]-=1
                lens[b-1]-=1
                lens[c-1]-=1
                del parts[a-1][idx1],parts[b-1][idx2],parts[c-1][idx3]
            else:
                half = half_product3(parts[a-1][idx1],parts[b-1][idx2],case['h{}'.format(i)]['fail'])
                lens[a-1]-=1
                lens[b-1]-=1
                del parts[a-1][idx1],parts[b-1][idx2]
            
            if ths[i-1]:#�������������Ʒ
                cost += case['h{}'.format(i)]['test']
                if half.test():
                    halfs[i-1].append(copy.deepcopy(half))
                elif dhs[i-1]:
                    cost += case['h{}'.format(i)]['disassemble']
                    #��������Ʒ���õ���������ܲ���
                    for part in half.parts:
                        if not part.tested:#û���һ��Ҫ��
                            cost += case['p{}'.format(part.idx)]['test']
                            if part.test():
                                parts[part.idx-1].append(copy.deepcopy(part))
                            else:
                                pass
                        else:#�����ֱ�ӻ���
                            parts[part.idx-1].append(copy.deepcopy(part))
                else:
                    pass#ʲô���������������ϸ�İ��Ʒ 
            else:#����ֱ�ӷ�����Ʒ��
                halfs[i-1].append(copy.deepcopy(half))
        
            

    pass
def disassemble_half(parts,half):

    for part in half.parts:
        if not part.tested:#û���һ��Ҫ��
            cost += case['p{}'.format(part.idx)]['test']
            if part.test():
                parts[part.idx-1].append(copy.deepcopy(part))
            else:
                pass
        else:#�����ֱ�ӻ���
            parts[part.idx-1].append(copy.deepcopy(part))

def feedback(num_part,DNA):
    global cost,income
    cost=0
    income=0
    global fail_rate,case

    #����16������
    tp1,tp2,tp3,tp4,tp5,tp6,tp7,tp8,th1,th2,th3,dh1,dh2,dh3,tf,df = DNA
    tps = (tp1,tp2,tp3,tp4,tp5,tp6,tp7,tp8)
    ths = (th1,th2,th3)
    dhs = (dh1,dh2,dh3)
    
    failure_in_market=0

    part1s=[]
    part2s=[]
    part3s=[]
    part4s=[]
    part5s=[]
    part6s=[]
    part7s=[]
    part8s=[]
    parts=[
        part1s,
        part2s,
        part3s,
        part4s,
        part5s,
        part6s,
        part7s,
        part8s,
    ]
    for _ in range(num_part):
        for i in range(8):
            p = part(idx=i+1,fail_rate=case[f'p{i+1}']['fail'])
            cost+=case[f'p{i+1}']['cost']
            if tps[i]:
                cost += case[f'p{i+1}']['test']
                if p.test():
                    parts[i].append(copy.deepcopy(p))
            else:
                parts[i].append(copy.deepcopy(p))
    
    lens_parts = [len(part_) for part_ in parts]#������0��ʼ
    half1=[]
    half2=[]
    half3=[]
    halfs = [half1,half2,half3]
    updata_len_h = lambda:[len(half_) for half_ in halfs]
    makehalf(lens_parts,parts,halfs,ths,dhs)
    lens_halfs = updata_len_h()
    while(not (0 in lens_halfs)):
        idx1 = random.randint(0,lens_halfs[0]-1)
        idx2 = random.randint(0,lens_halfs[1]-1)
        idx3 = random.randint(0,lens_halfs[2]-1)
        cost += case['f']['cost']
        assemble_product = product(half1[idx1],half2[idx2],half3[idx3],case['f']['fail'])
        if tf:
            cost += case['f']['test']
            if assemble_product.test():
                income +=case['f']['market']
            elif df:
                cost += case['f']['disassemble']
                for i,half in enumerate(assemble_product.halfs):
                    cost += case['h{}'.format(i+1)]['test']
                    if half.test():
                        halfs[i].append(copy.deepcopy(half))
                    elif dhs[i]:
                        cost += case['h{}'.format(i+1)]['disassemble']
                        disassemble_half(parts,half)
                    else:#�����Ʒ
                        pass
            else:
                pass#����Ʒ
        else:
            income += case['f']['market']
            if assemble_product.test():
                pass#��ͨ���г���Ʒ�ϸ�
            else:
                income -= case['f']['market']
                cost += case['f']['adjustment']
                if df:
                    cost += case['f']['disassemble']
                    for i,half in enumerate(assemble_product.halfs):
                        cost += case['h{}'.format(i+1)]['test']
                        if half.test():
                            halfs[i].append(copy.deepcopy(half))
                        elif dhs[i]:
                            cost += case['h{}'.format(i+1)]['disassemble']
                            disassemble_half(parts,half)
                        else:#�����Ʒ
                            pass
                else:
                    pass
        makehalf(lens_parts,parts,halfs,ths,dhs)
        lens_halfs = updata_len_h()
        return income-cost
            
DNA_SIZE = 16
POP_SIZE = 50
def translateDNA(pop):
    coin = random.randint(0,1)
    return pop[:,0:DNA_SIZE] if coin else pop[:,DNA_SIZE:]#���ѡȡһ��Ⱦɫ����Ϊ���뷽��
def crossover_and_mutation(pop, CROSSOVER_RATE=0.8):
    new_pop = []
    for father in pop:  # ������Ⱥ�е�ÿһ�����壬���ø�����Ϊ����
        child = father.copy()  # �����ȵõ����׵�ȫ����������һ�������ƴ�����Щ0��1��Ϊ����
        if np.random.rand() < CROSSOVER_RATE:  # �����Ӵ�ʱ���Ǳ�Ȼ�������棬������һ���ĸ��ʷ�������
            mother = pop[np.random.randint(POP_SIZE)].copy()  # ����Ⱥ��ѡ����һ�����壬�����ø�����Ϊĸ��
            cross_points = np.random.randint(low=0, high=DNA_SIZE * 2)  # �����������ĵ�
            child[cross_points:] = mother[cross_points:]  # ���ӵõ�λ�ڽ������ĸ�׵Ļ���
        mutation(child)  # ÿ�������һ���Ļ��ʷ�������
        new_pop.append(child)
    return new_pop
def mutation(child, MUTATION_RATE=0.003):
    if np.random.rand() < MUTATION_RATE:  # ��MUTATION_RATE�ĸ��ʽ��б���
        mutate_point = np.random.randint(0, DNA_SIZE)  # �������һ��ʵ��������Ҫ��������λ��
        child[mutate_point] = child[mutate_point] ^ 1  # �������Ķ�����Ϊ��ת
def select(pop, fitness):  # nature selection wrt pop's fitness
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True,#������Ȼѡ�������
                           p=(fitness) / (fitness.sum()))#�������򻯣�ֵԽ����Խ���ױ���ȡ
    return pop[idx]

def get_fitness(pop):
    return np.random.rand(pop.shape[0])

def evolution(pop,N_GENERATION):
    for n in range(N_GENERATION):
        pop = np.array(crossover_and_mutation(pop,CROSSOVER_RATE))
        fitness = get_fitness(pop)
        pop = select(pop,fitness)
    pop = translateDNA(pop.astype(np.float64))
    return pop.sum(axis=0)/pop.shape[0]

if __name__ == '__main__':
    dna = np.random.randint(2,size=(DNA_SIZE,))
    result = feedback(100,dna)
    print(result)
