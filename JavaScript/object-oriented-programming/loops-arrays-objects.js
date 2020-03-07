//LOOPS, ARRAYS, AND OBJECTS IN JAVASCRIPT//

while (condition) {executed_code}

do {executed_code} while (condition)

for (var i=initial_#; i++ OR i--; i<final_#) {executed_code}

loop(){if(condition) {
  break;
}}



var array_name = [value_1];

array_name[index_#];


var numbers = [1, 2, 3, .., #];
var modified_array = numbers[numbers.length] = some_number;

var array_name = [];
var modified_array = array_name.push(one_or_more_new_values);

var array_name = [];
var modified_array = array_name.unshift(one_or_more_new_values);

var array_name = [];
var modified_array = array_name.shift();

var array_name = [];
var modified_array = array_name.pop();


var array_name = [1, 2, 3];
for (var i=0; i<array_name.length; i+=1) {
  object_name.method_name(array_name[i]);
}

var array_name = [1, 2, 3];
var joined_string = array_name.join(', ');

var array_name = [1, 2, 3];
var index_position = array_name.indexOf(value);

var two_dim_array = [row_one_values], [row_two_values], [row_three_values], .., [row_#_values];

two_dim_array[row_#_index_#][column_#_index_#]

var array_name = [];
var second_array_name = [];
var new_concat_array = array_name.concat(second_array_name);



var object_name = {
  property_1 : value_1,
  property_2 : value_2,
  property_3 : value_3,
  . . .
}
