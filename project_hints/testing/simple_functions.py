def function_1():
    return "Output for function 1."


def function_2():
    return "Correct output for function 2."


def function_3(name):
    if type(name) == type(int(name)):
        return (f"x = {name}")
    else:
        return (f"x = {name:0.2f}")

def function_4(x, y):
    return float(x) + float(y)

