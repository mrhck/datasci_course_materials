from __future__ import division
from collections import Counter
import codecs
import json
import sys

def main():
  tweet_file = codecs.open(sys.argv[1], 'rU')
  top_ten = {}
  for line in tweet_file:
    json_string = json.loads(line)
    if 'entities' in json_string and json_string['entities'] is not None:
      entities = json_string['entities']
      if 'hashtags' in entities and entities['hashtags'] is not None:
        hashtags = entities['hashtags']
        for hashtag in hashtags:
          if 'text' in hashtag and hashtag['text'] is not None:
            key = hashtag['text']
            if key in top_ten:
              top_ten[key] += 1
            else:
              top_ten[key] = 1
  
  keys = top_ten.keys()
  keys.sort(lambda x, y: cmp(top_ten[y], top_ten[x]))
  
  for key in keys[:10]:
    print key.encode('utf-8'), ' ', top_ten[key]
  
if __name__ == '__main__':
    main()
