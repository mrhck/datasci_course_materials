SELECT A.docid as row, B.docid as col, sum(A.count* B.count) as val
FROM frequency A, frequency B where A.term = B.term and  A.docid='10080_txt_crude' and B.docid='17035_txt_earn'
GROUP BY row, col;