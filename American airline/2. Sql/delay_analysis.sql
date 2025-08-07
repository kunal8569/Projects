select * from airline_delays;
-- total row count
select count(*) from airline_delays;

-- avaible years
select distinct year from airline_delays;

-- distinct airport
select count(distinct airport) as total_airports FROM airline_delays;

-- distinct carrier
select distinct carrier_name from airline_delays
where carrier_name like '%American%';

 -- filter to american airlines
 select * from airline_delays
 where carrier_name in ("American Eagle Airlines Inc.", "American Airlines Inc.", "American Airlines Network");
 
 -- delay trend by month (all year)
 select year, month, sum(arr_delay) as total_delay from airline_delays
 where carrier_name in ("American Eagle Airlines Inc.", "American Airlines Inc.", "American Airlines Network")
 group by year, month
 order by year, month;
 
 -- total delay reason across all airline
 select 
	sum(carrier_ct) as carrier,
    sum(weather_ct) as weather,
    sum(nas_ct) as nas,
    sum(security_ct) as security,
    sum(late_aircraft_ct) as late_aircraft
from airline_delays;
 
 -- top dealy cause of american airline
select 
	sum(carrier_ct) as carrier,
    sum(weather_ct) as weather,
    sum(nas_ct) as nas,
    sum(security_ct) as security,
    sum(late_aircraft_ct) as late_aircraft
from airline_delays
where carrier_name in ("American Eagle Airlines Inc.", "American Airlines Inc.", "American Airlines Network");

-- delay per airport for american airline
select airport_name, sum(arr_delay) as total_delay from airline_delays
where carrier_name in ("American Eagle Airlines Inc.", "American Airlines Inc.", "American Airlines Network")
group by airport_name
order by total_delay desc
limit 10;

-- cancelled and diverted airline trend
select year, month, sum(arr_cancelled) as cancelled,
    sum(arr_diverted) as diverted
    from airline_delays
    where carrier_name in ("American Eagle Airlines Inc.", "American Airlines Inc.", "American Airlines Network")
group by year, month
order by year, month;