from flask import Flask, request, jsonify
from company_data_extraction.main import gather_company_info

app = Flask(__name__)

@app.route("/api/company_info", methods=["POST"])
def get_company_info():
    data = request.json
    company_name = data.get("company_name")

    if not company_name:
        return jsonify({"error": "Company name is required"}), 400

    try:
        company_info = gather_company_info(company_name)
        return jsonify({"company_info": company_info})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
