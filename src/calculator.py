import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def sin(a,b):
    return (math.sin(a*math.pi/180),math.sin(b*math.pi/180))

def cos(a,b):
    return (math.cos(a*math.pi/180),math.cos(b*math.pi/180))

def tan(a,b):
    return (math.tan(a*math.pi/180),math.tan(b*math.pi/180))

def log(a,b):
    return (math.log(a,b))

def exp(a,b):
    return (math.pow(a,b))

def root(a,b):
    return (math.sqrt(a),math.sqrt(b))

if __name__ == "__main__":
    
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    # Single-value functions
    print(f"Addition of {a} and {b} is: {add(a, b):.3f}")
    print(f"Subtraction of {a} and {b} is: {sub(a, b):.3f}")
    print(f"Multiplication of {a} and {b} is: {mul(a, b):.3f}")
    print(f"Division of {a} and {b} is: {div(a, b):.3f}")
    print(f"Log of {a} upon {b} is: {log(a, b):.3f}")
    print(f"Exponent of {a} upon {b} is: {exp(a, b):.3f}")

    # Tuple-returning functions
    # Store the result in a temporary variable for clarity and easy access
    sines = sin(a, b)
    print(f"Sin of {a} and {b} are: ({sines[0]:.3f}, {sines[1]:.3f})")

    cosines = cos(a, b)
    print(f"Cosine of {a} and {b} are: ({cosines[0]:.3f}, {cosines[1]:.3f})")

    tangents = tan(a, b)
    print(f"Tan of {a} and {b} are: ({tangents[0]:.3f}, {tangents[1]:.3f})")

    roots = root(a, b)
    print(f"Square root of {a} and {b} are: ({roots[0]:.3f}, {roots[1]:.3f})")
