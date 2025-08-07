import mysql.connector
import pandas as pd

#load data
df= pd.read_csv(r"C:\Users\hp\Desktop\American airline\Airline_Delay_Cause.csv")
# print(airline_delay)
df = df.astype(object).where(pd.notnull(df), None)
print(df)


#connect my sql
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="KUnal@2121",
    database="flight_delay_cause"
)
cursor=conn.cursor()

insert_stmt="""
insert into airline_delays(
year, month, carrier, carrier_name, airport, airport_name,
        arr_flights, arr_del15, carrier_ct, weather_ct, nas_ct, security_ct,
        late_aircraft_ct, arr_cancelled, arr_diverted, arr_delay,
        carrier_delay, weather_delay, nas_delay, security_delay, late_aircraft_delay
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

# Insert row by row (batching helps performance)
data = [tuple(x) for x in df.to_records(index=False)]
cursor.executemany(insert_stmt, data)
conn.commit()

print(f" {cursor.rowcount} rows inserted successfully.")

# Close
cursor.close()
conn.close()
