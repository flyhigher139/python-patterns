#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


# class MoveFileCommand(object):
#     def __init__(self, src, dest):
#         self.src = src
#         self.dest = dest

#     def execute(self):
#         self()

#     def __call__(self):
#         print('renaming {} to {}'.format(self.src, self.dest))
#         os.rename(self.src, self.dest)

#     def undo(self):
#         print('renaming {} to {}'.format(self.dest, self.src))
#         os.rename(self.dest, self.src)


# def main():
#     command_stack = []

#     # commands are just pushed into the command stack
#     command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
#     command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))

#     # they can be executed later on
#     for cmd in command_stack:
#         cmd.execute()

#     # and can also be undone at will
#     for cmd in reversed(command_stack):
#         cmd.undo()

# if __name__ == "__main__":
#     main()

### OUTPUT ###
# renaming foo.txt to bar.txt
# renaming bar.txt to baz.txt
# renaming baz.txt to bar.txt
# renaming bar.txt to foo.txt

#---------------------------------------------#

#---------------------------------------#
# my command pattern
#---------------------------------------#

class Vehicle(object):
    """docstring for ClassName"""
    def __init__(self):
        self.name = 'vehicle'
        
    def __call__(self):
        print "travelling by a Vehicle"

    def execute(self):
        self()


class Bus(Vehicle):
    """docstring for Bus"""
    def __init__(self):
        super(Vehicle, self).__init__()
        self.name = 'bus'

    def __call__(self):
        print 'travelling by bus'

    def execute(self):
        self()
        
class Bike(Vehicle):
    """docstring for Bike"""
    def __init__(self):
        super(Vehicle, self).__init__()
        self.name = 'bike'

    def __call__(self):
        print 'travelling by bike'

    def execute(self):
        self()

class Car(Vehicle):
    """docstring for Car"""
    def __init__(self):
        super(Vehicle, self).__init__()
        self.name = 'car'

    def __call__(self):
        print 'travelling by car'

    def execute(self):
        self()

class Rocket(Vehicle):
    """docstring for Rocket"""
    def __init__(self):
        super(Vehicle, self).__init__()
        self.name = 'rocket'

    def __call__(self):
        print 'travelling by rocket'

    def execute(self):
        self()


class Traveller(object):
    """docstring for Traveller"""
    def __init__(self, name):
        self.name = name

    def set_vehicle(self, vehicle):
        self.vehicle = vehicle
        
    def travel(self):
        self.vehicle.execute()


def main():
    # create a traveller
    tom = Traveller('tom')

    print 'stop 1:'
    # traveller's first vehicle
    vehicle = Bus()
    tom.set_vehicle(vehicle)
    tom.travel()

    print 'stop 2:'
    # traveller's second vehicle
    vehicle = Bike()
    tom.set_vehicle(vehicle)
    tom.travel()

    print 'stop 3:'
    # traveller's third vehicle
    vehicle = Car()
    tom.set_vehicle(vehicle)
    tom.travel()

    print 'stop 4:'
    # traveller's fourth vehicle
    vehicle = Rocket()
    tom.set_vehicle(vehicle)
    tom.travel()

if __name__ == '__main__':
    main()


### OUTPUT ###
# stop 1:
# travelling by bus
# stop 2:
# travelling by bike
# stop 3:
# travelling by car
# stop 4:
# travelling by rocket