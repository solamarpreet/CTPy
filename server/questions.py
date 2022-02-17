from flask import Blueprint, jsonify, request

question_bp = Blueprint('question', __name__, url_prefix='/question')

@question_bp.route('/1/', methods=['GET', 'POST'])
def q1():
    dict = {'qnum':'1', 'qtext':'What is the sum of game.data(1) and 3154?', 'qdata': 5927, 'qans': '9081'}
    if request.method == 'POST':
        ans = str(request.get_json()['ans'])
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qtext': dict['qtext'], 'qnum': dict['qnum'], 'qdata': dict['qdata']})

@question_bp.route('/2/', methods=['GET', 'POST'])
def q2():
    dict = {'qnum':'2', 'qtext':'Which element in this list is at the index position 3?', 'qdata':[25, 59, 31, 55, 13, 72], 'qans':'55'}
    if request.method == 'POST':
        ans = str(request.get_json()['ans'])
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qnum': dict['qnum'], 'qtext': dict['qtext'], 'qdata': dict['qdata']})