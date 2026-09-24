from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "veda-internship-secret-key"
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        email = request.form["email"]
        phone = request.form["phone"]
        city = request.form["city"]
        occupation = request.form["occupation"]

        flash("Profile created successfully!", "success")

        return render_template(
            "profile.html",
            name=name,
            age=age,
            email=email,
            phone=phone,
            city=city,
            occupation=occupation
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
