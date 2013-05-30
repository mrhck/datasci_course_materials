import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
      mr.emit_intermediate(record[0], 1)

def reducer(key, list_of_values):
    total = 0
    for v in list_of_values:
      total += 1
    mr.emit((key, total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
