from app import app
from typing import Dict, List
from app.models import Questions
from app.api.users_api import token_required
from flask import jsonify, wrappers, request


@app.route('/questions/', methods=['GET'])
def questions() -> Dict[str, List[Dict[str, str]]]:
    return Questions.to_json(dict(Questions.get_questions()))


@app.route('/question/<int:id>', methods=['GET'])
def get_question(id: int) -> Dict[str, List[Dict[str, str]]]:
    question = Questions.query.get_or_404(id)
    output = []
    question_data = {}
    question_data['id'] = question.question_id
    question_data['question'] = question.question
    question_data['category'] = question.category_id
    output.append(question_data)

    return jsonify({'question': output})


@app.route('/question', methods=['POST'])
@token_required
def add_question() -> wrappers.Response:
    question = request.get_json()
    print(question)
    try:
        Questions.add(question)
        return jsonify({"201 Created": "HTTP/1.1"})
    except:
        return jsonify({"403 Forbidden": "HTTP/1.1"})


@app.route('/question/<int:id>', methods=['DELETE'])
@token_required
def delete_question(id: int) -> wrappers.Response:
    Questions.query.get_or_404(id)
    try:
        Questions.delete_note(id)
        return jsonify({"200 OK": "HTTP/1.1"})
    except:
        return jsonify({"403 Forbidden": "HTTP/1.1"})


@app.route('/question/<int:id>', methods=['PUT'])
@token_required
def edit_question(id: int) -> wrappers.Response:
    Questions.query.get_or_404(id)
    try:
        Questions.edit(request.get_json(), id)
        return jsonify({"200 OK": "HTTP/1.1"})
    except:
        return jsonify({"403 Forbidden": "HTTP/1.1"})


@app.route('/category/<int:id>/questions', methods=['GET'])
@token_required
def get_category_questions(id: int) -> wrappers.Response:
    category_questions = Questions.query.filter_by(category_id=id).all()
    output = []
    for question in category_questions:
        question_data = {}
        question_data['id'] = question.question_id
        question_data['question'] = question.question
        question_data['category'] = question.category_id
        output.append(question_data)
    return jsonify({'question': output})
