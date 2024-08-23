from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = eval(expression)
        if result / 1 == 0:
            integer = int(result)
            final_res = str(integer) + "/1"
            return final_res
        else:
            fraction = Fraction(result).limit_denominator()
            return f"{fraction.numerator}/{fraction.denominator}"
            
