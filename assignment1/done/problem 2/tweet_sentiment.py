import sys
import codecs
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    
def get_scores(sentiment_file):
  file = open(sentiment_file)
  scores = {}  # initialize an empty dictionary
  for line in file:
    term, score = line.split("\t")
    scores[term] = int(score)
  return scores
    
  
def main():
  scores = get_scores(sys.argv[1])
  tweet_file = codecs.open(sys.argv[2], 'rU')
  for line in tweet_file:
    sentiment = 0
    json_string = json.loads(line)
    if 'text' in json_string:
      tweet = json_string['text']
      words = tweet.split()
      for key in words:
        if key in scores:
          sentiment += scores[key]
      print sentiment
  
if __name__ == '__main__':
    main()
