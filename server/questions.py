from flask import Blueprint, jsonify, request

question_bp = Blueprint('question', __name__, url_prefix='/question')

@question_bp.route('/1/', methods=['GET', 'POST'])
def q1():
    dict = {
            'qnum' :    '1',
            'qtext':    'What is the sum of game.data(1) and 3154?',
            'qdata':    5927,
            'qans' :    '9081'
            }
    if request.method == 'POST':
        ans = request.get_json()['ans']
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qtext': dict['qtext'], 'qnum': dict['qnum'], 'qdata': dict['qdata']})

@question_bp.route('/2/', methods=['GET', 'POST'])
def q2():
    dict = {
            'qnum'  :   '2',
            'qtext' :   'What is the length of the string returned by game.data(2)?',
            'qdata' :   'You bring the crowns and heads of conquered kings to my city steps! You insult my queen, You threaten my people with slavery and death. Oh Ive chosen my words carefully persian, perhaps you should have done the same.',
            'qans'  :   '216'
            }
    if request.method == 'POST':
        ans = request.get_json()['ans']
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qnum': dict['qnum'], 'qtext': dict['qtext'], 'qdata': dict['qdata']})

@question_bp.route('/3/', methods=['GET', 'POST'])
def q3():
    dict = {
            'qnum'  :   '3',
            'qtext' :   'Which element in the list returned by game.data(3) is at index position 38?',
            'qdata' :   [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527],
            'qans'  :   '892'
            }
    if request.method == 'POST':
        ans = request.get_json()['ans']
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qnum': dict['qnum'], 'qtext': dict['qtext'], 'qdata': dict['qdata']})

@question_bp.route('/4/', methods=['GET', 'POST'])
def q4():
    dict = {
            'qnum'  :   '4',
            'qtext' :   'Return a string that contains the characters starting from index 10 and going upto but not including the character at index 25 in the string generated by the game.data(4) method.',
            'qdata' :   'Yes! Yes! Bombay is berry berry nice this time of the year.',
            'qans'  :   'Bombay is berry'
            }
    if request.method == 'POST':
        ans = request.get_json()['ans']
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qnum': dict['qnum'], 'qtext': dict['qtext'], 'qdata': dict['qdata']})

@question_bp.route('/5/', methods=['GET', 'POST'])
def q5():
    dict = {
            'qnum'  :   '5',
            'qtext' :   'Reverse the string generated by game.data(5) function.',
            'qdata' :   'Yes! Yes! Bombay is berry berry nice this time of the year.',
            'qans'  :   '.raey eht fo emit siht ecin yrreb yrreb si yabmoB !seY !seY'
            }
    if request.method == 'POST':
        ans = request.get_json()['ans']
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qnum': dict['qnum'], 'qtext': dict['qtext'], 'qdata': dict['qdata']})

@question_bp.route('/6/', methods=['GET', 'POST'])
def q6():
    dict = {
            'qnum'  :   '6',
            'qtext' :   'Reverse the second half of the string in game.data(6) and then return the complete string so that the first half of the answer is unchanged and the second half is reversed.',
            'qdata' :   'You think darkness is your ally. But you merely adopted the dark. I was born in it, moulded by it.',
            'qans'  :   'You think darkness is your ally. But you merely ad.ti yb dedluom ,ti ni nrob saw I .krad eht detpo'
            }
    if request.method == 'POST':
        ans = request.get_json()['ans']
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qnum': dict['qnum'], 'qtext': dict['qtext'], 'qdata': dict['qdata']})

@question_bp.route('/7/', methods=['GET', 'POST'])
def q7():
    dict = {
            'qnum'  :   '7',
            'qtext' :   'Create a string by joining all the elements in the list returned by game.data(7) seperated by a space',
            'qdata' :   ['Badges!','We','dont','need','no','stinkin','badges.'],
            'qans'  :   'Badges! We dont need no stinkin badges.'
            }
    if request.method == 'POST':
        ans = request.get_json()['ans']
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qnum': dict['qnum'], 'qtext': dict['qtext'], 'qdata': dict['qdata']})

