use sakila;

# 그룹화의 개념
select customer_id, count(*) as freq
from rental
group by customer_id;

# 가장 많이 대여한 회원 찾기
select customer_id, count(*) as freq
from rental
group by customer_id
order by 2 desc;    # order by freq desc; 도 가능

# 잘못된 필터링 사용
select customer_id, count(*)
from rental
where count(*) > 40
group by customer_id;
# where 와 having의 역할 혼동으로 에러 발생

# 그룹 연산 필터링
select customer_id, count(*)
from rental
group by customer_id
having count(*) >=40;

# 집계함수
select max(amount) as max_amt,
	min(amount) as min_amt,
	avg(amount) as avg_amt,
	sum(amount) as tot_amt,
	count(*) as num_payments
from payment;

# 명시적 그룹과 암시적 그룹
select customer_id,
	max(amount) as max_amt,
	min(amount) as min_amt,
	avg(amount) as avg_amt,
	sum(amount) as tot_amt,
	count(*) as num_payments
from payment
group by customer_id;

# 집계함수 적용 결과 비교
# amount 컬럼의 전체 데이터의 평균값 리턴
select avg(amount) as avg_amt
from payment;
# customer_id 그룹별 평균값 리턴
select customer_id, avg(amount) as avg_amt
from payment
group by customer_id;

# 고유한 값 계산
select count(customer_id) as num_rows,
		count(distinct customer_id) as num_customers
from payment;

# 표현식 사용(11p)
select max(datediff(return_date, rental_date)) from rental;
select avg(datediff(return_date, rental_date)) from rental;


# 다중 컬럼 그룹화(15p)
select fa.actor_id, f.rating, count(*)
from film_actor as fa
	inner join film as f
	on fa.film_id = f.film_id
group by fa.actor_id, f.rating
order by 1,2;
# 1) actor_id로 그룹화
# 2) actor_id 내부에서 등급별 그룹화

# 그룹 생성
select extract(year from rental_date) as year,
		count(*) as how_many
from rental
group by extract(year from rental_date);

# 롤업 생성
select fa.actor_id, f.rating, count(*)
from film_actor as fa
	inner join film as f
	on fa.film_id = f.film_id
group by fa.actor_id, f.rating with rollup
order by 1,2;

# 그룹 필터조건
select fa.actor_id, f.rating, count(*)
from film_actor fa
	inner join film f
	on fa.film_id=f.film_id
where f.rating in ('G', 'PG')
group by fa.actor_id, f.rating
having count(*) > 9;

# 학습 점검
select customer_id, count(*), sum(amount)
from payment
group by customer_id;