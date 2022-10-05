import sys

tokens = (token for token in sys.stdin.read().split()) #generator ??

N = int(next(tokens))
Q = int(next(tokens))

lst = []
for _ in range(N):
    cur_num = int(next(tokens))
    lst.append(cur_num)

queries = []
for _ in range(Q):
    left_index = int(next(tokens))
    right_index = int(next(tokens))
    queries.append((left_index, right_index))

prefix_sums = [0]
for element in lst:
    last_prefix_sum = prefix_sums[-1]
    new_prefix_sum = last_prefix_sum + element
    prefix_sums.append(new_prefix_sum)

for left_index, right_index in queries:
    # (2,4)
    right_index_sum = prefix_sums[right_index]
    left_index_sum = prefix_sums[left_index - 1]
    print(right_index_sum - left_index_sum)