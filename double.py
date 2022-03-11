def doubler(func):
    def double():
        func()
        func()
    return double()
