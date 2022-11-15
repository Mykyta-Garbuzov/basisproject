from flask import Flask, request, jsonify
import connexion

app = connexion.App(__name__, specification_dir="./")

app.add_api("swagger.yml")



@app.route("/")
def home():
    return jsonify({"Message":"This is your flask app with docker"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)