class User():
    def __init__(self, id, name, index, consume_profile, produce_profile):
        self.id = id
        self.name = name
        self.index = index
        self.color = "black"
        self.produce_profile = produce_profile
        self.consume_profile = consume_profile
        self.lights = []

    def update_color(self, color):
        self.color = color
        for light in self.lights:
            light["color"] = color

USERS = [
    User("30aa4c7f-faa4-4941-968f-3b024a5f1efe", "spannungsteiler", 1, "MisterX", "Level1"),
    User("9c55ac05-e4b5-47e5-8596-9ac7346e84ff", "stromteiler", 3, "Student", "Level7")
]
