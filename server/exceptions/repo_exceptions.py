class UniqFieldException(Exception): #Exception es de Python
    def __init__(self, *args):
        super().__init__(*args)