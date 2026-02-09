# 문자열 데이터 처리
use sqlclass_db;

drop table if exists string_tbl;
create table string_tbl
(char_fld char(30),
vchar_fld varchar(30),
text_fld text) ;

delete from string_tbl;

insert into string_tbl(vchar_fld)
values ('abcd'),
		('xyz'),
		('QRSTUV'),
		('qrstuv'),
		('12345');

select vchar_fld from string_tbl order by vchar_fld;

select strcmp('12345', '1234') 12345_1234,
		strcmp('abcd', 'xyz') abcd_xyz,
		strcmp('abcd', 'QRSTUV') abcd_QRSTUV,
		strcmp('qrstuv', 'QRSTUV') qrstuv_QRSTUV,
		strcmp('12345', 'xyz') 12345_xyz,
		strcmp('xyz', 'qrstuv') xyz_qrstuv;

# 문자열 조작(문자열 비교)
use sakila;
select name, name like '%y' as ends_in_y
from category;
select name, name regexp 'y$' as ends_in_y
from category;

# concat() 함수 활용

# concat() 함수 사용 2
select concat(first_name, '',last_name, 
' has been a customer since ', date(create_date)) as cust_narrative
from customer;

# insert() 함수
select insert('goodbye world',9,0, 'cruel ') as string;
							# ㄴ 추가할 위치
select insert('goodbye world',1,7, 'hello') as string;
							# 시작위치 1부터 7글자를 'hello'로 교체
# replace() 함수
select replace('goodbye world','goodbye', 'hello')as replace_str;
select substr('goodbye cruel world', 9,5);

# sign() 함수
use sqlclass_db;
drop table if exists account;
# account 테이블 생성(7장 p.188)
create table account
	(account_id int,
	acct_type varchar(20),
	balance float);

insert into account (account_id, acct_type, balance)
values (123, 'Money Market', 785),
		(456, 'Savings', 0.00),
		(789, 'Checking', -324);
select account_id, sign(balance), abs(balance) from account;

# cast()함수
select cast('2019-09-17' as date) date_field,
		cast('108:17:57' as time) time_field;
select cast('20190917153000'as datetime);
select cast('2019/09/17 15:30:00'as datetime);
# 2019-09-17 15:30:00 : mysql의 기본 표현 방법

# 날짜 생성 함수
select str_to_date('September 17, 2019', '%M %d, %Y') as return_date;

# str_dt_date(str, format) 예제
select str_to_date('04/30/2024', '%m/%d/%Y') as date1;    # 4월은 30일까지만 있음. 강의자료가 오류
select str_to_date('01,5,2024', '%d,%m,%Y') as date2;
select str_to_date('15:35:00', '%H:%i:%s') as time1;

# 현재 날짜/시간 생성
select current_date(), current_time(), current_timestamp();
# 날짜를 반환하는 시간 함수
select date_add(current_date(), interval 5 day);

# 날짜를 반환하는 시간함수 : last_day(date) 함수
select last_day('2022-08-01');
# 문자열을 반환하는 시간 함수 : dayname(date) 함수
select dayname('2022-08-01');

# extract() 함수
select extract(year from '2019-09-18 22:19:05');
# 숫자를 반환하는 시간 함수 : datediff(date1, date2) 함수
select datediff('2019-09-03', '2019-06-21');