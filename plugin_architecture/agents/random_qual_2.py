import random
import json
import os


a_file = open("ARCH01.json", "r")
json_object = json.load(a_file)
a_file.close()
print(json_object)


y1 = random.randint(1, 5)
y2 = random.randint(1, 5)
y3 = random.randint(1, 5)
auto_qual_scores = {'synergy': y1, 'usability': y2, 'maturity': y3}
json_object["agent2-qual-metrics"] = auto_qual_scores

def dd_synergy():
  if y1 >= 4:  
    json_object["A2-DD1"] = "synergy is good"
  elif y1 <= 2:
    json_object["A2-DD1"] = "synergy is bad"
  else:
    json_object["A2-DD1"] = "synergy is nominal"
dd_synergy()


## Design Decisions for usability
if y2 >= 4:  
  json_object["A2-DD2"] = "usability is good"
elif y2 <= 2:
  json_object["A2-DD2"] = "usability is bad"
else:
  json_object["A2-DD2"] = "usability is nominal"

## Design Decisions for maturity
if y3 >= 4:  
  json_object["A2-DD3"] = "maturity is good"
elif y3 <= 2:
  json_object["A2-DD3"] = "maturity is bad"
else:
  json_object["A2-DD3"] = "maturity is nominal"

## Pseudo assessment criteria
score = y1 + y2 + y3

if score > 12:
  json_object["A2-Assessment"] = "This architecture is excellent, the SCORE is %d" % (score)
elif score < 6:
  json_object["A2-Assessment"] = "This architecture is unacceptable, the SCORE is %d" % (score)
else:
  json_object["A2-Assessment"] = "This architecture is considerable, the SCORE is %d" % (score)

a_file = open("ARCH01.json", "w")
json.dump(json_object, a_file, indent=4)
a_file.close()