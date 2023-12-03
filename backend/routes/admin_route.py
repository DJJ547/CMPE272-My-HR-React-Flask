from flask import blueprints, jsonify, request, Response, session, json
from config import app
from models.admin import admin
from datetime import datetime

admin_route = blueprints.Blueprint('admin_route', __name__)

@admin_route.route('/admin/Get_all_users', methods=['GET'])
def get_all_users():
    if request.method == 'GET':
        cur = app.mysql.connection.cursor()
        cur.execute("SELECT emp_no, birth_date, first_name, last_name, gender, hire_date FROM employees limit 20")
        data = cur.fetchall()
        cur.close()
        
        output = []
        for i in data:
            i ={}
            i['id'] = data[0]
            i['birth_date'] = i[1]
            i['first_name'] = data[2]
            i['last_name'] = data[3]
            i['gender'] = data[4]
            i['hire_date'] = data[5]
            output.append(i)
        
        print(output)
        return Response(json.dumps(output), status=200)

