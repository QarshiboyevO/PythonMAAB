import sqlite3

# =========================
# TASK 1 — roster.db
# =========================

conn = sqlite3.connect("roster.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Insert data
cur.executemany("""
INSERT INTO Roster VALUES (?, ?, ?)
""", [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

# Update name
cur.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# Query Bajoran
cur.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")
print("Bajoran Characters:", cur.fetchall())

# Delete over 100
cur.execute("""
DELETE FROM Roster WHERE Age > 100
""")

# Add Rank column
try:
    cur.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
except:
    pass

# Update ranks
cur.execute("UPDATE Roster SET Rank='Captain' WHERE Name='Benjamin Sisko'")
cur.execute("UPDATE Roster SET Rank='Lieutenant' WHERE Name='Ezri Dax'")
cur.execute("UPDATE Roster SET Rank='Major' WHERE Name='Kira Nerys'")

# Sort by age descending
cur.execute("SELECT * FROM Roster ORDER BY Age DESC")
print("Roster Sorted:", cur.fetchall())

conn.commit()
conn.close()


# =========================
# TASK 2 — library.db
# =========================

conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# Insert data
cur.executemany("""
INSERT INTO Books VALUES (?, ?, ?, ?)
""", [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
])

# Update year
cur.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984'
""")

# Query Dystopian
cur.execute("""
SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'
""")
print("Dystopian Books:", cur.fetchall())

# Delete before 1950
cur.execute("""
DELETE FROM Books WHERE Year_Published < 1950
""")

# Add Rating column
try:
    cur.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
except:
    pass

# Update ratings
cur.execute("UPDATE Books SET Rating=4.8 WHERE Title='To Kill a Mockingbird'")
cur.execute("UPDATE Books SET Rating=4.7 WHERE Title='1984'")
cur.execute("UPDATE Books SET Rating=4.5 WHERE Title='The Great Gatsby'")

# Sort by year ascending
cur.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
print("Books Sorted:", cur.fetchall())

conn.commit()
conn.close()