from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)

# Connection to your XAMPP database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/bincom_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Tables mapping
class AnnouncedPuResults(db.Model):
    __tablename__ = 'announced_pu_results'
    result_id = db.Column(db.Integer, primary_key=True)
    polling_unit_uniqueid = db.Column(db.String(50))
    party_abbreviation = db.Column(db.String(4))
    party_score = db.Column(db.Integer)
    entered_by_user = db.Column(db.String(50))

class Lga(db.Model):
    __tablename__ = 'lga'
    uniqueid = db.Column(db.Integer, primary_key=True)
    lga_id = db.Column(db.Integer)
    lga_name = db.Column(db.String(50))

class PollingUnit(db.Model):
    __tablename__ = 'polling_unit'
    uniqueid = db.Column(db.Integer, primary_key=True)
    lga_id = db.Column(db.Integer)

@app.route('/')
def question1():
    results = AnnouncedPuResults.query.filter_by(polling_unit_uniqueid='8').all()
    return render_template('question1.html', results=results)

@app.route('/lga', methods=['GET', 'POST'])
def question2():
    lgas = Lga.query.all()
    selected_lga = request.form.get('lga_id')
    results = None
    if selected_lga:
        results = db.session.query(
            AnnouncedPuResults.party_abbreviation, 
            func.sum(AnnouncedPuResults.party_score)
        ).join(PollingUnit, AnnouncedPuResults.polling_unit_uniqueid == PollingUnit.uniqueid)\
         .filter(PollingUnit.lga_id == selected_lga)\
         .group_by(AnnouncedPuResults.party_abbreviation).all()
    return render_template('question2.html', lgas=lgas, results=results)

@app.route('/add', methods=['GET', 'POST'])
def question3():
    if request.method == 'POST':
        new_res = AnnouncedPuResults(
            polling_unit_uniqueid=request.form['pu_id'],
            party_abbreviation=request.form['party'],
            party_score=request.form['score'],
            entered_by_user='Motunrayo'
        )
        db.session.add(new_res)
        db.session.commit()
        return "Success! <a href='/'>Go Home</a>"
    return render_template('question3.html')

if __name__ == '__main__':
    app.run(debug=True)