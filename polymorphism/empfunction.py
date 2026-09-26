class Developer:
    def work(self):
        print("Developer is coding.")


class Tester:
    def work(self):
        print("Tester is testing.")


class Manager:
    def work(self):
        print("Manager is managing.")


def assign_work(employee):
    employee.work()


assign_work(Developer())
assign_work(Tester())
assign_work(Manager())