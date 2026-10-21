
def calculate_travel_distance(tank_capacity, km_per_litre): 
    '''  
    This function calculates the distance a vehicle can travel based on tank  
    capacity (ie how many litres of fuel in tank) and the number of  
    kilometres a vehicle can travel per litre, and returns the  
    distance, rounded to two decimal points. 
    ''' 

    f_capacity = float(tank_capacity) 
    f_kml = float(km_per_litre) 
    distance = round(f_capacity * f_kml, 2) 
    return distance 