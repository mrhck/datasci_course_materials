from __future__ import division
from collections import Counter
import codecs
import json
import sys

def main():
  tweet_file = codecs.open(sys.argv[1], 'rU')
  terms = {}
  total_count = 0
  for line in tweet_file:
    json_string = json.loads(line)
    if 'text' in json_string:
      tweet = json_string['text']
      words = tweet.split()
      for key in words:
        if key in terms:
          terms[key] += 1
        else:
          terms[key] = 1
        total_count += 1
  
  for key in terms:
    print key.encode('utf-8') , ' ', terms[key] / total_count 
  
if __name__ == '__main__':
    main()