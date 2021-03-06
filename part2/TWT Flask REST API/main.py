from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name, years):
        return {"data": f"Hello {name}, you are probably {years} years old"}

api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:years>")

if __name__ == "__main__":
    app.run(debug=True)