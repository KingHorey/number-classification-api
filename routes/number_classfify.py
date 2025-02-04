from flask_restful import Resource
from flask import request

from utils.sum_digits import sum_digits
from utils.check_prime import is_prime
from utils.check_perfect import is_perfect
from utils.number_properties import check_properties
from utils.fetch_fun_fact import get_fun_fact


class GetNumberInfo(Resource):

    def get(self):
        """
                get method to get info about number
        """
        query_parameters = request.args.get('number')
        # print(query_parameters)
        number = query_parameters.isdigit()
        parsed_int = int(query_parameters)

        if not number:
            return {"number": "alphabet", "error": True}, 400
        sum_of_digits = sum_digits(parsed_int)
        check_prime = is_prime(parsed_int)
        check_perfect = is_perfect(parsed_int)
        properties = check_properties(parsed_int)
        fun_fact = get_fun_fact(parsed_int)

        # print(sum_of_digits)
        return {"number": query_parameters, "is_prime": check_prime,  "is_perfect": check_perfect, "properties": properties, "digit_sum": sum_of_digits, "fun_fact": fun_fact}, 200
