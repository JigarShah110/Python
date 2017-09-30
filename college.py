
__author__ = "Jigar N. Shah"


"""This Progam is an example of Class and inheritance for college
It will print as following for three modules:

1.Student
2.Professor
3.Head of Department


Name: Jigar Shah
Age: 20
Mobile No: 9714589930
Enrolment No: 098
Department: Computer
Post: Student

Welcome  Jigar Shah
You have two lectures of S.P.Patel



Name: S.P.Patel
Age: 40
Mobile No: 9823651478
Department: Computer
Qualification: M.E.
Post: Professor


Welcome Professor S.P.Patel
You Have meeting with H.O.D. at 2:00 p.m.



Name: T.J.Raval
Age: 45
Mobile No. 9854632710
Department Computer
Qualification: Ph.d.
Post: H.O.D.


Welcome H.O.D.  T.J.Raval
Meeting With Professors At 2:00 p.m.




"""
class college: #PARENT CLASS
    """"This Class is for Whole College and it is parent class of all"""

    def __init__(self,name,age,res_city,mobile_no,department,post):

        self.name = name
        self.age = age
        self.res_city = res_city
        self.mobile_no = mobile_no
       
        self.department = department
        self.post = post

    def about_today(self): #METHOD WHICH IS USED BY EVERY CHILD CLASS
        if self.post == "Student":
            if self.department == "Computer" :
                print "Welcome ",self.name
                print "You have two lectures of S.P.Patel"

            elif self.department == "Mechanical" :
                print "Welcome ",self.name
                print "You have first lecture of S.S.Patel"

            elif self.department == "Electrical" :
                print "Welcome ",self.name
                print "You have no lectures today only two labs"
        
        elif self.post =="Professor" :

            if self.department == "Computer" :
                print "Welcome Professor" ,self.name
                print "You Have meeting with H.O.D. at 2:00 p.m."

            elif self.department == "Mechanical" :
                print "Welcome Professor" ,self.name
                print "You have to go Ahmedabad with Principal"

            elif self.department == "Electrical" :
                print "Welcome Professor" ,self.name
                print "You have two lectures in class D"

        elif self.post == "H.O.D." :

            if self.department == "Computer" :
                print "Welcome H.O.D. ",self.name
                print "Meeting With Professors At 2:00 p.m."

            elif self.department == "Mechanical" :
                print "Welcome H.O.D. ",self.name
                print "You have to manage Seminars"

            elif self.department == "Electrical":
                print "Welcome H.O.D. ",self.name
                print "You have to make new time table of next week"
        print

class admin:
    """This is an admin class which can be used by both studentes and professors"""

    def __init__(self , post):

        self.post = post

    def activity(self):

        if self.post == "Student":
            print "Welcome in Administration"
            print "You have Multiple Choices:"
            print "1. Bus Pass Form"
            print "2. Collection of Marksheet"
            print "3. Any Other Issues"

        elif self.post == "Professor":

            print "Welcome Professor in Administration"
            print "Your Choices:"
            print "1. "

        else:
            print "Welcome H.O.D"
            print "Do You Have meeting with Principal??"


class student(college,admin): #CHILD CLASS OF college ONLY FOR STUDENTS
        """This Class is For Students so it will take post as student"""

        post = "Student"
        
        def __init__(self,name,age,res_city,mobile_no,enrolment_no,department,post):

            self.name = name
            self.age = age
            self.res_city = res_city
            self.mobile_no = mobile_no
            self.enrolment_no = enrolment_no
            self.department = department
            self.post = post

        
        def display(self):
            print "Name:" , self.name
            print "Age:" , self.age
            print "Mobile No:" , self.mobile_no
            print "Enrolment No:" , self.enrolment_no
            print "Department:" , self.department
            print "Post:" , student.post
            print

class professor(college,admin): #CHILD CLASS OF college ONLY FOR PROFESSORS
        """"This Class is for Professors"""

        post = "Professor"

        def __init__(self ,name,age, res_city , mobile_no , department , qualification):
            self.name = name
            self.age = age
            self.res_city = res_city
            self.mobile_no = mobile_no
            self.department = department
            self.qualification = qualification
            

        def display(self):
            print "Name:" , self.name
            print "Age:" , self.age
            print "Mobile No:" , self.mobile_no
            print "Department:" , self.department
            print "Qualification:" , self.qualification
            print "Post:" , professor.post
            print


class departmenthead(professor,admin): #AS PER A H.O.D. IS ALSO AN PROFESSOR SO IT IS CHILD CLASS OF BOTH college AND professor

        """"This Class is for All H.O.D 's"""

        qualification = "Ph.d."

        post = "H.O.D."

        def __init__(self, name, age , mobile_no , res_city , department):
            self.name = name
            self.age = age
            self.mobile_no = mobile_no
            self.res_city = res_city
            self.department = department

        def display(self):
            print "Name:" , self.name
            print "Age:" , self.age
            print "Mobile No." , self.mobile_no
            print "Department" , self.department
            print "Qualification:" , departmenthead.qualification
            print "Post:" ,departmenthead.post
            print


stud1 = student("Jigar Shah","20" , "Mehsana" , 9714589930 , "098" , "Computer" , "Student") #OBJECT OF STUDENT
stud1.display()           #CALLING OF BOTH METHODS WHICH ARE RESIDES INSIDE student CLASS
stud1.about_today()       #THIS METHOD RESIDES IN PARENT(college) CLASS
stud1.activity()          #THIS METHOD ONLY ACCESSIBLE BY ADMIN CLASS's OBJECT or ITS CHILD CLASS

stud2 = student("Parimal","20" , "Mehsana" , 9542967300 , "125" , "Electrical" , "Student")
stud2.display()
stud2.about_today()
stud2.activity()

prof1 = professor("S.P.Patel" , "40" , "Visnagar" , 9823651478 , "Computer" , "M.E.")
prof1.display()         #CALLING OF BOTH METHODS WHICH ARE RESIDES INSIDE professor CLASS
prof1.about_today()     #THIS METHOD RESIDES IN PARENT(college) CLASS
prof1.activity()        #THIS METHOD ONLY ACCESSIBLE BY ADMIN CLASS's OBJECT or ITS CHILD CLASS

prof2 = professor("S.S.Patel" , "30" , "Mehsana" , 9712645079 , "Mechanical" , "B.E.")
prof2.display()
prof2.about_today()
prof2.activity()

hod1 = departmenthead("T.J.Raval" , "45" , "9854632710" , "Ahmedabad" , "Computer")
hod1.display()          #CALLING OF BOTH METHODS WHICH ARE RESIDES INSIDE departmenthead CLASS
hod1.about_today()      #THIS METHOD RESIDES IN PARENT(college) CLASS
hod1.activity()         #THIS METHOD ONLY ACCESSIBLE BY ADMIN CLASS's OBJECT or ITS CHILD CLASS

hod2 = departmenthead("Dr. D.K.Patel" , "50" , "9572641380" , "Ahmedabad" , "Mechanical")
hod2.display()
hod2.about_today()
hod2.activity()

exit = raw_input("Press Enter To Close:")
