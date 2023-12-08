from funcs import read_file


def get_body_from_path(path):
    body = ""  # Better way to do this than to define
    print(path)
    path = path.split("?")[0]
    paramaters = ""
    try:
        paramaters = path.split("?")
    except Exception:
        print("No paramaters")
    body = "" # Better way to do this than to define

    try:
        if path == "/":
            body = "Yo"
        elif path == "/startproject":
            print(paramaters)
        elif path == "/compile":
            pass
        else:  # If
            body = "<!DOCTYPE html> <html><body><h1>Error 404: File Not Found</body></html>"

    except Exception as e:

        print(e)
        body = "<!DOCTYPE html> <html><body><h1>Error 500: Internal Server Error</body></html>"

    return bytes(body, 'utf-8')  # String now converted to bytes here


# Please put your own functions here :)


# TODO: Check for errors


# Shorthands:
get_body = get_body_from_path

GB = get_body_from_path
