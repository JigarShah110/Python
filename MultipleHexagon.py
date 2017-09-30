__author__ = "Jigar Shah"

"""
This code is written to complete assignment.
This code will create following pattern.

Enter Side Length: 10
Enter No. of Hexagons: 5
         * * * * * * * * * * 
        * * * * * * * * * * * 
       * * * * * * * * * * * * 
      * * * * * * * * * * * * * 
     * * * * * * * * * * * * * * 
    * * * * *           * * * * * 
   * * * * *             * * * * * 
  * * * * *               * * * * * 
 * * * * *                 * * * * * 
* * * * *                   * * * * * 
 * * * * *                 * * * * * 
  * * * * *               * * * * * 
   * * * * *             * * * * * 
    * * * * *           * * * * * 
     * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * 
       * * * * * * * * * * * * 
        * * * * * * * * * * * 
         * * * * * * * * * * 
Press Enter to close it

"""
class pattern :

        """This class is for pattern that we made in last section without class"""

        row = 1
        space = " "
        star = "* "
        
        def __init__(self):

                self.side_length = input("Enter Side Length: ")
                self.hexagons = input("Enter No. of Hexagons: ")
        def initia(self):
                
                self.line_diamond = self.side_length
                self.counter = 0
                self.space_counter = (2*(self.side_length - self.hexagons))
                self.total_length = (2* self.side_length - 1)

        def draw(self):

                if self.hexagons >= self.side_length : #Condition for size of Hexagon
                        print "Wrong Choice"

                #Logic Start
                else:
        
                        while pattern.row <= self.side_length : #For Upper Part of Hexagon
                                if pattern.row <= self.hexagons : #For Continuous Execution
                                        print pattern.space*(self.side_length - pattern.row) +\
                                          pattern.star*(self.line_diamond)
        
                                        self.line_diamond +=  1
                
                                else : #For Spaces Between Left and Right Portion(UPPER PART)
                                         print pattern.space * (self.side_length-pattern.row) +\
                                         pattern.star*self.hexagons + pattern.space*(self.space_counter) +\
                                         pattern.star*self.hexagons
                                         self.space_counter += 2
                                         self.counter += 1
                                pattern.row += 1
                
                        while pattern.row <=self.total_length : #For Lower Part of Hexagons
                                if self.counter > 1 : #FOR Spaces Between Left and Right Portion(LOWER PART)
                                        print pattern.space*(pattern.row - self.side_length) + pattern.star * self.hexagons + pattern.space *(self.space_counter - 4) + pattern.star*self.hexagons
                                        self.space_counter -= 2
                                        self.counter -= 1
                                
                                
                                else : #For Continuous Execution
                                        print pattern.space * (pattern.row - self.side_length) + pattern.star*(self.line_diamond - 1)
                                        self.line_diamond  -= 1

                                pattern.row += 1
                
                #Logic Ends


patobj = pattern()
patobj.initia()
patobj.draw()


        
