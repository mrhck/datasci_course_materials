import MapReduce
import sys

mr = MapReduce.MapReduce()

# A = L x M
# B = M x N
L = 5
M = 5
N = 5
# =============================
# Do not modify above this line

def mapper(record):
  if record[0] == 'a':
    for k in range(0, N):
      mr.emit_intermediate((record[1], k), ('a', record[2], record[3]))
  if record[0] == 'b':
    for i in range(0, L):
      mr.emit_intermediate((i, record[2]), ('b', record[1], record[3]))

def reducer(key, list_of_values):
  dict = {}
  for val in list_of_values:
    dict[(val[0], val[1])] = val[2]
  sum = 0
  elem_a = 0
  elem_b = 0
  for i in range(0, M):
    a_key = ('a', i)
    b_key = ('b', i)
    if a_key in dict:
      elem_a = dict[a_key]
    else:
      elem_a = 0
    if b_key in dict:
      elem_b = dict[b_key]
    else:
      elem_b = 0
    sum += elem_a * elem_b
  
  mr.emit(key + (sum,))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