@question_bp.route('/8/', methods=['GET', 'POST'])
def q8():
    dict = {
            'qnum'  :   '8',
            'qtext' :   'Increment each element in the list returned by game.data(8) method by 15',
            'qdata' :   [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527],
            'qans'  :   '[401, 477, 62, 433, 922, 359, 251, 390, 838, 581, 612, 993, 343, 630, 968, 360, 414, 177, 773, 234, 933, 252, 427, 581, 841, 263, 881, 965, 641, 964, 702, 232, 830, 82, 119, 73, 527, 39, 907, 909, 782, 568, 96, 394, 858, 846, 460, 757, 732, 973, 758, 542]'
            }
    if request.method == 'POST':
        ans = request.get_json()['ans']
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qnum': dict['qnum'], 'qtext': dict['qtext'], 'qdata': dict['qdata']})

@question_bp.route('/9/', methods=['GET', 'POST'])
def q9():
    dict = {
            'qnum'  :   '9',
            'qtext' :   'The method game.data(9) returns a nested list that further contains 2 lists. Add each element of the first inner list with each element at the same index in the second inner list and return the answer as a new list',
            'qdata' :   [[456, 39, 532, 126, 245, 57, 27], [91, 234, 43, 438, 317, 619, 30]],
            'qans'  :   '[547, 273, 575, 564, 562, 676, 57]'
            }
    if request.method == 'POST':
        ans = request.get_json()['ans']
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qnum': dict['qnum'], 'qtext': dict['qtext'], 'qdata': dict['qdata']})

@question_bp.route('/10/', methods=['GET', 'POST'])
def q10():
    dict = {
            'qnum'  :   '10',
            'qtext' :   'The method game.data(10) returns a list where each element is the hexadecimal representation of a unicode character. Convert all the characters, join them & submit your answer as a string.',
            'qdata' :   ['0x54', '0x68', '0x65', '0x72', '0x65', '0x73', '0x20', '0x61', '0x20', '0x50', '0x68', '0x6f', '0x65', '0x62', '0x65', '0x20', '0x6f', '0x6e', '0x20', '0x6d', '0x79', '0x20', '0x73', '0x61', '0x6e', '0x64', '0x77', '0x69', '0x63', '0x68', '0x21'],
            'qans'  :   'Theres a Phoebe on my sandwich!'
            }
    if request.method == 'POST':
        ans = request.get_json()['ans']
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qnum': dict['qnum'], 'qtext': dict['qtext'], 'qdata': dict['qdata']})

@question_bp.route('/11/', methods=['GET', 'POST'])
def q11():
    dict = {
            'qnum'  :   '11',
            'qtext' :   'The method game.data(11) returns a base64 encoded string. Decode and return this string',
            'qdata' :   'RmFpdGggaW4geW91ciBuZXcgYXBwcmVudGljZSwgbWlzcGxhY2VkIG1heSBiZS4gQXMgaXMgeW91ciBmYWl0aCBpbiB0aGUgZGFyayBzaWRlIG9mIHRoZSBmb3JjZS4gQXQgYW4gZW5kIHlvdXIgcnVsZSBpcy4gQW5kIHNob3J0IGVub3VnaCBpdCB3YXMh',
            'qans'  :   'Faith in your new apprentice, misplaced may be. As is your faith in the dark side of the force. At an end your rule is. And short enough it was!'
            }
    if request.method == 'POST':
        ans = request.get_json()['ans']
        if ans == dict['qans']:
            return jsonify({'check':'Correct Answer'})
        else:
            return jsonify({'check':'Incorrect Answer. Please try again'})
    else:
        return jsonify({'qnum': dict['qnum'], 'qtext': dict['qtext'], 'qdata': dict['qdata']})
