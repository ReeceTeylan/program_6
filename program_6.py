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

# Add instance method On or Off
    def turnOn(self):
        self.on = True
        print(f"{self.tvName} is turned on")

    def turnOff(self):
        self.on = False
        print(f"{self.tvName} is turned off")
# Add instance method for getchannel
# Add instance method for getvolume
# Add instance method for setvolume
# Add instance method for setchannel
# Add instance method for channelup
# Add instance method for channeldown
# Add instance method for volumeup
# Add instance method for volumedown
