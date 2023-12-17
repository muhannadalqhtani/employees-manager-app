import sqlite3
# قاعدة بيانات
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age TEXT,
                job TEXT,
                email TEXT,
                gender TEXT,
                mobile TEXT,
                address TEXT
            )
        """
         # اضف لي قاعدة بيانات
        self.cur.execute(sql)
        self.con.commit()
      # ادخال  الى قاعدة بيانات
    def insert(self, name, age, job, email, gender, mobile, address):
        self.cur.execute("insert INTO employees VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                         (name, age, job, email, gender, mobile, address))
        self.con.commit()
        # يحدد موظفين بعدها يرتب لك
    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows
      # يحذف موظف من قاعدة بيانات
    def remove(self, id):
        self.cur.execute("DELETE FROM employees WHERE id=?", (id,))
        self.con.commit()
      # تحديث قاعدة الموظفين في قاعدة بيانات
    def update(self, id, name, age, job, email, gender, mobile, address):
        self.cur.execute("UPDATE employees SET name=?, age=?, job=?, email=?, gender=?, mobile=?, address=? WHERE id=?",
                         (name, age, job, email, gender, mobile, address, id))
        self.con.commit()


