import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
      mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    for v in list_of_values:
      if v[0] == "order":
        order = v
        break
    for v in list_of_values:
      if v[0] != "order":
        mr.emit(order + v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
