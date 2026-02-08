use sakila;

# 조건 유형
# 동등 조건
select c.email, r.rental_date
from customer as c
	inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14';

# 부등 조건
select c.email, r.rental_date
from customer as c
	inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) != '2005-06-14';

# 동등/부등 조건 사용 예
# 8p인데 실제 실행하지 말 것! 그래서 페이지 공부만 할 것

# 범위 조건
# 해당 식이 특정 범위 내에 있는지 확인
select customer_id, rental_date
from rental
where rental_date < '2005-05-25';

# 해당 날짜만 검색
select customer_id, rental_date
from rental
where rental_date <= '2005-06-16'
	and rental_date >= '2005-06-14';
# rental_date는 datetime속성으로 날짜와 시간을 같이 포함해 2005-06-16은 포함되지 않음(시간정보 때문)

# 범위 조건 10p - date() 사용하여 정확한 날짜만 추출
select customer_id, rental_date
from rental
where date(rental_date) <= '2005-06-16' and
	date(rental_date) >= '2005-06-14';


# between 연산자
select customer_id, rental_date
from rental
where date(rental_date) between '2005-06-14' and '2005-06-16';
# 하한값, 상한값의 위치가 바뀌면(06-16이 먼저 적히면) 결과 출력 없음

# 숫자 범위 사용
select customer_id, payment_date, amount
from payment
where amount between 10.0 and 11.99;    # 출력값 보면 상한값 범위에 포함됨

# 문자열 범위 지정
select last_name, first_name
from customer
where last_name between 'FA' and 'FRB';

# 멤버십 조건
# or 또는 in()연산
select title, rating
from film
where rating='G' or rating='PG';
# 위를 이렇게 쓰기 가능
select title, rating
from film
where rating in ('G', 'PG');

# 서브 쿼리 사용
select title, rating from film where title like '%PET%';

select title, rating
from film
where rating in (select rating from film where title like '%PET%');

# not in 사용
select title, rating
from film
where rating not in('PG-13','R','NC-17');

# 일치 조건 : 와일드 카드 사용시 like 연산자 사용, 부분 일치 검색
# 두번째 위치에'A' 네번째 위치에 'T'를 포함하며 마지막은 'S'로 끝나는 문자열
select last_name, first_name
from customer
where last_name like '_A_T%S';
# last_name이 'Q'로 시작하거나 'Y'로 시작하는 ㄱ객 이름 검색
select last_name, first_name
from customer
where last_name like 'Q%' or last_name like 'Y%';
# 두번째가 훨씬 더 많이 쓰이는 예제(첫번째는 쓰기 어려우니까)

# 정규 표현식 사용
select last_name, first_name
from customer
where last_name regexp '^[QY]';

# Null
select rental_id, customer_id, return_date
from rental
where return_date is null;

# is not null
select rental_id, customer_id, return_date
from rental
where return_date is not null;

# null 과 조건 조합
select rental_id, customer_id, return_date
from rental
where return_date is null
or (date(return_date) not between '2005-05-01' and '2005-08-31');

# 실습 서브셋 조건설정
select payment_id, customer_id, amount, date(payment_date) as payment_date
from payment
where (payment_id between 101 and 120);

# 실습 4-1
select payment_id, customer_id, amount, date(payment_date) payment_date
from payment
where (payment_id between 101 and 120)
and customer_id != 5 and (amount > 8 or date(payment_date) = '2005-08-23');

# 실습 4-2
select payment_id, customer_id, amount, date(payment_date) payment_date
from payment
where (payment_id between 101 and 120)
and customer_id = 5 and not (amount > 6 or date(payment_date)='2005-06-19');

# 실습 4-3
select amount from payment
where amount in (1.98, 7.98, 9.98);