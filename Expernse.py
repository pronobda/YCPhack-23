class expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"<Expnse: {self.name}, {self.category}, ${self.amount:.2f}>"
