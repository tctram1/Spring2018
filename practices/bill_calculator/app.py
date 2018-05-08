from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/bill", methods=['POST', 'GET'])


def index():
    
    # Taxes dictionary
    states = {
        'Alabama': '0.0910',
        'AL': '0.0910',
        'Alaska': '0.0176',
        'AK': '0.0176',
        'Arizona': '0.0833',
        'AZ': '0.0833',
        'Arkansas': '0.0941',
        'AR': '0.0941',
        'California': '0.0854',
        'CA': '0.0854',
        'Colorado': '0.0752',
        'CO': '0.0752',
        'Connecticut': '0.0635',
        'CT': '0.0635',
        'Delaware': '0',
        'DE': '0',
        'Floria': '0.0680',
        'FL': '0.0680',
        'Georgia': '0.0715',
        'GA': '0.0715',
        'Hawaii': '0.0435',
        'HI': '0.0435',
        'Idaho': '0.0603',
        'ID': '0.0603',
        'Illinois': '0.0870',
        'IL': '0.0870',
        'Indiana': '0.0700',
        'IN': '0.0700',
        'Iowa': '0.0680',
        'IA': '0.0680',
        'Kansas': '0.0868',
        'KS': '0.0868',
        'Kentucky': '0.0600',
        'KY': '0.0600',
        'Louissiana': '0.1002',
        'LA': '0.1002',
        'Maine': '0.0550',
        'ME': '0.0550',
        'Maryland': '0.0600',
        'MD': '0.0600',
        'Massachusetts': '0.0625',
        'MA': '0.0625',
        'Michigan': '0.0600',
        'MI': '0.0600',
        'Minnesota': '0.0742',
        'MN': '0.0742',
        'Mississippi': '0.0707',
        'MS': '0.0707',
        'Missouri': '0.0803',
        'MO': '0.0803',
        'Montana': '0',
        'MT': '0',
        'Nebraska': '0.0689',
        'NE': '0.0689',
        'Nevada': '0.0814',
        'NV': '0.0814',
        'New Hampshire': '0',
        'NH': '0',
        'New Jersey': '0.0660',
        'NJ': '0.0660',
        'New Mexico': '0.0766',
        'NM': '0.0766',
        'New York': '0.0849',
        'NY': '0.0849',
        'North Carolina': '0.0695',
        'NC': '0.0695',
        'North Dakota': '0.0680',
        'ND': '0.0680',
        'Ohio': '0.0715',
        'OH': '0.0715',
        'Oklahoma': '0.0891',
        'OK': '0.0891',
        'Oregon': '0',
        'OR': '0',
        'Pennsylvania': '0.0634',
        'PA': '0.0634',
        'Rhode Island': '0.0700',
        'RI': '0.0700',
        'South Carolina': '0.0737',
        'SC': '0.0737',
        'South Dakota': '0.0640',
        'SD': '0.0640',
        'Tennessee': '0.0946',
        'TN': '0.0946',
        'Texas': '0.0817',
        'TX': '0.0817',
        'Utah': '0.0677',
        'UT': '0.0677',
        'Vermont': '0.0618',
        'VT': '0.0618',
        'Virgina': '0.0563',
        'VA': '0.0563',
        'Washington': '0.0918',
        'WA': '0.0918',
        'West Virginia': '0.0637',
        'WV': '0.0637',
        'Wisconsin': '0.0542',
        'WI': '0.0542',
        'Wyoming': '0.0546',
        'WY': '0.0546'
    }

    if request.method == "POST":
        my_meal_bt = float(request.form['my_meal_bt'])
        state = request.form['state']
        # from state get tax from dictionary
        if state in states:
            my_tax_value = float(states[state])
        else:
            print("State is invalid. Cann't get tax value.")
        my_meal_at = my_meal_bt + my_meal_bt * my_tax_value
        state_tax = my_tax_value * 100
        display_state_tax = round(state_tax, 2)
        my_tip_value = my_meal_at * 0.20
        display_tip = round(my_tip_value, 2)
        my_total = my_meal_at + my_tip_value
        display_total = round(my_total, 2)
        my_tax = my_tax_value * my_meal_bt
        display_tax = round(my_tax, 2)
        state = f"{state}"
        meal_bt = f"{my_meal_bt}"
        state_tax = f"{state_tax}"
        tax_value = f"{display_tax}"
        tip_value = f"{display_tip}"
        total = f"{display_total}"
        return render_template("index.html", state=state, meal_bt=meal_bt, state_tax=display_state_tax, tax_value=tax_value, tip_value=tip_value, total=total)
    else:
        return render_template("bill_form.html")

if __name__ == "__main__":
    app.run()