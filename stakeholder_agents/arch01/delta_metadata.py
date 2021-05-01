import random



json_object["id"] = "001"
json_object["labels"] = "Architecture"

y1 = random.randint(1, 5)
y2 = random.randint(1, 5)
y3 = random.randint(1, 5)


json2 = {'synergy': y1, 'usability': y2, 'maturity': y3}
json_object["agent2-qual-metrics"] = json2

## Design Decisions for synergy
if y1 >= 4:  
  json_object["DD1"] = "synergy is good"

if y1 <= 2:
  json_object["DD1"] = "synergy is bad"

if y1 == 3:
  json_object["DD1"] = "synergy is nominal"

## Design Decisions for usability

if y2 >= 4:  
  json_object["DD2"] = "usability is good"

if y2 <= 2:
  json_object["DD2"] = "usability is bad"

if y2 == 3:
  json_object["DD2"] = "usability is nominal"

## Design Decisions for maturity

if y3 >= 4:  
  json_object["DD3"] = "maturity is good"

if y3 <= 2:
  json_object["DD3"] = "maturity is bad"

if y3 == 3:
  json_object["DD3"] = "maturity is nominal"

## Pseudo assessment criteria

if y1 + y2 + y3 > 12:
  json_object["Assessment"] = "This architecture is excellent"

if y1 + y2 + y3 < 6:
  json_object["Assessment"] = "This architecture is unacceptable"

if 12 > y1 + y2 + y3 > 6:
  json_object["Assessment"] = "This architecture is unacceptable"

a_file = open("designer01.json", "w")
json.dump(json_object, a_file)
a_file.close()
