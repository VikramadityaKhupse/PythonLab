# https://leetcode.com/problems/fraction-addition-and-subtraction/description/
class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Parse the expression using regex
        fractions = re.findall('[+-]?\\d+/\\d+', expression)
        
        numerator, denominator = 0, 1  # Initialize result as 0/1
        
        for frac in fractions:
            num, denom = map(int, frac.split('/'))
            
            # Common denominator logic
            numerator = numerator * denom + num * denominator
            denominator *= denom
            
            # Simplify the fraction
            gcd = math.gcd(numerator, denominator)
            numerator //= gcd
            denominator //= gcd
        
        # If the result is a whole number, return it as a fraction
        return f"{numerator}/{denominator}"


            
        