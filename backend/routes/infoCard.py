# from flask import Blueprint, request, Response, jsonify, json
# from config import app
#
#
# infoCard = Blueprint('infoCard', __name__)
#
# @infoCard.route('/dashboard/infoCard', methods=['GET'])
# def infoCard():
#         #open database connection, and fetch data from database
#         cur = app.mysql.connection.cursor()
#         cur.execute("SELECT title FROM titles WHERE emp_no = %s ORDER BY from_date DESC LIMIT 1", (10001,))
#
#         title = cur.fetchone()
#         cur.close()
#
#
#         return jsonify({'title': title})