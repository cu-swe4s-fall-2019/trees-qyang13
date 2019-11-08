#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

echo Generating random and non_random words...
# bash rand_word_generator.sh

echo Starting functional testing
run test_invalid_data_structure python insert_key_value_pairs.py --data_structure haha --dataset rand.txt --num_pairs 10000
assert_exit_code 1

run test_no_input python insert_key_value_pairs.py --data_structure hash --dataset fake.txt --num_pairs 10000
assert_exit_code 1

run test_invalid_num_pairs python insert_key_value_pairs.py --data_structure hash --dataset rand.txt --num_pairs -1
assert_exit_code 1

run test_hash_rand python insert_key_value_pairs.py --data_structure hash --dataset rand.txt --num_pairs 10000
assert_exit_code 0
assert_stdout

run test_tree_rand python insert_key_value_pairs.py --data_structure tree --dataset rand.txt --num_pairs 10000
assert_exit_code 0
assert_stdout

run test_avl_rand python insert_key_value_pairs.py --data_structure avl --dataset rand.txt --num_pairs 10000
assert_exit_code 0
assert_stdout

run test_hash_sorted python insert_key_value_pairs.py --data_structure hash --dataset non_rand.txt --num_pairs 10000
assert_exit_code 0
assert_stdout

run test_tree_sorted python insert_key_value_pairs.py --data_structure tree --dataset non_rand.txt --num_pairs 10000
assert_exit_code 0
assert_stdout

run test_avl_sorted python insert_key_value_pairs.py --data_structure avl --dataset non_rand.txt --num_pairs 10000
assert_exit_code 0
assert_stdout


rm ssshtest
