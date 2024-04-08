# Coleman Petras
# M03 Lab
# M03 Collaboration
# This program is designed to take input from a customer and output the vehicle information based on the inputs in an easy to read format

# Define the Vehicle superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define the Automobile class that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Function to accept user input for a car
def get_car_details():
    vehicle_type = input("Enter the vehicle type as car: ")
    while vehicle_type != "car":
        vehicle_type = input("Enter the vehicle type as car: ")
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = int(input("Enter the number of doors (2 or 4): "))
    while doors != 2 and doors != 4:
        doors = int(input("Enter the number of doors (2 or 4): "))
    roof = input("Enter the type of roof (solid or sun roof): ")
    while roof != "sun roof" and roof != "solid":
        roof = input("Enter the type of roof (solid or sun roof): ")
    
    return Automobile(vehicle_type, year, make, model, doors, roof)

# Main program
def main():
    car = get_car_details()
    print("\nVehicle details:")
    print("  Vehicle type:", car.vehicle_type)
    print("  Year:", car.year)
    print("  Make:", car.make)
    print("  Model:", car.model)
    print("  Number of doors:", car.doors)
    print("  Type of roof:", car.roof)

if __name__ == "__main__":
    main()
