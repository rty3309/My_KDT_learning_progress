use sakila;

# customer 테이블과 actor 테이블 union all 연산 수행
select 'cust' as type1, c.first_name, c.last_name
from customer c
union all
select 'ACTR' as type1, a.first_name, a.last_name
from actor a;

select count(first_name) from customer;
select count(first_name) from actor;

# actor 테이블에 union all 연산 수행
select 'actr1' as type, a.first_name, a.last_name
from actor a
union all
select 'actr2' as type, a.first_name, a.last_name
from actor a;

# customer 테이블과 actor 테이블에서
select 'cust' as type1, c.first_name, c.last_name
from customer c
where c.first_name like 'J%' and c.last_name like 'D%'
union all
select 'act' as type1, a.first_name, a.last_name
from actor a
where a.first_name like 'J%' and a.last_name like 'D%';

# union : 중복 데이터 제거
select c.first_name, c.last_name
from customer c
where c.first_name like 'J%' and c.last_name like 'D%'
union
select a.first_name, a.last_name
from actor a
where a.first_name like 'J%' and a.last_name like 'D%';

# intersect 연산자 : 교집합
select c.first_name, c.last_name
from customer c
where c.first_name like 'D%' and c.last_name like 'T%'
intersect
select a.first_name, a.last_name
from actor a
where a.first_name like 'D%' and a.last_name like 'T%';

# intersect 연산자
# inner join 연산자를 이용하여 공통 항목 검색
select c.first_name, c.last_name
from customer as c inner join actor as a
on (c.first_name = a.first_name) and (c.last_name= a.last_name);

# customer 테이블과 actor 테이블의 교집합
select c.first_name, c.last_name
from customer c
where c.first_name like 'J%' and c.last_name like 'D%'
intersect
select a.first_name, a.last_name
from actor a
where a.first_name like 'J%' and a.last_name like 'D%';

# EXCEPT 연산자
select a.first_name, a.last_name
from actor a
where a.first_name like 'J%' and a.last_name like 'D%'
except
select c.first_name, c.last_name
from customer c
where c.first_name like 'J%' and c.last_name like 'D%';

# 집합 연산 규칙
# 복합 쿼리의 결과 정렬
select a.first_name fname, a.last_name lname
from actor a
where a.first_name like 'J%' and a.last_name like 'D%'
union all
select c.first_name, c.last_name
from customer c
where c.first_name like 'J%' and c.last_name like 'D%'
order by lname, fname;