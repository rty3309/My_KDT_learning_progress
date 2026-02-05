use sqlclass_db;

# books 테이블이 있으면 삭제
drop table if exists books;

# books 테이블 생성
create  table books(
	book_id int not null auto_increment,
	title varchar(50),
	publisher varchar(30),
	year varchar(10),
	price INT,
	primary key (book_id)
);

# 한 행씩 데이터 추가
insert into books(title, publisher, year, price)
values ('Operating System Concepts', 'Wiley','2003', 30700);

insert into books(title, publisher, year, price)
values ('Head First PHP and MySQL', 'OReilly', '2009', 58000);

# 여러 행의 데이터 추가
insert into books(title, publisher, year, price)
values ('C Programming Language', 'Prentice-Hall', '1989', 35000),
('Head First SQL', 'OReilly', '2007', 43000),
('Java How to Programming', 'Pearson', '2015', 65000);

select * from books;

select title, year, price from books;

select publisher from books;

select * from books where publisher='OReilly';    # 검색시 대소문자 구분없음
select * from books where publisher='oreilly';    # 그래서 둘 다 결과 같음

select * from books where cast(publisher as binary) = 'oreilly';

select * from books where price >= 30000 and price <= 50000;

update books set price=30000 where book_id=1;
select * from books;

update books
set title='Head First SQL 3rd Edition', price=45000 where year=2007;
select * from books where year=2007;

delete from books where book_id=5;
select * from books;

alter table books add author VARCHAR(50);
desc books;    # 변경된 테이블 구성 확인
select * from books;

update books set author='John Willey' where book_id=1;
update books set author='Beightley' where book_id=2;
update books set author='Brian' where book_id=3;
update books set author='Lynn' where book_id=4;
select * from books;

alter table books change author book_author varchar(60);
desc books;    # desc : 내림차순

alter table books rename column book_author to author;
desc books;

alter table books drop column author;
select * from books;
