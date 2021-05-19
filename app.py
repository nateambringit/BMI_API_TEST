from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('height', required = True)
parser.add_argument('weight', required=True)
bmi = {}


class BMI(Resource):
    def __init__(self):
        self.__init__height = parser.parse_args().get('height', None)
        self.__init__weight = parser.parse_args().get('weight',None)

    def get(self):
        try:
            height = float(parser.parse_args().get('height'))
            weight = float(parser.parse_args().get('weight'))
        except ValueError:
            response = {
                "statusCode": 200,
                "bmi": "-",
                "label":"-",
                "message":"Value can't be strings"
            }
            return response
        if (height<=0) or (weight<=0):
            response = {
                "statusCode": 200,
                "bmi": "-",
                "label":"-",
                "message":"Value can't be zero or negative"
            }
            return response
        bmi = round(weight/(height/100)**2,2)

        if(bmi>=18.5) and (bmi<=24.9):
            response = {
            "statusCode": 200,
            "bmi": bmi,
            "label":"normal",
            "message": "success"
        }
        elif(bmi>=25):
            response = {
            "statusCode": 200,
            "bmi": bmi,
            "label":"overweight",
            "message": "success"
        }
        elif(bmi<25):
            response = {
            "statusCode": 200,
            "bmi": bmi,
            "label":"underweight",
            "message": "success"
            }
        else:
            response = {
            "statusCode": 200,
            "bmi": bmi,
            "label":"unclassified",
            "message": "success"
        }
        return response

api.add_resource(BMI, '/')


if __name__ == '__main__':
    app.run()
