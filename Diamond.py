__author__ = "jigar n harsh"

"""
This code is written to complete assignment.
This code will create following pattern.
            *             
           * *            
          * * *           
         * * * *          
        * * * * *         
       * * * * * *        
      * * * * * * *       
     * * * * * * * *      
    * * * * * * * * *     
   * * * * * * * * * *    
  * * * * *   * * * * *   
 * * * * *     * * * * *  
  * * * * *   * * * * *   
   * * * * * * * * * *    
    * * * * * * * * *     
     * * * * * * * *      
      * * * * * * *       
       * * * * * *        
        * * * * *         
         * * * *          
          * * *           
           * *            
            *             

"""

row=1
upper=1
star="* "
space=" "
diamond=input("Enter No. of Diamonds:")
side_length=input("Enter Side Length of Diamond:")
counter=0
daimond_par_row = 1
total_length=2*side_length - 1

#Logic Starts

if side_length < ((diamond*2)+1) : # Min Condition to be matched
        print "Wrong Input"
else:
        while row < side_length : #For Upper Portion
                if row <= (diamond*2):
                        print ( space*((side_length - row)+1) + star*row + space*((side_length - row)+1))* daimond_par_row
                else :
                        print ( space*((side_length - row)+1) + star*diamond + space*(upper +1) +\
                                star*diamond + space*((side_length - row)+1)) * daimond_par_row
                        upper +=2
                        counter+=1
                row+=1
        if row == side_length : #For Center Portion
                print ( space*((side_length - row)+1) + star*diamond + space*(upper +1) +\
                        star*diamond + space*((side_length - row)+1) ) * daimond_par_row
        row+=1
        while row > side_length : #For Lower Portion
                while counter >= 1 :
                        print ( space*(row - side_length + 1) + star*(diamond) + space *(upper-1) +\
                                star*(diamond) + space*(row - side_length + 1)) * daimond_par_row
                        counter-=1
                        row+=1
                        upper-=2
                while row<=total_length :
                        
                        print ( space*((row - side_length)+1) + star*((total_length - row) + 1) +\
                                space*((row - side_length)+1)) * daimond_par_row
                        row+=1
#Logic Ends
