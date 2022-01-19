class Driver:
    def __init__(self) -> None:
        self.dict_of_drivers = {
                            "Ali":{"model":"Swift","location":[0,0],"avail":True},
                            "Jazib":{"model":"Swift","location":[0,0],"avail":True},
                            "Sourav":{"model":"Swift","location":[0,0],"avail":True},
                              }
    def register(self):
        
        
        wish = True
        
        while True:
            if wish==False:
                break
            name = input("Enter Driver name")
            self.dict_of_drivers[name] = dict()
            model = input("Enter model name")
            location = list(map(int,input("Enter location by 2 coordinates").split()))
            avail = input("Enter availability(Y/N)?")
            self.dict_of_drivers[name]["model"] = model
            self.dict_of_drivers[name]["location"] = location
            if avail == "Y":
                self.dict_of_drivers[name]["avail"] = True
            elif avail == "N":
                self.dict_of_drivers[name]["avail"] = True
            else:
                print("give Y or N")

            
            
            choice = input("Do you want to register another Driver?(T/F)")
            
            if choice == "T":
                continue
            else:
                wish=False

        print(self.dict_of_drivers)

    

    
