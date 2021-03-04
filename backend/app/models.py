from app import db
from typing import List


class Categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(64), nullable=False, unique=True)
    questions = db.relationship("Questions", backref="quest", lazy='dynamic')

    def __repr__(self) -> str:
        return '{}'.format(self.category_name)

    @staticmethod
    def add(category_dict: dict) -> None:
        category = Categories(category_name=category_dict["data"])
        db.session.add(category)
        db.session.commit()

    @staticmethod
    def get_categories() -> List[list]:
        categories = db.session.query(Categories).all()
        return [[item.category_id, item.category_name] for item in
                categories]

    @staticmethod
    def delete_note(category_id: int) -> None:
        delete = db.session.query(Categories).filter_by\
            (category_id=category_id).one()
        db.session.delete(delete)
        db.session.commit()

    @staticmethod
    def to_json(dictionary: dict) -> dict:
        res = {"categories": []}
        res2 = {"categories": [res["categories"].append({"id": k, "name": v})
                               for k, v in dictionary.items()]}
        return res

    @staticmethod
    def edit(category_name: dict, id: int) -> None:
        print(category_name)
        Categories.query.filter_by(category_id=id).update \
            (dict(category_name=category_name["data"]))
        db.session.commit()


class Questions(db.Model):
    category_id = db.Column(db.Integer,
                            db.ForeignKey('categories.category_id'))
    question = db.Column(db.String(140), nullable=False, unique=True)
    question_id = db.Column(db.Integer, primary_key=True)
    answers = db.relationship("Answers", backref="questions", lazy='dynamic')

    def __repr__(self) -> str:
        return '{}'.format(self.question)

    def __eq__(self, other):
        return self.question == other.question and self.category_id == \
               other.category_id and self.question_id == other.question_id


class Answers(db.Model):
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    answer = db.Column(db.String, nullable=False)
    answer_id = db.Column(db.Integer, primary_key=True)
    right_answer = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return '{}'.format(self.answer)

    def __eq__(self, other):
        return self.answer == other.answer and self.answer_id == \
               other.answer_id and self.question_id == other.question_id and \
               self.right_answer == other.right_answer
