import random
import json

json_object["id"] = "001"
json_object["labels"] = "Architecture"

y1 = random.randint(1, 5)
y2 = random.randint(1, 5)
y3 = random.randint(1, 5)

auto_qual_scores = {'synergy': y1, 'usability': y2, 'maturity': y3}
json_object["agent2-qual-metrics"] = auto_qual_scores

## Design Decisions for synergy
if y1 >= 4:  
  json_object["DD1"] = "synergy is good"
elif y1 <= 2:
  json_object["DD1"] = "synergy is bad"
else:
  json_object["DD1"] = "synergy is nominal"

## Design Decisions for usability
if y2 >= 4:  
  json_object["DD2"] = "usability is good"
elif y2 <= 2:
  json_object["DD2"] = "usability is bad"
else:
  json_object["DD2"] = "usability is nominal"

## Design Decisions for maturity
if y3 >= 4:  
  json_object["DD3"] = "maturity is good"
elif y3 <= 2:
  json_object["DD3"] = "maturity is bad"
else:
  json_object["DD3"] = "maturity is nominal"

## Pseudo assessment criteria
score = y1 + y2 + y3

if score > 12:
  json_object["Assessment"] = "This architecture is excellent, the SCORE is %d" % (score)
elif score < 6:
  json_object["Assessment"] = "This architecture is unacceptable, the SCORE is %d" % (score)
else:
  json_object["Assessment"] = "This architecture is considerable, the SCORE is %d" % (score)

a_file = open("ARCH01.json", "w")
json.dump(json_object, a_file, indent=4)
a_file.close()
