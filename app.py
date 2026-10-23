from flask import Flask, render_template, request
from evaluator import evaluate_startup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        idea = {
            'problem': request.form['startup_idea'],
            'unique': request.form['unique'],
            'market': request.form['market'],
            'competition': request.form['competition'],
            'monetization': request.form['revenue_plan']
        }
        score, result = evaluate_startup(idea)
        return render_template('index.html', score=score, result=result, idea=idea)
    return render_template('index.html', score=None, result=None)

if __name__ == '__main__':
    app.run(debug=True)
