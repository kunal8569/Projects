create database flight_delay_cause;
use flight_delay_cause;
create table airline_delays(
    year INT,
    month INT,
    carrier VARCHAR(10),
    carrier_name VARCHAR(100),
    airport VARCHAR(10),
    airport_name VARCHAR(200),
    arr_flights INT,
    arr_del15 INT,
    carrier_ct INT,
    weather_ct INT,
    nas_ct INT,
    security_ct INT,
    late_aircraft_ct INT,
    arr_cancelled INT,
    arr_diverted INT,
    arr_delay FLOAT,
    carrier_delay FLOAT,
    weather_delay FLOAT,
    nas_delay FLOAT,
    security_delay FLOAT,
    late_aircraft_delay FLOAT
);
select * from airline_delays;




