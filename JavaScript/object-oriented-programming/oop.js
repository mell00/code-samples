//OBJECT-ORIENTED JAVASCRIPT PROGRAMMING//


//Define and assign value to a variable in one of three ways:
var variable_name1 = "variable_value1";
const variable_name2 = "variable_value2";
//NOTE: the value of a variable set with const cannot be altered
let variable_name3 = "variable_value3";

//Update value of a variable:
variable_name1 = "variable_value4";

//Define and assign value(s) to an array:
let array_name1 = ["array_value1","array_value2","array_value3"];
let array_name2 = [1, 2, 3];

//Access value within an array:
array_name1[0]
//"array_value1"

//Define a function:
function function_1 (param1,param2) {

}

//Define and assign key:value pairs to an object (thereby creating an object literal):
const object_name1 = {key_1:"value_1", key_2:[1,2], key_3:"value_3"};

//Call the property of an object:
object_name1.key_1
//"value_1"

//Access value of a (collection containing) property called on an object:
object_name1.key_2[0]
//1

//Access value of a property within a property of an object:
object_name1['property_1'][index_#]['property_2'][index_#]
OR
object_name1.property_1(index_#).property_2(index_#)

//Add new property to an object literal:
object_name.new_property = value
OR
object_name['new_property'] = value


//Constructors


//Create a new constructor function:
function Constructor_name(argument_1,argument_2,argument_3,...,argument_n) {
  this.argument_1 = argument_1;
  this.argument_2 = argument_2;
  this.argument_3 = argument_3;
  ...
  this.argument_n = argument_n;
}
OR
function Constructor_name(argument_1,argument_2,argument_3,...,argument_n) {
  this.argument_1 = argument_1;
  this.argument_2 = argument_2;
  this.argument_3 = argument_3;
  ...
  this.argument_n = argument_n;
  this.additional_argument = 'Banana';
}

//Create new instance object from a constructor function:
var instance_object_name = new Constructor_name(value_1,value_2,value_3,...,value_n);

//Add a new property to an existing object:
instance_object_name.argument_4 = 1;

//Add a method to an existing object:
instance_object_name.add_1_and_2 = function () {return this.argument_1 + this.argument_2;};


//Classes


//Create a new class:
class Class_name {Constructor(argument_1,argument_2,argument_3,...,argument_n){executed_code_within_class Class_name}};

//Initialize the values of properties within a class:
class Class_name {Constructor(argument_1,argument_2,argument_3,...,argument_n){
  this.add_1_and_2 = argument_1 + argument_2;
  this.argument_3 = argument_3;
  this.argument_n = argument_n;
  this.additional_argument = 'Banana';
}};

//Add a new property to a class:
Class_name.argument_4 = 1;

//Create an instance of a class:
const instance_object_name = new Class_name(value_of_argument_1,value_of_argument_2,value_of_argument_3,...,value_of_argument_n);

//Create a method within a class:
class Class_name {Constructor(argument_1,argument_2,argument_3,...,argument_n){
  method_name(params){executed_code_returning_a_value}
}};

//Add a method to a class:
Class_name.argument_n_plus_1 = function () {executed_code};

//Call a class method:
Class_name.method_name(args)


//Getters and Setters


//Define a getter method:
get getter_name(){executed_code_returning_a_value};

//Access value of a getter method:
object_name.getter_name
OR
object_name[getter_name]

//Define a setter method:
set setter_name(){executed_code_that_accepts_value};

//Access setter method:
console.log(setter_name);
