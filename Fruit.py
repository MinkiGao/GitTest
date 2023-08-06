class Fruit():
    def __init__(self, catrgory, color):
        self.categry = catrgory
        self.color = color
    
    def print_fruit_info(self):
        print("fruit category:",self.categry)
        print("fruit color:",self.color)