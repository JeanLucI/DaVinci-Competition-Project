from flask import Blueprint, request, jsonify

from .extensions import mongo

from .suggestion import generate_suggestion

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Connected to MongoDB!'

@main.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    email = data.get('email')
    first = data.get('first')
    last = data.get('last')
    pswd = data.get('pswd')
    tuition = data.get('tuition')
    rent = data.get('rent')
    grocery = data.get('grocery')
    eating_out = data.get('eating_out')
    transit = data.get('transit')
    boursaries = data.get('boursaries')
    loans = data.get('loans')
    income = data.get('income')

    mongo.db.users.insert_one(
        {
            '_id':email,
            'pswd':pswd,
            'first_name':first,
            'last_name':last,
            'tuition':tuition,
            'rent':rent,
            'grocery':grocery,
            'eating_out':eating_out,
            'transit':transit,
            'boursaries':boursaries,
            'loans':loans,
            'income':income
        }
    )
    return jsonify({'status': 'User added successfully!'})

@main.route('/check_email', methods=['POST'])
def check_email():
    data = request.json
    email = data.get('email')

    user = mongo.db.users.find_one({'_id':email})

    if user == None:
        return jsonify({'status': False})
    return jsonify({'status':True})

@main.route('/check_user', methods=['POST'])
def check_user():
    data = request.json
    email = data.get('email')
    pswd = data.get('pswd')

    user = mongo.db.users.find_one({'_id':email, 'pswd':pswd})
    if user == None:
        return jsonify({'status': False})
    return jsonify({'status': True})

@main.route('/get_data', methods=['GET'])
def get_user():
    email = request.args.get('email', '')

    user_data = mongo.db.users.find_one({'_id':email})

    return jsonify(user_data)

@main.route('/update_data', methods=['POST'])
def update_data():
    data = request.json
    email = data.get('email')
    tuition = data.get('tuition')
    rent = data.get('rent')
    grocery = data.get('grocery')
    eating_out = data.get('eating_out')
    transit = data.get('transit')
    boursaries = data.get('boursaries')
    loans = data.get('loans')
    income = data.get('income')

    mongo.db.users.update_one(
        {'_id':email}, 
        {'$set': 
            {
                'tuition': tuition,
                'rent':rent,
                'grocery':grocery,
                'eating_out':eating_out,
                'transit':transit,
                'boursaries':boursaries,
                'loans':loans,
                'income':income
            }
        }, upsert=True
    )

@main.route('/get_suggestion', methods=['GET'])
def get_suggestion():
    email = request.args.get('email', '')

    user_data = mongo.db.users.find_one({'_id':email})
    data_list = [
        user_data['tuition'],
        user_data['rent'],
        user_data['grocery'],
        user_data['eating_out'],
        user_data['transit'],
        user_data['boursaries'],
        user_data['loans'],
        user_data['income']
    ]

    suggestion = generate_suggestion(data_list)

    return jsonify({'suggestion':suggestion})


    