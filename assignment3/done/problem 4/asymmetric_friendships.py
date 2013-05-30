import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
      record.sort();
      tuple = (record[0], record[1])
      mr.emit_intermediate(tuple, 1)

def reducer(key, list_of_values):
    if len(list_of_values) != 2:
      mr.emit(key)
      mr.emit((key[1], key[0]))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
