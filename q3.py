import q3lib
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_part',type=int,default=10000)
    parser.add_argument('--pop_size',type=int,default=50)
    parser.add_argument('--cross_rate',type=float,default=0.6)
    parser.add_argument('--mutation_rate',type=float,default=0.01)
    parser.add_argument('--N_generation',type=int,default=20)
    parser.add_argument('--gene',type=str,default=None)
    
    args = parser.parse_args()
    num_part = args.num_part
    pop_size = args.pop_size
    cross_rate = args.cross_rate
    mutation_rate = args.mutation_rate
    gene = args.gene
    
    q3lib.POP_SIZE = pop_size
    q3lib.CROSSOVER_RATE = cross_rate
    q3lib.MUTATION_RATE = mutation_rate
    q3lib.N_GENERATION = args.N_generation
    
    pop = q3lib.generate_pop(gene_path=gene)
    q3lib.evolution(pop,num_part)
    
    
