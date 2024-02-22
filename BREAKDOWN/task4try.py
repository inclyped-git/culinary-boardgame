class Restaurant:
    
    RESTAURANT_TYPES = ['Desserts & Beverages', 'Farm-to-Table', 'Fusion Cuisine', 'Fast Food']
    
    def __init__(self, restaurant_name, restaurant_type, restaurant_price, board_position):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.restaurant_price = restaurant_price
        self.board_position = board_position
        self.managers_list = []
        
    get_restaurant_name = lambda self: self.restaurant_name
    get_restaurant_type = lambda self: self.restaurant_type
    get_restaurant_price = lambda self: self.restaurant_price
    get_board_position = lambda self: self.board_position
    get_managers_list = lambda self: self.managers_list
    
    has_manager_availability = lambda self: len(self.get_managers_list()) < 3
    
    
    # need to edit this part for joining managers together.
    def add_new_comanager(self, manager):
        self.get_managers_list().append(manager)
        
        if len(self.get_managers_list()) == 3:
            if self.get_managers_list()[2] == self.get_managers_list()[0]:
                temp = self.get_managers_list()[1]
                self.get_managers_list()[1] = self.get_managers_list()[2]
                self.get_managers_list()[2] = temp
    
    has_sole_manager = lambda self: len( list( set( self.get_managers_list()) ) ) == 1
    
    def get_managerial_share(self, manager):
        sumManagerialShare = 0
        if manager in self.managers_list:
            for i in range(len(self.get_managers_list())):
                if self.get_managers_list()[i] == manager and i == 0:
                    sumManagerialShare += 40
                elif self.get_managers_list()[i] == manager:
                    sumManagerialShare += 30
        return sumManagerialShare
    
    def __str__(self):
        return f"{self.get_restaurant_name()}"
            
    __repr__ = lambda self: self.__str__()