class Journey:
    """
    Description:
    Class for calculating whether you have enough fuel for the journey.
    ---
    Parameters:
        distance (int): The distance in required for your journey.
        fuel_left (int): How many gallons are in the tank for making your journey.
    """
    outcome: bool = None
    fuel_consumption: int = 25
    def __init__(self, distance, fuel_left):
        self.distance = distance
        self.fuel_left = fuel_left

    def willyoumakeit(self) -> None:
        if self.fuel_left * self.fuel_consumption < self.distance:
            self.outcome = False
        else:
            self.outcome = True

    def __str__(self):
        return self.willyoumakeit()

if __name__ == "__main__":
    journey = Journey(50, 2)
    journey.willyoumakeit()
    print(journey.outcome)