# -*- coding:gbk -*-
import numpy as np
import q3lib
import argparse
from time import time
import pickle
def num2DNA(num):
    dna = [int(c) for c in format(num,'016b')]
    return np.array(dna)

def DNA2num(DNA):
    char_dna = ''.join([str(x) for x in DNA])
    return int(char_dna,2)

if __name__ == '__main__':
    start = time()
    good = []
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_part',type=int,default=100)
    parser.add_argument('--save_path',type=str,default=None)
    parser.add_argument('--save_size',type=int,default=1000)
    args = parser.parse_args()
    save_path = args.save_path
    save_size = args.save_size
    num_part = args.num_part
    bad = 0
    for i in range(2**16):
        result = q3lib.feedback(num_part,num2DNA(i))
        if i%100==0:
            print(f'encoded_plan:{i},profit:{result},raw_DNA:{num2DNA(i)}')
        if result>0:
            good.append({'raw_DNA':num2DNA(i),'encoded_plan':i,'profit':result})
        else:
            bad+=1
    good.sort(key=lambda x:x['profit'],reverse=True)
    good_gene = np.array([x['raw_DNA'] for x in good[0:save_size]])
    if save_path:
        with open(save_path,'wb') as f:
            pickle.dump(good_gene,f)
    end = time()
    print('positive:{},negtive{}'.format(len(good),bad))
    print('time:{}'.format(end-start))
    print(q3lib.feedback(1,good_gene[0]))