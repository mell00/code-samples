#OBJECT-ORIENTED PYTHON PROGRAMMING

#Creating a class:

class Classname:
    attribute_name = attribute_value

    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def regular_method_name(self, param):
        #Code that does something to self.param
        return self.param

    @classmethod
    def classmethod_name(cls, param3):
        #Code that does something to cls.param3
        return cls.param3

    @classmethod
    def altconstructor_cls_name(cls, object_creation_procedure):
        object_creation_procedure = #Code for object_creation_procedure
        param1,param2 = object_creation_procedure
        return cls(param1,param2)


    @staticmethod
    def staticmethod_name(param6):
        #Code that does something to param6
        return param6

#Special (Magic/Dunder) Method Emulation:

    def __builtin_operator_method_name__(self,other)
        return #Modified operation(s) that builtin_operator_method_name() should now perform

#-------------------------------------------------------------------------------------------------------------

#Calling a class attribute using class name:

Classname.attribute_name
##returns attribute_value##

#Calling a class attribute using instance variable:

instance_var = Classname(attribute_name = attribute_value)
instance_var.attribute_name = new_attribute_value
instance_var.attribute_name
##returns new_attribute_value##

#Storing the value returned by calling a regular method using instance variable:

instance_var = Classname(arg)

#Calling a class method using class name:

Classname.classmethod_name(arg3)
##returns cls.arg3##

#Calling a class method using instance variable:

cls_instance_var = Classname(arg3)
cls_instance_var.classmethod_name
##returns cls.arg3##

#Calling a static method (using class name):

Classname.staticmethod_name(arg6)
##returns staticmethod_name(arg6)##

#Calling a special (magic/dunder) method:

builtin_operator_method_name(arg)

#OR

arg.__builtin_operator_method_name__()

##both return value of arg operated on with builtin_operator_method_name##
##special method##


#Checking if object is an instance of a class using isinstance() function

isinstance(object_name,Classname)
##returns boolean value##


#Checking if object is a class/subclass of another class using issubclass() function

issubclass(object_name,Classname)
##returns boolean value##


#Setting value for new or existing attribute within an object using setattr() function

setattr(object_name,attribute_name,attribute_value)
##creates attibute_name within object_name and sets value to attribute_value##
##alternatively, sets existing attribute_name of object_name to attribute_value##


#Return dictionary representation of object's (writable) attributes using __dict__ attribute

object_name.__dict__['attribute_name_or_value']
##if __dict__ lacks arguments, prints map of entire dictionary consisting of all (writable) attributes within object_name##
##if argument is entered, locates associated attribute_value_or_name within dictionary##




#-------------------------------------------------------------------------------------------------------------

#Creating a subclass of a class:

class Subclassname(Classname):
    attribute_2_name = attribute_2_value

#Initializing/constructing an attribute exclusive to subclass:

    def __init__(self,var1):
        self.var1 = var1

#Creating a classmethod exclusive to subclass:

    @classmethod
    def subclass_classmethod_name(cls, param):
        #Code that does something to cls.param7
        return cls.param

#Change functionality of inherited regular method exclusively within subclass:

    def __init___of_Subclassname(self, param, added_param):
        super().__init__(param) #Imports value of param from Classname (the parent class)
        self.added_param = added_param_value #Assigns value to new parameter added_param

    def modified_inherited_reg_method(self):
        #Code that does something with self.param and self.added_param
        return #Statement using self.param and self.added_param

    #NOTE: ^ ALWAYS CALL ORIGINAL DEF OF METHOD FROM PARENT CLASS ^

#Creating a property object:

    @property
    def attribute_like_method_name(self)
        return #Value that accepts + includes/uses some pre-defined attribute (such as self.var1, for example)
#-------------------------------------------------------------------------------------------------------------
#GETTER/SETTER/DELETER METHODS contained within body of a specific property;
#two methods to define these methods: invoking with property decorators, or defining
#getter/setter/deleter methods + calling property() function

#Method 1: Invoking with property decorators:
class Getsetdelete_1(Classname):
    attribute_3_name = attribute_3_value

    def __init__(self,var):
        self.var = var

    @property
    def var(self): #Turns var() method into "getter" for read-only attribute of the same name
        """#docstring for var""" #Sets docstring for var property
        return self.var #Invokes getter attribute of var property


    @var.setter
    def var(self,value):
        self.var = value #Invokes setter attribute of var property

    @var.deleter
    def var(self):
        del self.var #Invokes deleter attribute of var property

#-------------------------------------------------------------------------------------------------------------

#Method 2: Defining getter/setter/deleter methods + property() function:
class Getsetdelete_2(Classname):

    def __init__(self): #Initializes/constructs managed attribute var
        self.var = None

    def getvar(self): #Defines getter method
        return self.var

    def setvar(self,value): #Defines setter method
        self.var = value

    def delvar(self): #Defines deleter method
        del self.var

var = property(getvar,setvar,delvar,"var property docstring")

#-------------------------------------------------------------------------------------------------------------
