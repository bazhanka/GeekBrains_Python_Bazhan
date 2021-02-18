class Worker:
    def __init__(self, name,surname,position,wage,bonus):
        self.name=name
        self.surname=surname
        self.position=position
        self.income= {'wage':wage, 'bonus':bonus}
class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(int(self.income['wage'])+int(self.income['bonus']))
it=Position('Peter','Popov', 'IT',12300,900)
it.get_full_name()
it.get_total_income()
