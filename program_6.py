# Create a class
class TV:
# Add constructor and instance variable
    def __init__(self, tv_name, channel, volume_level, on):
        self.tvName = tv_name
        self.channel = channel
        self.volumeLevel = volume_level
        self.on = on

        # Add conditions
        if self.channel < 1:
            self.channel = 1
            print(f"{self.tvName}: There are no channels lower than 1")

        if self.channel > 120:
            self.channel = 120
            print(f"{self.tvName}: There are no channels higher than 120")

        if self.volumeLevel > 7:
            self.volumeLevel = 7
            print(f"{self.tvName}: 7 is the highest volume")

        if self.volumeLevel < 1:
            self.volumeLevel = 1
            print(f"{self.tvName}: 1 is the lowest volume")

# Add instance methods