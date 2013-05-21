SELECT count(distinct(docid))
FROM (SELECT docid
FROM frequency
WHERE docid IN (SELECT docid FROM frequency WHERE term='transactions') and docid IN (SELECT docid FROM frequency WHERE term='world'))