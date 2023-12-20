#!/usr/bin/python3
class CustomException(Exception):
    def __init__(self, message="Custom Exception"):
        super().__init__(message)

def raise_custom_exception():
    raise CustomException("This is a custom exception")

if __name__ == "__main__":
    try:
        raise_custom_exception()
    except CustomException as ce:
        print("Caught an exception: {}".format(ce))
