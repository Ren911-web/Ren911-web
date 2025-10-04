from flask import Blueprint, request, jsonify
Logout = Blueprint('Logout',__name__)

@Logout.route('/logout', methods=['POST'])
def logout_user():
    print("Headers", request.headers)