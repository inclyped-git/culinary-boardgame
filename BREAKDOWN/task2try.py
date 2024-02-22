from DATA1 import board_size as boardSize1
from DATA2 import board_size as boardSize2

from DATA1 import delimiter as del1
from DATA2 import delimiter as del2

from DATA1 import csv_data as csv1
from DATA2 import csv_data as csv2

def retrieve_restaurant_details(data, delimiter, board_size):

    titles = data[0].split(delimiter)
    
    nameIndex = titles.index('Restaurant Name')
    typeIndex = titles.index('Type')
    priceIndex = titles.index('Price')
    positionIndex = titles.index('Board Position')
    
    finalDict = {}
    
    bigData = data[1:]
    
    offset = 0
    for i in range(len(bigData)):
        data = bigData[i].split(delimiter)
        value = [data[nameIndex], data[typeIndex], data[priceIndex]]
        key = int(data[positionIndex]) + offset
        
        if key % (board_size - 1) == 0 and key > 0 and key < board_size**2 -1:
            finalDict[key + 1] = value
            offset += 1
        else:
            finalDict[key] = value
        

    print(finalDict)
        
        
retrieve_restaurant_details(csv2, del2, boardSize2)