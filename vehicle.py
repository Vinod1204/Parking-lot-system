class Vehicle:
    def __init__(self,reg_no,v_type):
        self.reg_no=reg_no
        self.v_type=v_type

    def __str__(self):
        return f"{self.v_type} {self.reg_no}"