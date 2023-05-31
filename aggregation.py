

#% Creating Object outside and passing as a value



class Student:
    def __init__(self,name,age,clss,addr):
        self.name=name              
        self.age=age               
        self.standard=clss         
        self.Address_of_obj=addr   


    def Student_details(self):        
        print(f'Name of the student is {self.name}')
        print(f'Age of the student is {self.age}')
        print(f'{self.name} is studing in {self.standard}')
        self.Address_of_obj.display_address()

class Address:
    def __init__(self,city,district,state,country): 
        self.city=city                 
        self.district=district
        self.state=state
        self.country=country

        # city=input("Enter City Name: ")
        # district=input("Enter District Name: ")
        # state=input("Enter State Name: ")
        # country=input("Enter country Name: ")

    def display_address(self):
        print(f'Name of the City is {self.city}')
        print(f'Name of the District is {self.district}')
        print(f'Name of the State is {self.state}')
        print(f'Name of the Country is {self.country}')

## obj1=Address(city,district,state,country)
obj1=Address("Bhubaneswar","jagatsinghpur","Odisha","India")

pawan=Student("Pawan",18,"Graduation",obj1)
pawan.Student_details()
print()
print()
tushar=Student("Tushar",25,"MCA",obj1)
tushar.Student_details()











#% Creating Object inside the constructor of current class

class Address:
    def __init__(self,city,district,state,country):
        self.city=city
        self.district=district
        self.state=state
        self.country=country

    def display_address(self):
        print(f'Name of the City is {self.city}')
        print(f'Name of the District is {self.district}')
        print(f'Name of the State is {self.state}')
        print(f'Name of the Country is {self.country}')

class Student:
    def __init__(self,name,age,clss):
        self.Sname=name
        self.Sage=age
        self.Sstandard=clss
        city=input("Enter City Name: ")
        district=input("Enter District Name: ")
        state=input("Enter State Name: ")
        country=input("Enter country Name: ")
        obj1=Address(city,district,state,country)
        self.AddressObject=obj1

    def Student_details(self):
        print(f'Name of the student is {self.Sname}')
        print(f'Age of the student is {self.Sage}')
        print(f'{self.Sname} is studing in {self.Sstandard} class')
        self.AddressObject.display_address()

class Trainer:
    def __init__(self,name,age,sub):
        self.Tname=name
        self.Tage=age
        self.Tsubject=sub
        city=input("Enter City Name: ")
        district=input("Enter District Name: ")
        state=input("Enter State Name: ")
        country=input("Enter country Name: ")
        obj2=Address(city,district,state,country)
        self.AddressObject=obj2

    def Trainer_details(self):
        print(f'Name of the Trainer is {self.Tname}')
        print(f'Age of the Trainer is {self.Tage}')
        print(f'Subject Of the Trainer is {self.Tsubject}')
        self.AddressObject.display_address()

print()
print()
pawan=Student("Pawan",18,"Python")
pawan.Student_details()
print()
print()
tushar=Student("Tushar",25,"Java")
tushar.Student_details()
print()
print()
harshad=Trainer("Harshad",28,"Python")
harshad.Trainer_details()





#$------------------------------------------------------------------------------------------------------





## Example-2---->>>  Car/Driver Program



class Car:
    def __init__(self,Cname,Cnumber,Ccolor,Cbrand):
        self.car_name=Cname
        self.car_number=Cnumber
        self.car_color=Ccolor
        self.car_brand=Cbrand

    def car_detsils(self):
        print(f'Name of the car is {self.car_name}')
        print(f'Number of the car is {self.car_number}')
        print(f'Color of the car is {self.car_color}')
        print(f'Brand of the car is {self.car_brand}')

    def start(self):
        print(f'{self.car_name} is Start')

    def acclerate(self):
        print(f'{self.car_name} is Accelerate')

    def stop(self):
        print(f'{self.car_name} is Stop')

class Driver:
    def __init__(self,dname,dage,dexperience):
        self.driver_name=dname
        self.driver_age=dage
        self.driver_experience=dexperience
        ## Taking input to create car object
        Cname=input("Enter Your Car Name: ")
        Cnumber=input("Enter Your Car Number:")
        Ccolor=input("Your Car Color Is: ")
        Cbrand=input("Enter Your Car Brand: ")
        carObj=Car(Cname,Cnumber,Ccolor,Cbrand)
        self.dcar=carObj

    def driving(self):
        print(f'{self.driver_name} has entered into the car')
        self.dcar.start()
        self.dcar.acclerate()
        self.dcar.stop()
        print(f'{self.driver_name} has come out of car')
        ## self.dcar.car_detsils()

    def driver_details(self):
        print(f'Name of the driver is {self.driver_name}')
        print(f'Age of the driver is {self.driver_age}')
        print(f'Experience of the driver is {self.driver_experience} years')
        self.addressObj.car_detsils()

tushar=Driver("Tushar",25,5)
tushar.driving()






#$-----------------------------------------------------------------------------------------------------------





## Example-3--->>> Player/Team class program



class Player:
    def __init__(self,Pname,Page,Pcountry,P_no_of_match,P_no_of_run,P_no_of_wicket):
        self.Pname=Pname
        self.Page=Page
        self.Pcountry=Pcountry
        self.P_no_of_match=P_no_of_match
        self.P_no_of_run=P_no_of_run
        self.P_no_of_wicket=P_no_of_wicket

class Team:
    def __init__(self,no_of_player):
        self.no_of_player=no_of_player
        self.LOPO=[]
        for i in range(self.no_of_player):
            name=input("Enter Player Name: ")
            age=int(input("Enter Player age: "))
            country=input("Enter Player country: ")
            match=int(input("Enter Player matches: "))
            run=int(input("Enter Player runs: "))
            wicket=int(input("Enter Player wickets: "))
            PlayerObject=Player(name,age,country,match,run,wicket)
            self.LOPO.append(PlayerObject)

    def max_run(self):
        mxo=self.LOPO[0]
        for i in self.LOPO:
            if i.P_no_of_run > mxo.P_no_of_run:
                mxo=i
        return f"Maximum Run Scored By {mxo.Pname}"

    def min_run(self):
        mxo=self.LOPO[0]
        for i in self.LOPO:
            if i.P_no_of_run < mxo.P_no_of_run:
                mxo=i
        return f"Minimum Run Scored By {mxo.Pname}"

    def max_wicket(self):
        mxo=self.LOPO[0]
        for i in self.LOPO:
            if i.P_no_of_wicket > mxo.P_no_of_wicket:
                mxo=i
        return f"Maximum Wicket Taken By {mxo.Pname}"

    def min_wicket(self):
        mxo=self.LOPO[0]
        for i in self.LOPO:
            if i.P_no_of_wicket < mxo.P_no_of_wicket:
                mxo=i
        return f"Minimum Wicket Taken By {mxo.Pname}"


india=Team(3)
print(india.max_run())
print(india.min_run())
print(india.max_wicket())
print(india.min_wicket())

