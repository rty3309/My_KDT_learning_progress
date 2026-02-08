use sqlclass_db;

# SQL 과제 2
# KDT 12기 이재헌

# 1) 1960년에 노벨상 물리학상 또는 노벨 평화상을 수상한 사람의 정보를 출력
select year, category, fullname from nobel where (year=1960) and (category = 'Peace' or category = 'physics');

# 2) Albert Einstein이 수상한 연도와 수상 분야(category), 출생대륙, 출생국가를 출력
select year, category, prize_amount, birth_continent, birth_country from nobel
where fullname = 'Albert Einstein'

# 3) 1910년 부터 2010년까지 노벨 평화상 수상자 명단 출력 (연도 오름차순)
select year, fullname, birth_country from nobel
where (year >= 1910 and year <= 2010) and category='peace'
order by year asc;

# 4) 전체 테이블에서 수상자 이름이 ‘John’으로 시작하는 수상자 모두 출력
select category, fullname from nobel
where fullname like 'John%';

# 5) 1964년 수상자 중에서 노벨화학상과 의학상(‘Physiology or Medicine’)을 제외한
# 수상자의 모든 정보를 수상자 이름을 기준으로 오름차순으로 정렬 후 출력
select * from nobel
where year = 1964 and not category='Physiology or Medicine';

# 6) 2000년부터 2019년까지 노벨 문학상 수상자 명단 출력
select year, fullname, gender, birth_country from nobel
where (year between 2000 and 2019) and category='literature';

# 7) 각 분야별 역대 수상자의 수를 내림차순으로 정렬 후 출력(group by, order by)
select category, count(*) as 'count(category)'
from nobel
group by category
order by count(*) desc;

# 8) 노벨 의학상이 있었던 연도를 모두 출력 (distinct) 사용
select distinct year from nobel
where category='Physiology or Medicine';

# 9) 노벨 의학상이 없었던 연도의 총 회수를 출력
select count(distinct year) as no_medicine_count
from nobel
where year not in (select distinct year from nobel where category = 'Physiology or Medicine');


# 10) 여성 노벨 수상자의 명단 출력
select fullname, category, birth_country
from nobel
where gender = 'female';

# 11) 수상자들의 출생 국가별 횟수 출력
select birth_country, count(*) as 'count(birth_country)'
from nobel
group by birth_country;

# 12) 수상자의 출생 국가가 ‘Korea’인 정보 모두 출력
select * from nobel
where birth_country = 'Korea';

# 13) 수상자의 출신 국가가 (‘Europe’, ‘North America’, 공백)이 아닌 모든 정보 출력
select * from nobel
where birth_continent not in ('Europe', 'North America', '');

# 14) 수상자의 출신 국가별로 그룹화를 해서 수상 횟수가 10회 이상인 국가의 모든 정보
# 출력하고 국가별 수상횟수의 역순으로 출력 (birth_country, 횟수 출력)
select birth_country, count(*) as 'count'
from nobel
group by birth_country
having count(*) >= 10
order by count(*) desc;

# 15) 2회 이상 수상자 중에서 fullname이 공백이 아닌 경우를 출력하는데, fullname의 오름차순으로 출력
select fullname, count(*) as num
from nobel where not fullname = ''
group by fullname
having count(*) >= 2
order by fullname;