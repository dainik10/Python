# wap to develop student class with static, non static and local variables, constructor and non static methods. name of student, rollno, address, and 3 subject marks. if marks greater than 35 then print pass, if any of less than 35 print fail and if pass calculate the grade.

name=input("Enter the name of a student: ")
rollno=int(input("Enter the rollno of a student: "))
address=input("Enter the address of a student: ")
sub1=int(input("Enter the marks of subject1: "))
sub2=int(input("Enter the marks of subject2: "))
sub3=int(input("Enter the marks of subject3: "))
class student:
    def __init__(self):
        self.name=name
        self.rollno=rollno
        self.address=address
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        
    def display(self):
        print("Name of a student is: ",self.name)
        print("Rollno of a student is: ",self.rollno)
        print("Address of a student is: ",self.address)
        print("Marks of subject1 is: ",self.sub1)
        print("Marks of subject2 is: ",self.sub2)
        print("Marks of subject3 is: ",self.sub3)
        
    def find_result(self):
        self.total=self.sub1+self.sub2+self.sub3
        self.avg=self.total/3
        if(self.sub1>=35 and self.sub2>=35 and self.sub3>=35):
            print("Pass")
            if(self.avg>=75):
                print("Grade A")
            elif(self.avg>=60 and self.avg<75):
                print("Grade B")
            elif(self.avg>=50 and self.avg<60):
                print("Grade C")
            elif(self.avg>=35 and self.avg<50):
                print("Grade D")
        else:
            print("Fail")
s1=student()
s1.display()
s1.find_result()
