from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/application-form")
def start():
    
    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def applicationForm():    
    f_name = request.form.get("first_name")
    l_name = request.form.get("last_name")
    salary = request.form.get("salary_requirement")
    job = request.form.get("job_type")

    return render_template("application.html", first_name=f_name, last_name=l_name, salary=salary, job=job )


if __name__ == "__main__":
    app.run(debug=True)