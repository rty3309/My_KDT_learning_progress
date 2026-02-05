use sqlclass_db;

# person 테이블이 있으면 삭제
drop table if exists person;
create table person
		(person_id smallint unsigned,
		fname varchar(20),
		lname varchar(20),
		eye_color enum('BR', 'BL', 'GR'),
		birth_date date,
		street varchar(30),
		city varchar(20),
		state varchar(20),
		country varchar(20),
		postal_code varchar(20),
		primary key (person_id));
desc person;

drop table if exists favorite_food;
create table favorite_food
		(person_id smallint unsigned,
		food varchar(20),
		primary key(person_id, food),
		foreign key(person_id) references person(person_id)
		);    # FOREIGN KEY : 다른 테이블과 연결할 컬럼 지정, person: 테이블
		
desc favorite_food;

set foreign_key_checks=0;
alter table person modify person_id smallint unsigned auto_increment;
# 제약 조건 활성화는 굳이 안 써줘도 됨
# set foreign_key_checks=1;
desc person;

insert into person
		(person_id, fname, lname, eye_color, birth_date)
		values (null, 'William', 'Turner', 'BR', '1972-05-27');
select * from person;

select person_id, fname, lname, birth_date from person;
select person_id, fname, lname, birth_date
from person where lname='turner';

insert into favorite_food (person_id, food) values (1,'pizza');
insert into favorite_food (person_id, food) values (1, 'cookies');
insert into favorite_food (person_id, food) values (2, 'nachos');
# nachos는 2 값을 넣어서 오류 뜸

insert into favorite_food (person_id, food) values (1, 'nachos');

select food from favorite_food
where person_id=1 order by food asc;    # 오름차순

select food from favorite_food
where person_id=1 order by food desc;    # 내림차순

insert into person
(person_id, fname, lname, eye_color, birth_date,
street, city, state, country, postal_code)
values(null, 'Susan','Smith','BL', '1975-11-02',
'23 Maple St.', 'Arlington', 'VA', 'USA', '20220');

select person_id, fname, lname, birth_date from person;

update person
set street='1225 Tremon St.',
	city='Boston',
	state='Ma',
	country='USA',
	postal_code='02138'
where person_id=1;
select * from person;

insert into favorite_food (person_id, food) values(3, 'lasagna');

select * from favorite_food;

update person set birth_date = str_to_date('DEC-21-1980', '%b-%d-%Y')
where person_id=1;
select * from person;

delete from person where person_id=2;
select * from person;

set foreign_key_checks=0;    # 제약 조건 비활성화
delete from person;    # person 테이블의 데이터만 삭제
select * from person;