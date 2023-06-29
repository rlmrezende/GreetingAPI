# import Flask and jsonify
from flask import Flask, jsonify

# import Resource, Api and reqparser
from flask_restful import Resource, Api, request

app = Flask(__name__)

api = Api(app)

class Greet(Resource):
    def get(self):

        name = request.args.get('name')

        if name:
            greeting = f'Hello {name}!'
        else:
            greeting = 'Hello person without name!'

        # make json from greeting string 
        return jsonify(greeting=greeting)
    
    
# assign endpoint
api.add_resource(Greet, '/greet',)

if __name__ == '__main__':
    app.run(debug=True)
    
    