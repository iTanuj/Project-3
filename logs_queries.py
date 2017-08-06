#!/usr/bin/python3
import psycopg2
DBNAME = "news"


# executes the passed query and return it's result
def result_of(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    rslt = c.fetchall()
    db.close()
    return rslt


# prints passed result formatted according to the query
# usage: dq for double qoutes signal, sfx for apt suffix
def show(dq, result, sfx):
    qou = '"' if dq else ''
    for row in result:
        print('\t{0}{1}{0} --- {2} {3}'.format(qou, row[0], row[1], sfx))
    print()


# query for 3 most popular articles
q1 = "select * from article_views order by views desc limit 3;"


# query for popularity of each author in order of their article views
q2 = '''select authors.name, sum(article_views.views) as views
from article_views, authors where article_views.author=authors.id
group by authors.name order by views desc;'''


# query for showing dates when more than 1% requests led to errors
q3 = '''select * from err_dates where err_percent > 1.0
order by err_percent desc;'''


# finally calling execution and printing all queries one-by-one

print("The most popular three articles of all time are:\n")
show(True, result_of(q1), 'views')

print("The most popular article authors of all time are:\n")
show(False, result_of(q2), 'views')

print("Days, when more than 1% of requests led to errors are:\n")
show(False, result_of(q3), '\b% errors')
