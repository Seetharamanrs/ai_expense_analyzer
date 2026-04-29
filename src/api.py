from flask import request, Flask,jsonify
from queries import  get_category_spending,get_monthly_trend, total_spending
from ai_advisor import get_financial_advice

app=Flask(__name__)

@app.route('/total',methods=['GET'])
def total():
    data=total_spending().to_dict()
    return jsonify(data)

@app.route('/category',methods=['GET'])
def category():
    data=get_category_spending().to_dict(orient="records")
    return jsonify(data)

@app.route('/monthly',methods=['GET'])
def monthly():
    data=get_monthly_trend().to_dict()
    return jsonify(data)

@app.route('/ai-advice',methods=['GET'])
def ai_advice():
    df=get_category_spending()
    sumary=df.to_string(index=False)
    advice=get_financial_advice(sumary)
    return jsonify({"Advice":advice})


if __name__=="__main__":
    app.run(debug=True)