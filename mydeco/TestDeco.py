def mydeco(func):
    def inner():
        print("Executing before method execution ....")
        func()
        print("Executing after method execution ....")

    return inner

@mydeco
def test():
    print("Going to execute the method ...")


test()
