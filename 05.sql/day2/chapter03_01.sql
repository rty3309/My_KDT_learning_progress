# 3장. 쿼리 입문

use sakila;
show tables;

desc customer;

select * from language;

select language_id, name, last_update from language;

select name from language;

# select절에 추가할 수 있는 항목 - 숫자/문자열, 표현식, 함수
select language_id,
	'COMMON' language_usage,    # language_usage : 가상컬럼
	language_id * 3.14 lang_pi_value,
	upper(name) language_name    # upper : 대문자로 바꿔주는 내장함수
from language;

# 컬럼 별칭 : AS, 쓰기를 권장함
select language_id,
	'COMMON' as language_usage,
	language_id * 3.14 as lang_pi_value,
	upper(name) as language_name
from language;

# 중복 제거 : distinct 키워드
select actor_id from film_actor order by actor_id;

# distinct : 중복 제거
select distinct actor_id from film_actor order by actor_id;

# from절
# subquery(서브쿼리) : 9장 참조
select concat(cust.last_name, ', ', cust.first_name) as full_name
from
	(select first_name, last_name, email
	from customer
	where first_name = 'JESSIE'
	) as cust;
# 내부의 select(서브쿼리)를 출력해보면 from과 다르게 나옴
# 거기에서 밖의 select로 됨

# 임시테이블(Temporary table)
create temporary table actors_j
	(actor_id smallint(5),
	first_name varchar(45),
	last_name varchar(45));
desc actors_j;

insert into actors_j
	select actor_id, first_name, last_name
	from actor where last_name like 'J%';
select * from actors_j;

# 가상테이블(view) - 영구적으로 저장됨
drop view if exists cust_vw;    # view 삭제 명령어
create view cust_vw as
	select customer_id, first_name, last_name, active
	from customer;
select * from cust_vw;

# active=0인 데이터 검색
select first_name, last_name
from cust_vw where active=0;

# 테이블 연결 - join(inner join)
select *
from customer inner join rental
	on customer.customer_id=rental.customer_id;

# datetime 함수
select date('2021-07-29 09:02:03');
# time 함수
select time('2021-07-29 09:02:03');

# where절
select customer.first_name, customer.last_name,
	time(rental.rental_date) as rental_time
from customer inner join rental
	on customer.customer_id = rental.customer_id
where date(rental.rental_date) = '2005-06-14';

# 테이블 별칭 정의 - 이렇게 하기
select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from customer as c inner join rental as r    # from절에 테이블의 별칭지정
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14';

# 검색(필터링) 조건
select title
from  film
where rating='G' and rental_duration >= 7;

# where절 검색 조건 : and, or 사용
select title, rating, rental_duration
from film
where (rating='G' and rental_duration >=7) or
		(rating='PG-13' and rental_duration < 4);

# group by절과 having절
select c.first_name, c.last_name, count(*) as rental_count
from customer as c inner join rental as r
	on c.customer_id = r.customer_id
group by c.first_name, c.last_name
having count(*) >= 40
order by count(*) desc;

# order by 절
select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from  customer as c inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by c.last_name, c.first_name asc;

# 내림차순 정렬 : desc
select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from  customer as c inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by time(r.rental_date) desc;

# 컬럼의 순서(컬럼의 인덱스)를 통한 정렬
select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from  customer as c inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by 1 desc;


# 실습 3-1
select actor_id, first_name, last_name
from actor
order by last_name, first_name;

# 실습 3-2
select actor_id, first_name, last_name
from actor
where last_name='WILLIAMS' or last_name='DAVIS';

# 실습 3-3
select distinct customer_id
from rental
where date(rental_date) = '2005-07-05';

# 실습 3-4
select c.store_id, c.email, r.rental_date, r.return_date
from customer as c inner join rental as r
		on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by return_date desc;
# 그냥 return_date를 썼는데 두 테이블 중 rental에만 있어서 오류 없이 나옴
# 하지만 웬만하면 경로를 써줄 것.