from flask import Flask, render_template, request

app = Flask(__name__)

def length_converter(value, from_unit, to_unit):
    conversions = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1,
        'km': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34
        }
    value_in_meters = value * conversions[from_unit]
    converted_value = value_in_meters / conversions[to_unit]
    return converted_value

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    to_celsius = {
        'Celsius': lambda Value: Value,
        'Fahrenheit': lambda Value: (Value - 32) * 5 / 9,
        'Kelvin': lambda Value: Value - 273.15
    }

    from_celsius = {
        'Celsius': lambda Value: Value,
        'Fahrenheit': lambda Value: (Value * 9 / 5) + 32,
        'Kelvin': lambda Value: Value + 273.15
    }

    value_in_celsius = to_celsius[from_unit](value)
    
    return from_celsius[to_unit](value_in_celsius)

def weigth_converter(value, from_unit, to_unit):
    conversion_values = {
        'Milligram': 1,
        'Gram': 1000,
        'Kilogram': 1e6,
        'Ounce': 28349.5,
        'Pound': 453592.37
    }
    weight_value = value * conversion_value[from_unit]
    converted_value = weight_value / conversion_values[to_unit]
    return converted_value

@app.route('/')
def home():
    return render_template('index.html')  

if __name__ == '__main__':
    app.run(debug=True) 