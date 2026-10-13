from flask import Flask, jsonify

app = Flask(__name__)


employees = [
    {
        "id": 1,
        "name": "Anas Qureshi",
        "role": "DevOps Engineer"
    },
    {
        "id": 2,
        "name": "Rahul Sharma",
        "role": "Python Developer"
    },
    {
        "id": 3,
        "name": "Priya Patil",
        "role": "Cloud Engineer"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Employee Management API",
        "deployment": "Jenkins + Docker + AWS EC2",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/employees")
def get_employees():
    return jsonify(employees)


@app.route("/employees/<int:employee_id>")
def get_employee(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return jsonify(employee)

    return jsonify({
        "error": "Employee not found"
    }), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)