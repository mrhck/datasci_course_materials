import codecs
import json
import sys

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
  new_terms = {}
  for line in tweet_file:
    sentiment = 0
    tweet_new_terms = []
    json_string = json.loads(line)
    if 'text' in json_string:
      tweet = json_string['text']
      words = tweet.split()
      for key in words:
        if key in scores:
          sentiment += scores[key]
        else:
          if not key in tweet_new_terms:
            tweet_new_terms.append(key)
      for key in tweet_new_terms:
          if key in new_terms:
            new_terms[key] += sentiment
          else:
            new_terms[key] = sentiment   
    
    for key in tweet_new_terms:
      print key.encode('utf-8') , ' ', new_terms[key]
  
if __name__ == '__main__':
    main()
