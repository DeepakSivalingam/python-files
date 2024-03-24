'''
class--it is a blue print or a templated for crating a individual objects 
object-- instances of class..consist of methods and property 

'''

# class atributes 

class user_details:
    name="deepak"       # here we creted the class ...these are the class attributes 
    password="deepak2332"

# two ways to accesing the class attributes 

# one way-- getattr() method 

print(getattr(user_details,'name')) 
print(getattr(user_details,'password')) 
print(getattr(user_details,'gender','this attribute not found')) # the third parameter that specifies the exception that we given 

# dot notation 

print(user_details.name)
print(user_details.password)


# setattr -- for creating and changing the attibute 

setattr(user_details,'name','ram')
setattr(user_details,'gender','male')

user_details.city="villupuram"     # another way to create the attribute 
print(user_details.city)

print(getattr(user_details,'name'))
print(getattr(user_details,'gender'))


#delattr--- for deleting the attribute 

delattr(user_details,'gender')
print(user_details.__dict__)



# instance  atributes 

class student:
    department="IT"

object=student()    # here we created object for the above class

print(object.__dict__)

print(object.department)
object.department="CSE"
print(object.department)

# when we change or update the attributes by using the instance attribute it can't reflect in the class attributes .



#class methods

#example

class user_details:
    name="deepak"       
    password="deepak2332"
    
    def call():
        print("name :" ,user_details.name)
        print("password :" ,user_details.password)
        
user_details.call()


#instance methods 

