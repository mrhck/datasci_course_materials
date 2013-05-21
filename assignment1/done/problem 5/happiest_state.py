from __future__ import division
from collections import Counter
import codecs
import json
import sys

def get_scores(sentiment_file):
  file = open(sentiment_file)
  scores = {}  # initialize an empty dictionary
  for line in file:
    term, score = line.split("\t")
    scores[term] = int(score)
  return scores

def get_score_for_tweet(tweet, sentiments):
  words = tweet.split()
  score = 0
  for key in words:
    if key in sentiments:
      score += sentiments[key]
  return score
  

def main():
  scores = get_scores(sys.argv[1])
  tweet_file = codecs.open(sys.argv[2], 'rU')
  states = {}
  for line in tweet_file:
    json_string = json.loads(line)
    if 'text' in json_string:
      tweet = json_string['text']
      if 'place' in json_string and json_string['place'] is not None:
        place = json_string['place']
        if 'country_code' in place and place['country_code'] is not None and place['country_code'].upper() == 'US':
          if 'full_name' in place and place['full_name'] is not None:
            full_name = place['full_name']
            names = full_name.split(',')
            if len(names) == 2:
              state = names[1].strip().upper()
              if len(state) == 2:
                tweet_score = get_score_for_tweet(tweet, scores)
                if state in states:
                  states[state] += tweet_score
                else:
                  states[state] = tweet_score
  
  max_name = ''
  max_score = 0
  for key in states:
    if states[key] > max_score:
      max_name = key
      max_score = states[key]
  
  print max_name
  
if __name__ == '__main__':
    main()
