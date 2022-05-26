#create class 
class FootballTeam:

    #define attributes
    #Variable : DataType

    #initialise the class
    def __init__(self,stadium,location):
        self.__stadium = stadium
        self.__location = location

    #getter functions
    def GetStadium(self):
        return self.__stadium

    def GetLocation(self):
        return self.__location

    #setter functions
    def SetStadium(self):
        stadium = input("Enter home stadium: ")
        self.__stadium = stadium

    def SetLocation(self):
        location = input("Enter location of team: ")
        self.__location = location
    
#array of 3 football teams 
teams = []
for i in range(3):
    team = input("enter football team: ")
    team = FootballTeam("","")#initiating the stadium and location param to empty strings, they will be overwritten with setters
    stadium = team.SetStadium()
    location = team.SetLocation()
    teams.append(team)

#accessing stadium of team[0]
print(teams[0].GetStadium())

#inheritance
class player(FootballTeam):
    def __init__(self, stadium, location):
        super().__init__(stadium, location) #inheriting the values from the FootballTeam class
        self.__wage = 0
        

    def SetWage(self):
        wage = int(input("Enter total player wages per month: "))
        self.__wage = wage
    
    def GetWage(self):
        return self.__wage

Burnley = player("Turf More","North-West England")
Burnley.SetWage()
print(f"Total wages per month for Burnley: {Burnley.GetWage()}")