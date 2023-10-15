from flask import Flask, render_template, request

# Import your machine learning model here
import joblib

app = Flask(__name__)

# Load the machine learning model
model = joblib.load("Fertilizer.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        temperature = float(request.form.get("temperature"))
        humidity = float(request.form.get("humidity"))
        moisture = float(request.form.get("moisture"))
        soil_type = request.form.get("soil_type")
        crop_type = request.form.get("crop_type")
        nitrogen = float(request.form.get("nitrogen"))
        phosphorus = float(request.form.get("phosphorus"))
        potassium = float(request.form.get("potassium"))

        # Use your model to make a recommendation based on input data
        recommendation = model.predict([[temperature, humidity, moisture, soil_type, crop_type, nitrogen, phosphorus, potassium]])

        return render_template("index.html", recommendation=recommendation[0])

    return render_template("index.html", recommendation=None)

if __name__ == "__main__":
    app.run(debug=True)
