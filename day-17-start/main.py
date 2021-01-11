class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def __priv_method(self):
        self.id += 1


user1 = User(3, "Ash")

print(user1.id)
