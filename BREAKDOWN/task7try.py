from DATA1 import board_size as boardSize1
from DATA2 import board_size as boardSize2

from DATA1 import delimiter as del1
from DATA2 import delimiter as del2

from DATA1 import csv_data as csv1
from DATA2 import csv_data as csv2

class RestaurantManager:
    """
    Description: RestaurantManager is a class that contains the attributes of a manager -
    their name, their symbol, their bitecoins, the number of restaurants managed, and 
    what positions they currently own.
    """
    INITIAL_CAPITAL = 1000
    
    def __init__(self, name: str):
        """
        Description: Constructor for the RestaurantManager class.
        
        Parameters:
        @param str name: String that is the name of the restaurant manager.
        """
        self.name = name
        self.symbol = self.name.upper()[0]
        self.bitecoins = RestaurantManager.INITIAL_CAPITAL
        self.restaurants_managed = []
        self.manager_positions = []
    
    # set of getters.
    def get_name(self) -> str:
        """
        Description: Getter method for the instance variable "name".

        Returns:
        @return str: The name of the manager.
        """
        return self.name

    def get_symbol(self) -> str:
        """
        Description: Getter method for the instance variable "symbol".

        Returns:
        @return str: The starting character of the manager's name.
        """
        return self.symbol
    
    def get_bitecoins(self) -> int:
        """
        Description: Getter method for the instance variable "bitecoins".
        
        Returns:
        @return int: The number of bitecoins the manager currently has.
        """
        return self.bitecoins

    
    def get_restaurants_managed(self) -> list:
        """
        Description: Getter method for the instance variable "restaurants_managed"

        Returns:
        @return list: A list of restaurants the manager manages.
        """
        return self.restaurants_managed

    def get_manager_positions(self) -> list:
        """
        Description: Getter method for the instance variable "manager_positions"

        Returns:
        @return list: A list of positions the manager owns.
        """
        return self.manager_positions

    
    # set of updators and retrievers
    def update_bitecoins(self, coins: int):
        """
        Description: Updates the bitecoins the manager has.

        Parameters:
        @param int coins: The number of coins lost or gained by the manager.
        """
        self.bitecoins = self.get_bitecoins() + coins
        
    
    def update_position(self, pos: int):
        """
        Description: Appends the latest position the manager owns.

        Parameters:
        @param int pos: The new position the manager has occupied.
        """
        self.get_manager_positions().append(pos)
    
    def get_current_position(self) -> int:
        """
        Description: Returns the current position of the manager.

        Returns:
        @return int: The position of the manager.
        """
        return self.get_manager_positions()[-1]
    
    
    def undo_position(self) -> int:
        """
        Description: 

        Returns:
        @return int: The previous position the manager was in.
        """
        self.manager_positions = self.get_manager_positions()[:-1]
        return self.get_manager_positions()[-1]
    
    def update_restaurants_managed(self, restaurant: object):
        """
        Description: Appends the restaurant the manager owns.

        Parameters:
        @param Restaurant restaurant: The restaurant object that the manager owns.
        """
        if restaurant not in self.get_restaurants_managed():
            self.get_restaurants_managed().append(restaurant)
    
    # string rep functions
    def __str__(self) -> str:
        """
        Description: A function that represents the details of the restaurant manager object.

        Returns:
        @return str: A string that contains details of the RestaurantManager object.
        """
        return f"{self.get_name()} has {self.get_bitecoins()} BiteCoins and manages {len(self.get_restaurants_managed())} restaurant(s)"
    
    def __repr__(self) -> object:
        """
        Description: __repr__() function calls the __str__() function.

        Returns:
        @return str: A string that is returned by __str__() function.
        """
        return self.__str__()

    def buy_restaurant(self, restaurantsDictionary: dict, boardPosition: int) -> str:
        restaurantDetails = restaurantsDictionary[boardPosition] # gets the list of restaurant details.
        
        # checking if the value stored in the dictionary is a list or object.
        if isinstance(restaurantDetails, list):
            # if its a list,
            if self.get_bitecoins() < int(restaurantDetails[2]): # if the manager cannot afford the restaurant, it does not convert to a restaurant object.
                return f"{self.get_name()} does not have enough money to afford {restaurantDetails[0]}"
            else:
                restaurantsDictionary[boardPosition] = Restaurant(restaurantDetails[0], restaurantDetails[1], restaurant_price=int(restaurantDetails[2]), board_position=boardPosition)
                self.update_restaurants_managed(restaurantsDictionary[boardPosition])
                self.update_position(boardPosition)
                self.update_bitecoins(-restaurantsDictionary[boardPosition].get_restaurant_price())
                restaurantsDictionary[boardPosition].add_new_comanager(self)
                
                return f"{self.get_name()} becomes the first manager of {restaurantsDictionary[boardPosition].get_restaurant_name()}"
        
        else:
            # if its already an object,
            if not (restaurantsDictionary[boardPosition].has_manager_availability()):
                return f"{restaurantsDictionary[boardPosition].get_restaurant_name()} is no longer available"
            else:
                if self.get_bitecoins() < restaurantsDictionary[boardPosition].get_restaurant_price():
                    return f"{self.get_name()} does not have enough money to afford {restaurantsDictionary[boardPosition].get_restaurant_name()}"
                else:
                    self.update_restaurants_managed(restaurantsDictionary[boardPosition])
                    self.update_position(boardPosition)
                    self.update_bitecoins(-restaurantsDictionary[boardPosition].get_restaurant_price())
                    restaurantsDictionary[boardPosition].add_new_comanager(self)
                    
        
        # we need to consider cases where the manager is either head, co- or sole.
        if (restaurantsDictionary[boardPosition].has_sole_manager()):
            if restaurantsDictionary[boardPosition].get_managerial_share(self) == 100:
                return f"{self.get_name()} becomes a sole manager of {restaurantsDictionary[boardPosition].get_restaurant_name()}"
            else:
                return f"{self.get_name()} becomes the head manager of {restaurantsDictionary[boardPosition].get_restaurant_name()}"
        
        else:
            if restaurantsDictionary[boardPosition].get_managerial_share(self) >= 60:
                return f"{self.get_name()} becomes the head manager of {restaurantsDictionary[boardPosition].get_restaurant_name()}"
            else:
                return f"{self.get_name()} becomes co-manager of {restaurantsDictionary[boardPosition].get_restaurant_name()}"
                    
            
    def display_restaurants_managed(self):
        finalString = ""
        totalBitecoins = 0
        totalSharesWorth = 0
        
        for index in range(len(Restaurant.RESTAURANT_TYPES)):
            isFirst = True
            numberOfRestaurantList = 1
            
            for restaurant in self.get_restaurants_managed():
                
                if restaurant.get_restaurant_type() == Restaurant.RESTAURANT_TYPES[index]:
                    if isFirst: 
                        finalString += Restaurant.RESTAURANT_TYPES[index].upper() + "\n"
                        finalString += f"{numberOfRestaurantList}. {restaurant.get_restaurant_name()} ({restaurant.get_restaurant_price()} BiteCoins, {restaurant.get_managerial_share(self)}%)" + "\n"
                        numberOfRestaurantList += 1
                        totalBitecoins += restaurant.get_restaurant_price() * int ( restaurant.get_managerial_share(self) / 30 )
                        totalSharesWorth += restaurant.get_restaurant_price() * ( restaurant.get_managerial_share(self) / 100 )
                        isFirst = False
                    else:
                        finalString += f"{numberOfRestaurantList}. {restaurant.get_restaurant_name()} ({restaurant.get_restaurant_price()} BiteCoins, {restaurant.get_managerial_share(self)}%)" + "\n"
                        numberOfRestaurantList += 1
                        totalBitecoins += restaurant.get_restaurant_price() * int ( restaurant.get_managerial_share(self) / 30 )
                        totalSharesWorth += int (restaurant.get_restaurant_price() * ( restaurant.get_managerial_share(self) / 100 ))
        

        print(finalString + f"OVERALL\nRestaurants worth {totalBitecoins} BiteCoins\nManagerial share worth {totalSharesWorth} BiteCoins")    
                    
    def lose_bitecoins(self, restaurantsDictionary):
        restaurantDetail = restaurantsDictionary[self.get_current_position()]
        
        bitecoinsToLose = round(restaurantDetail.get_restaurant_price() * 0.5 + 0.1)
        self.update_bitecoins(-bitecoinsToLose)
        
        listOfManagers = list ( set (restaurantDetail.get_managers_list()) )
        for manager in listOfManagers:
            moneyGained = round ( (restaurantDetail.get_managerial_share(manager)/100) * bitecoinsToLose + 0.1 )
            manager.update_bitecoins(moneyGained)        
           
    def check_winning_conditions(self, numOfRestaurants=4,avgManagerialShare=0,numOfTypes=3):
        # checking if the number of restaurants owned meets the criteria.
        if not len(self.get_restaurants_managed()) >= numOfRestaurants:
            return False
        
        # checking if the average managieral share meets the criteria.
        listOfShares = [ restaurant.get_managerial_share(self) for restaurant in self.get_restaurants_managed() ]
        average = sum(listOfShares) / len(listOfShares)
        
        if not average >= avgManagerialShare:
            return False
        
        # checking if the types of restaurants meet the criteria.
        numOfTypesOwned = len(list(set([ restaurant.get_restaurant_type() for restaurant in self.get_restaurants_managed() ])))
        if not numOfTypesOwned >= numOfTypes:
            return False
        
        return True

    def get_next_positions(self, detailsDictionary):
        currentRestaurant = detailsDictionary[self.get_current_position()]