# defining that there are 100 cars
cars = 100
# defining that each car has 4 seats
 space_in_a_car = 4.0
# defining that there are 30 drivers
 drivers = 30
# defining that there are 90 passengers
 passengers = 90
# defining that all cars which don't have a driver will not be driven
 cars_not_driven = cars - drivers
#defining that all cars that have drivers are driven
 cars_driven = drivers
# defining the carpool capacity => 4 seats per car
 carpool_capacity = cars_driven * space_in_a_car
# defining the average amount of passengers per driven car
 average_passengers_per_car = passengers / cars_driven  
  
# printing the total amount of cars embeded in scentence
  print "There are", cars, "cars available."
# printing the amount of drivers embeded in scentence
  print "There are only", drivers, "drivers available."
# printing the the amount of cars which aeren't driven embeded in scentence
  print "There will be", cars_not_driven, "empty cars today."
# printing the total amout of people which could be transported embeded in scentence
  print "We can transport", carpool_capacity, "people today."
# printing the amount of passengers embeded in scentence
  print "We have", passengers, "to carpool today."
# printing the amount of people per car embeded in scentence
  print "We need to put about", average_passengers_per_car, "in each car."
# Just typing 4 instead of 4.0 for spaces per car would also work because there are no quater seats etc.
