# Trees
A implementation of binary tree that is used to compare with other data structures like AVL tree and Quadratic Hash Table.

## Integration Status
![](https://travis-ci.com/cu-swe4s-fall-2019/trees-qyang13.svg?branch=master)

## Usage
To use the main program `insert_key_value_pairs.py`. You will need a list of data that has key and value separated by comma. To generate that list of data, you can run the included bash script by:
```
bash rand_word_generator.sh
```
Once you have the required text file, you can run the program by following command:
```
python insert_key_value_pairs.py --data_structure avl --dataset rand.txt --num_pairs 10000
```
The program will output the time it took to add and search for the elements, either they exist or not:
```
Insert time for avl: 0.02816486358642578
Search time for avl: 0.0041370391845703125
Search for nonexistent element time for avl: 0.0049631595611572266
```

## Benchmarking
### Sorted keys
When handling sorted keys, the hash table method implemented outperforms both tree implementations. For AVL trees, it takes longer to insert than the binary tree because it will need to re-balance once awhile. On the other hand, the binary tree takes longer to search when the key is sorted, because the tree is unbalanced that the search is almost like a linear search. But overall, when the dataset is large, and when the same dataset will be used multiple times for search, it's more efficient to use AVL.
![](plots/Sorted_100.png|width=100)
![](plots/Sorted_10000.png|width=100)

### Random keys
Similar to the discussion in the previous section, hash table outperforms the trees in every aspect. And consistently, even though AVL tree takes longer to insert new element, but because of a more balanced tree, AVL tree takes less time to search than the binary tree.
![](plots/Random_100.png| width=100)
![](plots/Random_10000.png|width=100)
