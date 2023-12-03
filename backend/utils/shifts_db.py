from config import app
from models.shift import Shift

def get_shifts_from_db(employee_no):
    cur = app.mysql.connection.cursor()
    cur.execute("SELECT * FROM shifts WHERE emp_no = %s", (employee_no,))
    db_shifts = cur.fetchall()
    cur.close()
    return db_shifts
