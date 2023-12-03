from config import app


class Admin:
    def __init__(self):
        self.managers = []
    
    def update_managers(self):
        cur = app.mysql.connection.cursor()
        cur.execute("SELECT emp_no FROM dept_manager")
        result = cur.fetchall()
        cur.close()
        self.managers = [x[0] for x in result]

admin = None
with app.app_context():
    admin = Admin()
    admin.update_managers()
