# Define a class to simulate a person's day
class PersonDaySimulator:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.hunger = 0
        self.hygiene = 100
        self.mood = "Happy"
    
    def wake_up(self):
        self.energy -= 10
        self.hunger += 5
        self.hygiene -= 5
        self.mood = "Tired"
        print(f"{self.name} wakes up. Energy: {self.energy}, Hunger: {self.hunger}, Hygiene: {self.hygiene}, Mood: {self.mood}")

    def eat_breakfast(self):
        self.energy += 20
        self.hunger -= 20
        self.mood = "Happy"
        print(f"{self.name} eats breakfast. Energy: {self.energy}, Hunger: {self.hunger}, Mood: {self.mood}")

    def work(self):
        self.energy -= 30
        self.hunger += 10
        self.mood = "Stressed"
        print(f"{self.name} works. Energy: {self.energy}, Hunger: {self.hunger}, Mood: {self.mood}")

    def eat_lunch(self):
        self.energy += 15
        self.hunger -= 15
        self.mood = "Content"
        print(f"{self.name} eats lunch. Energy: {self.energy}, Hunger: {self.hunger}, Mood: {self.mood}")

    def relax(self):
        self.energy += 10
        self.hunger += 5
        self.mood = "Relaxed"
        print(f"{self.name} relaxes. Energy: {self.energy}, Hunger: {self.hunger}, Mood: {self.mood}")

    def sleep(self):
        self.energy = 100
        self.hunger += 5
        self.hygiene -= 10
        self.mood = "Sleepy"
        print(f"{self.name} goes to sleep. Energy: {self.energy}, Hunger: {self.hunger}, Hygiene: {self.hygiene}, Mood: {self.mood}")

# Create a person
person = PersonDaySimulator("John")

# Simulate a day
person.wake_up()
person.eat_breakfast()
person.work()
person.eat_lunch()
person.relax()
person.sleep()
