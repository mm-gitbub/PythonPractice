class Cake:
    recipe_type = "Basic Cake"
    baking_temperature = 180
    baking_time = 30

    def __init__(self, flour, sugar, milk, eggs):
        self.cake_flour = flour
        self.cake_sugar = sugar
        self.cake_milk = milk
        self.cake_eggs = eggs

    def mix_ingredients(self):
        print(f"Mixing of {self.cake_flour} grams of flours, {self.cake_sugar} grams of sugar, {self.cake_milk} ml of milk and {self.cake_eggs} eggs")

    def bake(self):
        print(f"Baking the cake at {self.baking_temperature} degree C for {self.baking_time} minutes")

    def serve(self):
        print("Serving the cake with decoration")

class Bakery():

    def __init__(self, name):
        self.bakery_name = name

    def prepare_cake(self, cake):
        print(f"Preparing a cake at {self.bakery_name}.")
        cake.mix_ingredients()
        cake.bake()
        cake.serve()

# Create the instance of Cake class with passing the arguments
cake_1 = Cake(200, 300, 230, 2)
cake_2 = Cake(250, 200, 260, 2)

bakery_1 = Bakery("Madhu Delish Cafe")

# Using bakery_1 instance to bake cake_1
bakery_1.prepare_cake(cake_1)
bakery_1.prepare_cake(cake_2)
print("The end.")






