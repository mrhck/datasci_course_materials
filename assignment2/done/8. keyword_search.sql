CREATE VIEW keyword_search as
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

SELECT A.docid as row, B.docid as col, sum(A.count* B.count) as val
FROM keyword_search A, keyword_search B where A.term = B.term and  A.docid='q'
GROUP BY row, col
ORDER BY val DESC;