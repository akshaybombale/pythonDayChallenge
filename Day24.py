class Cardesign:
    followers = 0
    def __init__(self, CarName, CarPrice):
        self.name = CarName
        self.price = CarPrice
        # print(f"car name is {self.name} and its price is {self.price} with {self.followers} followers")
    
    def Update_Price(self, Car_name, Updateprice):
        print(f"now My {Car_name} price is {Updateprice}")
     
        
        

car_1 = Cardesign("creta", 700000)
car_2 = Cardesign("nexon", 100000)

print(f"car name is {car_1.name} and its price is {car_2.price} with {car_1.followers} followers")
print(f"car name is {car_2.name} and its price is {car_2.price}")

car_1.Update_Price("xuv 400", 80000) #here if you just call function then also fine or you can do like print(car_1.Update_Price(80000)) but you will get none also


#Exercise area and circumstance of circle
class Circle:
    Pi = 3.14
    def __init__(self, radius):
        self.Circle_redius = radius
    
    def get_Area(self):
        area = self.Pi * self.Circle_redius ** 2 
        return area
    def get_Circumferance(self):
        return  2 * self.Pi * self.Circle_redius


obj1 =  Circle(5)
print("circumferance is: ",+ obj1.get_Area())
print("Area is: ",+ obj1.get_Circumferance()) 