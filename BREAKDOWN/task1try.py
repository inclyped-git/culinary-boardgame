
def printboard(n):
    print(" _____" * n)
    for j in range(n):
        for i in range(2):
            print("     ".join(['|'] * (n+1)))
        print("_____".join(['|'] * (n+1)))
        

def appendString(num, dictionary):
    finalString = ""
    for key in dictionary:
        lst = dictionary[key]
        
        if len(lst) == 0:
            finalString += "|" + "     "
        elif len(lst) == 1:
            finalString += "|" + f"  {lst[0]}  "
        elif len(lst) == 2:
            finalString += "|" + f"{lst[0]} {lst[1]}  "
        else:
            finalString += "|" + f"{lst[0]} {lst[1]} {lst[2]}"
        
        if (key + 1) % num == 0:
            finalString += "|\n"
    
    print(finalString)        
            
           
        
dictionary = {0: ['A'], 1: ['A','B'], 2: ['B'],
              3: ['C'], 4: ['B'], 5: ['A'],
              6: [], 7: [], 8: []}

appendString(3, dictionary)



def print_game_board(boardDimension, boardDictionary):
    listOfValues = []
    
    finalString = ""
    for key in boardDictionary:
        lst = boardDictionary[key]
        
        if len(lst) == 0:
            finalString += "|" + "     "
        elif len(lst) == 1:
            finalString += "|" + f"  {lst[0]}  "
        elif len(lst) == 2:
            finalString += "|" + f"{lst[0]} {lst[1]}  "
        else:
            finalString += "|" + f"{lst[0]} {lst[1]} {lst[2]}"
        
        if (key + 1) % boardDimension == 0:
            listOfValues.append(finalString + "|")
            finalString = ""
    
    print((" _____" * boardDimension))
    index = 0
    for key in boardDictionary:
        if (key + 1) % 3 == 0:
            
            if (key + 1) != len(boardDictionary) - 1:
                print("_____".join(['|'] * (boardDimension + 1)))
            else:
                print("_____".join(['|'] * (boardDimension + 1)))
        
        elif (key + 2) % 3 == 0:
            print(listOfValues[index])
            index += 1
        
        else:
            print("     ".join(['|'] * (boardDimension + 1)))