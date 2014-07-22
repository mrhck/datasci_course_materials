SELECT docid, sum(count) as big FROM frequency 
GROUP BY docid
HAVING big > 300