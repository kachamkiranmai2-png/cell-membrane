from flask import Flask, render_template, request

app = Flask(__name__)

# Class 9 educational dataset
data = [
    {"substance": "Oxygen", "size": "small", "charge": "neutral", "lipid_solubility": "high", "polarity": "low"},
    {"substance": "Carbon_Dioxide", "size": "small", "charge": "neutral", "lipid_solubility": "high", "polarity": "low"},
    {"substance": "Water", "size": "small", "charge": "neutral", "lipid_solubility": "low", "polarity": "high"},
    {"substance": "Glucose", "size": "large", "charge": "neutral", "lipid_solubility": "low", "polarity": "high"},
    {"substance": "Sodium_Ion", "size": "small", "charge": "positive", "lipid_solubility": "very low", "polarity": "high"},
    {"substance": "Potassium_Ion", "size": "small", "charge": "positive", "lipid_solubility": "very low", "polarity": "high"},
    {"substance": "Sucrose", "size": "large", "charge": "neutral", "lipid_solubility": "low", "polarity": "high"}
]

can_pass = {
    "Oxygen": "yes",
    "Carbon_Dioxide": "yes",
    "Water": "yes",
    "Glucose": "no",
    "Sodium_Ion": "no",
    "Potassium_Ion": "no",
    "Sucrose": "no"
}

explanations = {
    "Oxygen": "Oxygen is small and non-polar, so it can pass through the lipid part of the cell membrane.",
    "Carbon_Dioxide": "Carbon dioxide is small and non-polar, so it can pass through the cell membrane.",
    "Sodium_Ion": "Sodium ions have a positive charge and cannot easily cross the lipid part of the membrane without transport proteins.",
    "Potassium_Ion": "Potassium ions have a positive charge and need membrane transport proteins to cross the membrane.",
    "Glucose": "Glucose is relatively large and polar, so it cannot easily cross the lipid part of the membrane.",
    "Water": "Water is small and can cross the membrane. In cells, much water movement occurs through special proteins called aquaporins.",
    "Sucrose": "Sucrose is relatively large and polar, so it does not easily cross the lipid part of the membrane."
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected = request.form.get("substance", "")
    result = None

    if selected:
        row = next((item for item in data if item["substance"] == selected), None)
        if row:
            result = {
                "substance": selected.replace("_", " "),
                "can_pass": can_pass[selected],
                "size": row["size"].capitalize(),
                "charge": row["charge"].capitalize(),
                "lipid": row["lipid_solubility"].capitalize(),
                "polarity": row["polarity"].capitalize(),
                "explanation": explanations.get(selected, "")
            }

    return render_template(
        "index.html",
        substances=sorted(item["substance"] for item in data),
        selected=selected,
        result=result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
