SELECT A.row_num as row, B.col_num as col, sum(A.value * B.value) as val
FROM A, B where A.col_num = B.row_num and  A.row_num=2 and B.col_num=3
GROUP BY A.row_num, B.col_num;