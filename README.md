# Logs Analysis
This project is implementing postgreSQL and Python skills to work with given data
using psycopg2 module in python

## Requirements

- Download Vagrant and VirtualBox and install them
- Download [Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm/raw/master/vagrant/Vagrantfile)
- Download Git bash for Windows (yes only if Windows) and install
- Clone or Download this repo then extract from zip
- Download [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
## Setting up VM
- Move the 'Vagrantfile' to downloaded directory
- Extract 'newsdata.zip' to downloaded directory
- Open 'Terminal' or 'Git bash for Windows' in downlaoded directory
- run `vagrant up` (This can take time if running for the first time)
- run `vagrant ssh`
## Loading Database
  Follwing commands load data from sql file into local database and connects to schema `news`:
```sh
$ psql -d news -f newsdata.sql
$ psql -d news
```
This schema contains three tables namely: authors, articles and log.
## Usage
After connecting to `news` schema, you have to create two views.
1. Create `article_views` view by typing this:
```sh
create view article_views as (select title, count(*) as views,author from articles, log where log.path like concat('%',articles.slug) group by articles.title, articles.author);
```
2. Create `err_dates` view by typing this:
```sh
create view err_dates as select date(time), round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status),2) as err_percent from log group by date;
```
Finally, open another 'Terminal' or 'Git bash for Windows' in current directory and type `vagrant ssh` and run this:
```sh
$ python3 logs_queries.py
```
