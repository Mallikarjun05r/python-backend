from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Temporary database (list)
payments = []


# Create Payment
@app.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()

    payment = {
        "id": str(uuid.uuid4()),
        "customer_name": data.get("customer_name"),
        "amount": data.get("amount"),
        "payment_method": data.get("payment_method"),
        "status": "SUCCESS"
    }

    payments.append(payment)

    return jsonify({
        "message": "Payment created successfully",
        "payment": payment
    }), 201


# Get All Payments
@app.route('/payments', methods=['GET'])
def get_all_payments():
    return jsonify(payments), 200


# Get Payment By ID
@app.route('/payments/<payment_id>', methods=['GET'])
def get_payment(payment_id):
    for payment in payments:
        if payment["id"] == payment_id:
            return jsonify(payment), 200

    return jsonify({"message": "Payment not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)