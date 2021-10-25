#Lukas Robin
#18.11.2019

#Kinematiclib.py
#This library contains all the functions needed to calculate kinematics
class KinematicLib:
    #constructor
    def __init__(self, distance, velocity, acceleration, time):
        self.velocity = velocity
        self.acceleration = acceleration
        self.distance = distance
        self.time = time

    #calculate_velocity
    def calculate_velocity(self):
        self.velocity = self.distance / self.time
    #calculate_acceleration
    def calculate_acceleration(self):
        self.acceleration = self.distance / self.time ** 2
    #calculate_distance
    def calculate_distance(self):
        self.distance = self.velocity * self.time
    #calculate_time
    def calculate_time(self):
        self.time = self.distance / self.velocity
    #calculate_all
    def calculate_all(self):
        self.calculate_velocity()
        self.calculate_acceleration()
        self.calculate_distance()
        self.calculate_time()
    #return all values
    def get_time(self):
        return self.time
    def get_distance(self):
        return self.distance
    def get_velocity(self):
        return self.velocity
    def get_acceleration(self):
        return self.acceleration
        
