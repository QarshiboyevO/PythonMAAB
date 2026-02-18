import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

customers = pd.read_sql("SELECT * FROM customers", conn)
invoices = pd.read_sql("SELECT * FROM invoices", conn)

inner = customers.merge(invoices, on="CustomerId", how="inner")

invoice_counts = inner.groupby("CustomerId")["InvoiceId"].count().reset_index()
invoice_counts.columns = ["CustomerId", "Total_Invoices"]

print(invoice_counts.head())

movies = pd.read_csv("movie.csv")

df1 = movies[["director_name", "color"]]
df2 = movies[["director_name", "num_critic_for_reviews"]]

left_join = df1.merge(df2, on="director_name", how="left")
outer_join = df1.merge(df2, on="director_name", how="outer")

print("Left join rows:", len(left_join))
print("Outer join rows:", len(outer_join))


titanic = pd.read_csv("titanic.csv")

grouped = titanic.groupby("Pclass").agg(
    Avg_Age=("Age", "mean"),
    Total_Fare=("Fare", "sum"),
    Passenger_Count=("PassengerId", "count")
).reset_index()

print(grouped)

movie_group = movies.groupby(["color", "director_name"]).agg(
    Total_Reviews=("num_critic_for_reviews", "sum"),
    Avg_Duration=("duration", "mean")
)

print(movie_group.head())

flights = pd.read_csv("flights.csv")

flight_group = flights.groupby(["Year", "Month"]).agg(
    Total_Flights=("FlightNum", "count"),
    Avg_ArrDelay=("ArrDelay", "mean"),
    Max_DepDelay=("DepDelay", "max")
).reset_index()

print(flight_group.head())

def age_group(age):
    if age < 18:
        return "Child"
    else:
        return "Adult"

titanic["Age_Group"] = titanic["Age"].apply(lambda x: age_group(x) if pd.notnull(x) else "Unknown")

employees = pd.read_csv("employee.csv")

employees["Norm_Salary"] = employees.groupby("Department")["Salary"].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)

print(employees.head())

def duration_type(d):
    if d < 60:
        return "Short"
    elif d <= 120:
        return "Medium"
    else:
        return "Long"

movies["Duration_Type"] = movies["duration"].apply(duration_type)

result = (
    titanic
    .pipe(lambda df: df[df["Survived"] == 1])
    .pipe(lambda df: df.assign(Age=df["Age"].fillna(df["Age"].mean())))
    .pipe(lambda df: df.assign(Fare_Per_Age=df["Fare"] / df["Age"]))
)

print(result.head())
flight_pipe = (
    flights
    .pipe(lambda df: df[df["DepDelay"] > 30])
    .pipe(lambda df: df.assign(Delay_Per_Hour=df["DepDelay"] / df["AirTime"]))
)

print(flight_pipe.head())