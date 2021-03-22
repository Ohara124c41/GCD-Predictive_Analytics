# import module 
import json 
import gcd

from IPython.display import Image
from IPython.core.display import HTML 

# create create_json function and hook

liked = True #True, False

@gcd.hookimpl  
def create_json(): 

    if liked:  
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
        return json.dumps(value) 

    else:
        pass 
  
    # dictionary to JSON Object using dumps() method 
    # return JSON Object 
print(create_json()) 
  
@gcd.hookimpl
def show_architecture(arch_image):

    if liked:  
        arch_image = display(Image('https://raw.githubusercontent.com/Ohara124c41/GCD-Predictive_Analytics/main/gdb/auto01/001.PNG', width=1900, unconfined=True))
        return arch_image
    else:
      pass

@gcd.hookimpl
def show_gdb(gdb_image):

    if liked:  
        gdb_image = display(Image('https://raw.githubusercontent.com/Ohara124c41/GCD-Predictive_Analytics/main/gdb/auto01/004.png', width=1900, unconfined=True))
        return gdb_image
    else:
      pass
