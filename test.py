# Old way of defining functions before type hints were introduced in python3.5.
def greet_old(name):
    return "Hello, " + name


oldResult = greet_old("test")


# New way of defining functions after type hints were introduced.
def greet_new(name: str) -> str:
    return "Hello, " + name


newResult = greet_new("test2")
