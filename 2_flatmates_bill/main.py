class Bill:
    """
    Object contains info regarding flatmate's bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate that pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatemate2):
        weight = self.days_in_house / (self.days_in_house + flatemate2.days_in_house)
        to_pay = bill * weight
        return to_pay


class PdfReport:
    """
    Creates a pdf of the itemised bill by flatmate
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


f1 = Flatmate("nathy", 20)
f2 = Flatmate("charlie", 25)

print(f1.pays(120, f2))
