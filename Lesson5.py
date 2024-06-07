# 1. შექმენი ტრანსპორტის კლასი მინიმუმ 4 კლასის პარამეტრით

class Transport:
    speed= 80
    distance=60
    release_year=2012
    country='Japan'

# 4. დაამატე __init__ magic მეთოდი და მინიმუმ 3 ობიექტის
# პარამეტრი.
    def __init__(self, name, color, height, width, length):
        self.name=name
        self.color=color
        self.width=width
        self.height=height
        self.length=length

# 2. დაამატე ერთი სტატიკური მეთოდი.
    @staticmethod
    def moving():
        print('I am moving')

# 3. დაამატე ორი კლასის მეთოდი.
    @classmethod
    def time(cls):
        print(f'Travel time is {cls.distance/cls.speed}')

    @classmethod
    def speed_to_mps(cls):
        print(cls.speed * 1000/3600)


# 5. დაამატე მინიმუმ 2, ობიექტის მეთოდი.
    def info(self):
        print(f"Transport: {self.name}")
        print(f"Color: {self.color}")
        print(f"Length: {self.length}")
        print(f"height: {self.height}")
        print(f"Width: {self.width}")

    def volume(self):
        print(self.length*self.width*self.height)


# 6. დაამატე __repr__ magic მეთოდი
    def __repr__(self):
        return f"Transport(name='{self.name}', color={self.color}, width='{self.width}', height={self.height}, length={self.length}')"

# 7. ზემოხსენებული კლასისგან შექმენი მინიმუმ 5 ობიექტი და
# გამოიძახე მისი ზოგიერთი მეთოდი და პარამეტრი.

car=Transport("car", "red", 140, 180, 450)
bicycle=Transport("bicycle", "Blue", 120, 70, 180)
train=Transport("Train", "Black", 400, 300, 800)
plane=Transport("Plane", "White", 600, 450, 1200)
boat=Transport("Boat", "Yellow", 200, 250, 800)

car.volume()
bicycle.info()
train.speed_to_mps()
boat.time()
print(plane.length)