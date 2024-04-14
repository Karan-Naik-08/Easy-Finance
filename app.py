from flask import Flask, render_template,request,jsonify
import numpy as np
from HouseModel import give_pred
from CarModel import give_pred1

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('index1.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/input_form', methods=['POST'])
def input_form():
    return render_template('input_form.html')

@app.route("/verify", methods=['POST', 'GET'])
def verify():
    outpt= request.form.to_dict()
    finan=float(outpt['financialGoal'])
    yrs=float(outpt['years'])
    sal=float(outpt['salary'])
    med=float(outpt['medicalExpense'])
    wat=float(outpt['waterBill'])
    ele=float(outpt['electricityBill'])
    oth=float(outpt['otherexp'])


    percentage=6.3
    percentage_value = (percentage / 100) * finan
    finan1=finan+percentage_value

    allexp=med+wat+ele+oth

    yrstar=finan1/yrs
    monthly=yrstar/12

    saving=sal-allexp
    rem50=saving/2


    if monthly>rem50:
        name="The Goal is NOt achiveable Please Increase Years or decresase Goal Amount"
    else:
        name="The Goal Is Achiveable"

    return render_template("input_form.html",name=name)

@app.route('/house')
def house():
    return render_template('house.html')

@app.route("/result",methods=['POST','GET'])
def result():
    outpt= request.form.to_dict()
    area=outpt["Area"]
    bhk=outpt['BHK']
    bathroom=outpt['Bathrooms']
    parking=outpt['Parking']
    typ=outpt['type']
    status=outpt['status']
    transcation=outpt['Transcation']
    Frnishing=outpt['Furnishing']
    Locality=outpt['Locality']

    test=np.array([[area,bhk,bathroom,Frnishing,Locality,parking,status,transcation,typ]])
    inwords=give_pred(test)
    return render_template("house.html",name=inwords)


@app.route('/car')
def car():
    return render_template('car.html')

@app.route("/car_result", methods=['POST', 'GET'])
def car_result():
    input_data = request.form.to_dict()
    airbags = input_data["Airbags"]
    prod_year = input_data['Prod_year']
    Mileage = input_data['Mileage']
    Levy = input_data['Levy']
    fuel_type = input_data['Fuel_type']
    gear_box_type = input_data['Gear_box_type']
    Manufacturer = input_data['Manufacturer']
    Leather_interior = input_data['Leather_interior']
    Engine_Vol = input_data['Engine_Vol']

    test = np.array([[airbags, Mileage, prod_year, gear_box_type, Levy, Leather_interior, Manufacturer, fuel_type, Engine_Vol]])
    predicted_price = give_pred1(test)
    
    return render_template("car.html", price=predicted_price)

@app.route("/inputresult", methods=['POST', 'GET'])
def inputresult():
    global financial_data
    input_data = request.form.to_dict()
    salary=float(input_data.get("salary"))
    medicalExpense=float(input_data.get('medicalExpense'))
    waterBill=float(input_data.get('waterBill'))
    electricityBill=float(input_data.get('electricityBill'))
    otherexp=float(input_data.get('otherexp'))
    financialGoal1=float(input_data.get('financialGoal'))
    years=float(input_data.get('years'))

    percentage=6.3
    percentage_value = (percentage / 100) * financialGoal1
    financialGoal=financialGoal1+percentage_value

    m1= financialGoal/years
    monthlyAmount=m1/12
    financial_data = {
        'salary': salary,
        'medical_expense': medicalExpense,
        'water_bill': waterBill,
        'electricity_bill': electricityBill,
        'other_expenses': otherexp,
        'financial_goal': financialGoal,
        'years': years,
        'monthlyAmount' : monthlyAmount
    }

    return render_template("output.html")

@app.route("/get_financial_data", methods=['GET'])
def get_financial_data():
    global financial_data
    return jsonify(financial_data)




if __name__ == '__main__':
    app.run(debug=True)
