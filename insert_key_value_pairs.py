import sys
import time
import argparse as ap
import matplotlib
import matplotlib.pyplot as plt
import importlib
import binary_tree as bt
matplotlib.use('Agg')
sys.path.insert(1, "./hash-tables-qyang13/")
sys.path.insert(1, "./avl_tree/")
avl = importlib.import_module("avl")
ht = importlib.import_module("hash_tables")
hf = importlib.import_module("hash_functions")

class Benchmark:
    def __init__(self, struct = None, data = None, num = None):
        self.struct = struct
        if struct == 'hash':
            # Initialize a hash table that 5 times the size of number of insertion
            # to speed up the hash
            self.temp_hash = ht.QuadraticProbing(num*5, hf.h_sedgwicks)
        elif struct == 'tree':
            self.temp_tree = None
        elif struct == 'avl':
            self.temp_avl = avl.AVL()
        self.data = data
        self.num = num

    def time_insert(self):
        insert_start = time.time()
        i = 0
        # Initialize a hash table that 5 times the size of number of insertion
        # to speed up the hash
        for l in open(self.data):
            if i >= self.num:
                break
            else:
                i += 1
                pair = l.rstrip().split(",")
                if self.struct == 'hash':
                    self.temp_hash.add(pair[0], pair[1])
                elif self.struct == 'tree':
                    self.temp_tree = bt.insert(self.temp_tree, pair[0], pair[1])
                elif self.struct == 'avl':
                    self.temp_avl.insert(pair)
        insert_end = time.time()
        i_time = str(insert_end - insert_start)
        return i_time

    def time_search(self):
        search_start = time.time()
        i = 0
        # search for the same set of data that was inserted
        for l in open(self.data):
            if i >= self.num:
                break
            else:
                i += 1
                pair = l.rstrip().split(",")
                if self.struct == 'hash':
                    v = self.temp_hash.search(pair[0])
                elif self.struct == 'tree':
                    v = bt.search(self.temp_tree, pair[0])
                elif self.struct == 'avl':
                    v = self.temp_avl.find(pair).key[1]
        search_end = time.time()
        s_time = str(search_end - search_start)
        return s_time


    def time_search_not_exist(self):
        search_ne_start = time.time()
        # The non-existent key, all keys are integers so any string would work
        ne_key = 'ne'
        # search for the same set of data that was inserted
        for l in range(self.num):
                if self.struct == 'hash':
                    v = self.temp_hash.search(ne_key)
                elif self.struct == 'tree':
                    v = bt.search(self.temp_tree, ne_key)
                elif self.struct == 'avl':
                    v = self.temp_avl.find(['ne','ne'])
        search_ne_end = time.time()
        s_ne_time = str(search_ne_end - search_ne_start)
        return s_ne_time


def parse_args():
    '''    Argument Parser    '''
    parser = ap.ArgumentParser(description="correct way to parse",
                               prog='Insert key value pairs')

    parser.add_argument('--data_structure',
                        type=str,
                        help="Specify which data structure to use",
                        required=True)

    parser.add_argument('--dataset',
                        type=str,
                        help="Specify which dataset to use",
                        required=True)

    parser.add_argument('--num_pairs',
                        type=int,
                        help="Specify how many key/value pairs to use",
                        required=True)

    return parser.parse_args()


def main():
    args = parse_args()
    init = Benchmark(args.data_structure, args.dataset, args.num_pairs)
    insert_time = init.time_insert()
    search_time = init.time_search()
    search_not_exist_time = init.time_search_not_exist()

    print('Insert time for '+args.data_structure+': '+insert_time)
    print('Search time for '+args.data_structure+': '+search_time)
    print('Search for nonexistent element time for '
          +args.data_structure+': '+search_not_exist_time)


if __name__ == '__main__':
    main()
