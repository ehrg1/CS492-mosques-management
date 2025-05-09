import sqlite3

class Mosque:
    def __init__(self):
        self.conn = sqlite3.connect('mosques.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Mosq (
            ID INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            address TEXT,
            coordinates TEXT,
            Imam_name TEXT
        )''')
        self.conn.commit()

    def Display(self):
        self.cursor.execute("SELECT * FROM Mosq")
        return self.cursor.fetchall()

    def Search(self, name):
        self.cursor.execute("SELECT * FROM Mosq WHERE name LIKE ?", ('%' + name + '%',))
        return self.cursor.fetchone()

    def Insert(self, ID, name, type_, address, coordinates, Imam_name):
        self.cursor.execute("INSERT INTO Mosq VALUES (?, ?, ?, ?, ?, ?)", 
                            (ID, name, type_, address, coordinates, Imam_name))
        self.conn.commit()

    def Delete(self, ID):
        self.cursor.execute("DELETE FROM Mosq WHERE ID=?", (ID,))
        self.conn.commit()

    def Update(self, ID, Imam_name):
        self.cursor.execute("UPDATE Mosq SET Imam_name=? WHERE ID=?", (Imam_name, ID))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
