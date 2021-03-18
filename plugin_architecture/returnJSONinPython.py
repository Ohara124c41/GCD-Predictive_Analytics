# import module 
import json 
  
# create architecture_components function   
def architecture_components(): 
  
    # define variables 
    Architecture = "ARC001"
    Designer = "C.O'Hara (1)"
    Rank = 1
    Score = 5
  
    # create dictionary 
    value = { 
        "architecture": Architecture, 
        "designer": Designer, 
        "rank": Rank, 
        "score": Score 
    } 
  
    # dictionary to JSON Object using dumps() method 
    # return JSON Object 
    return json.dumps(value) 
  
  
# call function and print it 
print(architecture_components()) 
