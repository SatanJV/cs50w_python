from curses import wrapper


def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with decorating")
    return wrapper

@announce
def hello():
    print("Hello, world")

hello()