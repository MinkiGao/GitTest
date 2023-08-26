class Animal():
    def __init__(self, category, region):
        self.category = category
        self.region = region
    
    def print_info(self):
        print("category:",self.category)
        print("region:",self.region)
