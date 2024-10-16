from flask import Flask, jsonify, request  
from flask_sqlalchemy import SQLAlchemy  
  
app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///indian_constitution.db'  
db = SQLAlchemy(app)  
  
class Article(db.Model):  
 id = db.Column(db.Integer, primary_key=True)  
 title = db.Column(db.String(100), nullable=False)  
 content = db.Column(db.Text, nullable=False)  
 category = db.Column(db.String(50), nullable=False)  
 tags = db.Column(db.String(100), nullable=False)  
 creation_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())  
  
class Amendment(db.Model):  
 id = db.Column(db.Integer, primary_key=True)  
 title = db.Column(db.String(100), nullable=False)  
 content = db.Column(db.Text, nullable=False)  
 category = db.Column(db.String(50), nullable=False)  
 tags = db.Column(db.String(100), nullable=False)  
 creation_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())  
  
class FAQ(db.Model):  
 id = db.Column(db.Integer, primary_key=True)  
 question = db.Column(db.String(100), nullable=False)  
 answer = db.Column(db.Text, nullable=False)  
 category = db.Column(db.String(50), nullable=False)  
 tags = db.Column(db.String(100), nullable=False)  
 creation_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())  
  
class Contact(db.Model):  
 id = db.Column(db.Integer, primary_key=True)  
 name = db.Column(db.String(50), nullable=False)  
 email = db.Column(db.String(100), nullable=False)  
 phone_number = db.Column(db.String(20), nullable=False)  
 message = db.Column(db.Text, nullable=False)  
  
@app.route('/articles', methods=['GET'])  
def get_articles():  
 articles = Article.query.all()  
 return jsonify([article.to_dict() for article in articles])  
  
@app.route('/articles', methods=['POST'])  
def create_article():  
 article = Article(title=request.json['title'], content=request.json['content'], category=request.json['category'], tags=request.json['tags'])  
 db.session.add(article)  
 db.session.commit()  
 return jsonify(article.to_dict())  
  
@app.route('/amendments', methods=['GET'])  
def get_amendments():  
 amendments = Amendment.query.all()  
 return jsonify([amendment.to_dict() for amendment in amendments])  
  
@app.route('/amendments', methods=['POST'])  
def create_amendment():  
 amendment = Amendment(title=request.json['title'], content=request.json['content'], category=request.json['category'], tags=request.json['tags'])  
 db.session.add(amendment)  
 db.session.commit()  
 return jsonify(amendment.to_dict())  
  
@app.route('/faqs', methods=['GET'])  
def get_faqs():  
 faqs = FAQ.query.all()  
 return jsonify([faq.to_dict() for faq in faqs])  
  
@app.route('/faqs', methods=['POST'])  
def create_faq():  
 faq = FAQ(question=request.json['question'], answer=request.json['answer'], category=request.json['category'], tags=request.json['tags'])  
 db.session.add(faq)  
 db.session.commit()  
 return jsonify(faq.to_dict())  
  
@app.route('/contact', methods=['POST'])  
def create_contact():  
 contact = Contact(name=request.json['name'], email=request.json['email'], phone_number=request.json['phone_number'], message=request.json['message'])  
 db.session.add(contact)  
 db.session.commit()  
 return jsonify(contact.to_dict())  
  
if __name__ == '__main__':  
 app.run(debug=True)
