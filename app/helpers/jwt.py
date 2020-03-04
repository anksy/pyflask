class jwt:
    def __init__(self, function):
        self.function = function 
    
    def __call__(self, *args, **kwargs):
        print("before deco")
        self.function(*args, **kwargs) 
        print("after deco")
