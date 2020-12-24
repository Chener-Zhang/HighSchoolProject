#
# hw10pr1.py
#
# name: chener 
#

class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """
    thirtyonedays = [1,5,7,10]
    thirtydays = [4,6,9,11]

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

        
    def __eq__(self, d2):
        """ Overrides the == operator so that it declares two of the same dates in history as ==
            This way , we don't need to use the awkward d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False
### my work
    def tomorrow(self):
        
        thirtyonedays = [1,3,5,7,10]###
        thirtydays = [4,6,9,11]

        """ this will change the self and shows the date of next day"""
        
        if self.isLeapYear() and self.month == 2 and self.day == 29:
            self.month = 3
            self.day = 1
        elif not self.isLeapYear()and self.month == 2 and self.day == 28:
            self.month = 3
            self.day = 1            
        elif self.month == 12 and self.day == 31:
            self.year = self.year + 1
            self.month = 1
            self.day = 1
        elif self.month in thirtyonedays and self.day == 31:
            self.month = self.month + 1
            self.day = 1
        elif self.month in thirtydays and self.day == 30:
            self.month = self.month + 1
            self.day = 1
        elif self.month == 8 and self.day == 31:
            self.month = 9
            self.day = 1
        
        else:
            self.day = self.day + 1

            
    def yesterday(self):
        """ this will change the self and shows the date of next day"""

        
        thirtyonedays = [1,5,7,10]
        thirtydays = [4,6,9,11]

        if self.isLeapYear() and self.month == 3 and self.day == 1:
            self.month = 2
            self.day = 29
        elif not self.isLeapYear() and self.month == 3 and self.day ==1:
            self.month = 2
            self.day = 28 
        elif self.month == 1 and self.day == 1:
            self.year = self.year - 1
            self.month = 12
            self.day = 31
        elif self.month in thirtyonedays and self.day == 1:
            self.month = self.month - 1
            self.day = 30
        elif self.month in thirtydays and self.day == 1:
            self.month = self.month - 1
            self.day = 31
        elif self.month == 12 and self.day == 1:
            self.month = 11
            self.day = 30
        elif self.month == 2 and self.day == 1:
            self.month = 1
            self.day = 31
        elif self.month == 8 and self. day == 1:
            self.month = 7
            self.day = 31
        else:
            self.day = self.day - 1

    def addNDays(self, N):
        " this function shows the day which add to the current day"
        for i in range(N):
            self.tomorrow()
            print self
        print 
        return  self 

    def subNDays(self, N):
        "  this funciton shows how many days before this day"
        for i in range(N):
            self.yesterday()
            print self
        print
        return self

    def isBefore(self, d2):
        " this function is to check self is before d2 or not "
        Lself = [self.year, self.month, self.day]
        L2 = [d2.year, d2.month, d2.day]
        if Lself[0] < L2[0] :
            return True
        elif Lself[0] == L2[0] and Lself[1] < L2[1]:
            return True
        elif Lself[0] == L2[0] and Lself[1] == L2[1] and Lself[2] < L2[2]:
            return True
        else:
            return False

    def isAfter(self, d2):
        " this function is to check self is after d2 or not "
        Lself = [self.year, self.month, self.day]
        L2 = [d2.year, d2.month, d2.day]
        if Lself[0] > L2[0]:
            return True
        elif Lself[0] == L2[0] and Lself[1] > L2[1]:
            return True
        elif Lself[0] == L2[0] and Lself[1] == L2[1] and Lself[2] > L2[2]:
            return True
        else:
            return False

    def diff(self, d2):
        "this function is to count how many days difference between self and d2"
        self_copy = self.copy()
        d2_copy = d2.copy()
        b = 0
        if self == d2 :
             return 0
        
        elif self.isAfter(d2):
            while self_copy.isAfter(d2_copy):
                self_copy.yesterday()
                b = b + 1
            return b
        
        elif self.isBefore(d2):
            while self_copy.isBefore(d2):
                self_copy.tomorrow()
                b = b - 1
            return b

        
    def dow(self):
        " this funcion shows which date is which day"
        L = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        d2 = Date(4,25,2016)
        DAY = L[0]
        b = self.diff(d2) % 7
        if self == Date(4,25,2016):
            return L[0] 
        elif self.diff(d2) > 0:
            c = L[0 + b]
            return c
        elif self.diff(d2) < 0:
            c = L[0 + b]
            return c
            
            

        

        

        
        
            
        
    
            
        
            

        
        
        
            
        
            
    

            
            
            

            

