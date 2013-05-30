import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    terms = {}
    value = record[0]
    keys = record[1]
    words = keys.split()
    for word in words:
      terms[word] = value;
    for word in terms.keys():
      mr.emit_intermediate(word, value)

def reducer(key, list_of_values):
    total = []
    for v in list_of_values:
      total.append(v)
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
