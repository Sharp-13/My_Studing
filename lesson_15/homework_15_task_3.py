# Task 3
#
# TV controller
#
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
#
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
# exists in the list, or "No" - in the other case.
#
# The default channel turned on before all commands is №1.
#
# Your task is to create the TVController class and methods described above.

# from types import List

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    current_chan = 1
    def __init__(self, chan):
        self.chan = chan

    def first_channel(self):
        global current_chan
        current_chan = 1
        return self.chan[0]

    def last_channel(self):
        global current_chan
        current_chan = len(self.chan)
        return self.chan[current_chan-1]

    def turn_channel(self, chan_num):
        global current_chan
        current_chan = chan_num
        return self.chan[chan_num-1]

    def next_channel(self):
        global current_chan
        if current_chan < len(self.chan)-1:
            current_chan = current_chan + 1
        else:
            current_chan = 1
        return self.chan[current_chan-1]

    def previous_channel(self):
        global current_chan
        if current_chan == 1:
            current_chan = len(self.chan)
        else:
            current_chan = current_chan - 1
        return self.chan[current_chan - 1]

    def current_channel(self):
        global current_chan
        return self.chan[current_chan - 1]

    # def is_exist(self, chan_name = None, chan_num = None):
    #     if (chan_name in self.chan) or (chan_num > 0 and chan_num <= len(self.chan)):
    #         return 'Yes'
    #     else:
    #         return "No"




controller = TVController(CHANNELS)

if controller.first_channel() == "BBC":
    print('Ok')

if controller.last_channel() == "TV1000":
    print('Ok')

if controller.turn_channel(1) == "BBC":
    print('Ok')

if controller.next_channel() == "Discovery":
    print('Ok')

if controller.previous_channel() == "BBC":
    print('Ok')

if controller.current_channel() == "BBC":
    print('Ok')

# if controller.is_exist(4) == "No":
#     print('Ok')
#
# if controller.is_exist("BBC") == "Yes":
#     print('Ok')
