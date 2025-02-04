from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from routes.number_classfify import GetNumberInfo

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


api.add_resource(GetNumberInfo, "/api/classify-number/")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
