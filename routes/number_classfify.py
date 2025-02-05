import asyncio

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
        if not query_parameters:
            return {"number": "", "error": True}, 400
        try:
            number = int(query_parameters)
            parsed_int = number
            fun_fact = asyncio.run(get_fun_fact(parsed_int))
            sum_of_digits = asyncio.run(sum_digits(parsed_int))
            check_prime = asyncio.run(is_prime(parsed_int))
            check_perfect = asyncio.run(is_perfect(parsed_int))
            properties = asyncio.run(check_properties(parsed_int))

            # print(sum_of_digits)
            return {"number": number, "is_prime": check_prime,  "is_perfect": check_perfect, "properties": properties, "digit_sum": sum_of_digits, "fun_fact": fun_fact}, 200
        except ValueError:
            return {"number": query_parameters, "error": True}, 400
        except Exception as e:
            print(e)
            return {"number": query_parameters, "error": True}, 400
