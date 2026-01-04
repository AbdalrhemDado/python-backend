class Task :
    def __init__(self,id,name,description):
        self.id=id
        self.name=name
        self.description=description

    def __str__(self):
        return f"{self.id:<20}{self.name:<40} {self.description}"
