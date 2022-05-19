#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 60
        self.RIGHT_DEFAULT = 60
        self.MIDPOINT = 1300  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit),
                "sq": ("Square", self.square),
                "std":("safe_to_dance", self.safe_to_dance),
                "cw": ("Check_wall", self.check_wall),
                "rt": ("roof_turn", self.roof_turn),
                "bt": ("box_turn", self.box_turn),
                "cbt": ("complicated_box_turn", self.complicated_box_turn),
                "ss": ("s_scam", self.s_scam),
                "ms": ("m_scam", self.m_scam)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''
    def check_wall(self):
      while self.read_distance() >= 600:
        self.read_distance()
        self.fwd()
        time.sleep(0.5)
      else:  
        self.stop()

    
    def roof_turn(self):
      i = 1
      while i < 10:
        while self.read_distance() >= 600:
          self.read_distance()
          self.fwd()
          time.sleep(0.5)
        else:  
          self.right(primary=90, counter=-90)
          time.sleep(1.1)
          for butty2 in range(4):
            self.right()
            time.sleep(0.2)
            self.left()
            time.sleep(0.2)
      else:
        self.stop()



    
    def box_turn(self): 
        # infinite loop... never stop navigating
        while True:
            # look straight ahead
            self.servo(1300)
            while self.read_distance() >= 201:
                self.fwd()
                time.sleep(0.2)
            self.right()
            time.sleep(0.4)      
            #moves to the right while it does not see the hope
            while self.read_distance() <=450:
                self.turn_by_deg(20)
            #moves its head so it will see only the box
            while True:
                self.servo(2100)  
                #goes straith untill it will se the hope again
                while self.read_distance() <=300:
                    self.fwd()
                    time.sleep(0.1)
                self.servo(1300)  
                self.fwd()
                time.sleep(1)
                self.left()   
                time.sleep(0.9)

        self.stop()



    def complicated_box_turn(self): 
        while True:
            # look straight ahead
            self.servo(1300)
            while self.read_distance() >= 201:
                self.fwd()
                time.sleep(0.1)
            self.stop
            self.servo(2000)
            self.read_distance()
            left_distance = self.read_distance()
            self.read_distance()
            self.servo(800)
            self.read_distance()
            right_distance = self.read_distance()
            self.read_distance()
            
            if left_distance < right_distance:
                self.right()
                time.sleep(0.4)      
                #moves to the right while it does not see the hope
                while self.read_distance() <=450:
                    self.turn_by_deg(20)
                #moves its head so it will see only the box
                while True:
                    self.servo(2100)  
                    #goes straith untill it will se the hope again
                    while self.read_distance() <=300:
                        self.fwd()
                        time.sleep(0.1)
                    self.servo(1300)  
                    self.fwd()
                    time.sleep(1)
                    self.left()   
                    time.sleep(0.7)
            else:
                self.left()
                time.sleep(0.4)      
                #moves to the right while it does not see the hope
                while self.read_distance() <=450:
                    self.turn_by_deg(350)
                #moves its head so it will see only the box
                while True:
                    self.servo(800)  
                    #goes straith untill it will se the hope again
                    while self.read_distance() <=300:
                        self.fwd()
                        time.sleep(0.1)
                    self.servo(1300)  
                    self.fwd()
                    time.sleep(1)
                    self.right()   
                    time.sleep(0.7)
                    
    def s_scam(self): 
        self.servo(1300)
        while True:
            self.fwd()
            time.sleep(0.1)
            self.servo(800)
            self.read_distance()
            self.servo(2000)
            self.read_distance()


    def m_scam(self): 
        self.servo(1300)
        while True:
            while self.read_distance() >= 300:
                self.fwd()
                time.sleep(0.2)
                self.servo(800)
                time.sleep(0.2)
                self.read_distance()
                self.servo(1300)
                time.sleep(0.2)
                self.read_distance()
                self.servo(2000)
                time.sleep(0.2)
                self.read_distance()
                self.servo(1300)
                time.sleep(0.2)
                self.read_distance()
            self.stop  
            self.servo(1300)
            self.servo(800)
            self.read_distance()
            right_distance = self.read_distance()
            self.servo(2000)
            self.read_distance()
            left_distance = self.read_distance()
            if left_distance < right_distance:
                self.right()
                time.sleep(1)
                self.fwd()
                time.sleep(2)
                self.left()
                time.sleep(1)
            else:
                self.left()
                time.sleep(1)
                self.fwd()
                time.sleep(2)
                self.right()
                time.sleep(1)




            
    def dance(self):
        self.servo(1000)
        self.read_distance()
        if self.read_distance() <= 500:
            self.stop()
        else:
            self.servo(2000)
            self.read_distance()
        if self.read_distance() <= 500:
            self.stop()
        else:
            self.servo(1300)
            response = str.lower(input("Move left or move right(l/r): "))
        if response == 'l':
            self.left(primary=90, counter=-90)
        elif response == 'r':
            self.right(primary=90, counter=-90)
            time.sleep(5)
            self.fwd()
            time.sleep(2) 
        for butty in range(4):
            self.right()
            time.sleep(0.4)
            self.left()
            time.sleep(0.4)
        for butty2 in range(4):
            self.right(primary=90, counter=-90)
            time.sleep(0.2)
            self.left(primary=90, counter=-90)
            time.sleep(0.2)
            self.stop()
        


    def safe_to_dance(self):
        pass


    
    def square(self):
        for edge in range(4):
          self.fwd()
          time.sleep(2)
          self.right()
          time.sleep(1)
        self.stop
      
    
    def shake(self):
        """ Another example move """
        self.deg_fwd(720)
        self.stop()

    
    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    
    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    
    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass


    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP

if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
