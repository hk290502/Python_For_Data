# create a dictionary of Wise Owl 

tallest_building = {

"1": ["Burj Khalifa","Dubai","UAE","828"],

"2": ["Merdeka","Canada","Toronto","212"],

"3": ["Shanghai Tower","Shanghai","China","828"]



}

# loop over dictionary's records

for tallest_building_name, x in tallest_building.items():
    print(x[0] + " in " + x[1] + " is " + x[3] + " meters high")
    
