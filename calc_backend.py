# calc_backend.py
import math

def evaluate(expression):
    """
    Evaluates a simple mathematical expression safely.
    Supports +, -, *, /, sin, cos, tan, sqrt, log, etc.
    """
    try:
        # Replace common symbols
        expression = expression.replace('×', '').replace('÷', '/').replace('^', '*')

        # Evaluate using math module
        result = eval(expression, {"_builtins_": None}, vars(math))
        return result
    except Exception as e:
        return f"Error: {e}"