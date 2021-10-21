Задание 4.1
База данных содержит список аэропортов практически всех крупных городов России. В большинстве городов есть только один аэропорт. Исключение составляет:
select
    city,
    count(airport_code) as airport_count
from dst_project.airports
group by city
having count(airport_code) > 1



Задание 4.2
Вопрос 1
Таблица рейсов содержит всю информацию о прошлых, текущих и запланированных рейсах. Сколько всего статусов для рейсов определено в таблице?
select count(distinct status)
from dst_project.flights

Вопрос 2
Какое количество самолетов находятся в воздухе на момент среза в базе (статус рейса «самолёт уже вылетел и находится в воздухе»).
select count(aircraft_code)
from dst_project.flights
where status = 'Departed'

Вопрос 3
Места определяют схему салона каждой модели. Сколько мест имеет самолет модели 773 (Boeing 777-300)?
select 
    aircraft_code,
    count(seat_no) as seat_count
from dst_project.seats
where aircraft_code = '773'
group by aircraft_code

Вопрос 4
Сколько состоявшихся (фактических) рейсов было совершено между 1 апреля 2017 года и 1 сентября 2017 года?
select count(flight_no)
from dst_project.flights
where
    status = 'Arrived'
    and scheduled_arrival between '20170401' and '20170901'


Задание 4.3
Вопрос 1
Сколько всего рейсов было отменено по данным базы?
select count(flight_no)
from dst_project.flights
where status = 'Cancelled'

Вопрос 2
Сколько самолетов моделей типа Boeing, Sukhoi Superjet, Airbus находится в базе авиаперевозок?
select count(model) as aircraft_count
from dst_project.aircrafts
where model like '%Boeing%'

Вопрос 3
В какой части (частях) света находится больше аэропортов?
select count(airport_code)
from dst_project.airports
where timezone like '%Asia%'

Вопрос 4
У какого рейса была самая большая задержка прибытия за все время сбора данных?
select
    flight_id,
    flight_no,
    scheduled_arrival,
    actual_arrival,
    extract(epoch from scheduled_arrival - actual_arrival)
from dst_project.flights
where status = 'Arrived'
order by 5
limit 1

Задание 4.4
Вопрос 1
Когда был запланирован самый первый вылет, сохраненный в базе данных?
select *
from dst_project.flights
order by scheduled_departure
limit 1

Вопрос 2
Сколько минут составляет запланированное время полета в самом длительном рейсе?
select
    flight_id,
    flight_no,
    scheduled_departure,
    scheduled_arrival,
    extract(epoch from scheduled_arrival - scheduled_departure) / 60 as time_dif
from dst_project.flights
order by 5 desc
limit 1

Вопрос 3
Между какими аэропортами пролегает самый длительный по времени запланированный рейс?
select
    flight_id,
    flight_no,
    departure_airport,
    arrival_airport,
    scheduled_departure,
    scheduled_arrival,
    extract(epoch from scheduled_arrival - scheduled_departure) / 60 as time_dif
from dst_project.flights
order by 7 desc
limit 1

Вопрос 4
Сколько составляет средняя дальность полета среди всех самолетов в минутах? Секунды округляются в меньшую сторону (отбрасываются до минут).
select
    avg(extract(epoch from scheduled_arrival - scheduled_departure) / 60)
from dst_project.flights


Задание 4.5
Вопрос 1
Мест какого класса у SU9 больше всего?
select
    fare_conditions,
    count(seat_no) as seats_count
from dst_project.seats
where aircraft_code = 'SU9'
group by fare_conditions

Вопрос 2
Какую самую минимальную стоимость составило бронирование за всю историю?
select
    book_ref,
    total_amount
from dst_project.bookings
order by total_amount
limit 1

Вопрос 3
Какой номер места был у пассажира с id = '4313 788533'?
select seat_no
from dst_project.boarding_passes
where
    ticket_no = (select t.ticket_no
                from dst_project.tickets as t
                where t.passenger_id = '4313 788533')


Задание 5.1
Вопрос 1
Анапа — курортный город на юге России. Сколько рейсов прибыло в Анапу за 2017 год?
select count(flight_id)
from dst_project.flights
where
    arrival_airport = (select airport_code from dst_project.airports where city = 'Anapa')
    and status = 'Arrived'
    and actual_arrival between '20170101' and '20171231'

Вопрос 2
Сколько рейсов из Анапы вылетело зимой 2017 года?
select count(flight_id)
from dst_project.flights
where
    departure_airport = (select airport_code from dst_project.airports where city = 'Anapa')
    and date_part('month', actual_departure) in (1,2)

Вопрос 3
Посчитайте количество отмененных рейсов из Анапы за все время.
select count(flight_id)
from dst_project.flights
where
    departure_airport = (select airport_code from dst_project.airports where city = 'Anapa')
    and status = 'Cancelled'

Вопрос 4
Сколько рейсов из Анапы не летают в Москву?
select count(flight_id)
from dst_project.flights
where
    departure_airport = (select airport_code from dst_project.airports where city = 'Anapa')
    and arrival_airport not in (select airport_code from dst_project.airports where city = 'Moscow')

Вопрос 5
Какая модель самолета летящего на рейсах из Анапы имеет больше всего мест?
with A as (
    select distinct
        f.aircraft_code,
        a.model
    from dst_project.flights as f
        join dst_project.aircrafts as a on f.aircraft_code = a.aircraft_code
    where
        departure_airport = (select airport_code from dst_project.airports where city = 'Anapa')
)
select 
    A.aircraft_code,
    A.model,
    count(S.seat_no)
from A
    join dst_project.seats as S on A.aircraft_code = S.aircraft_code
group by
    A.aircraft_code,
    A.model