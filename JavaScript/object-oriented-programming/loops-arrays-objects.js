//LOOPS, ARRAYS, AND OBJECTS IN JAVASCRIPT//

//Loops:

while (condition) {executed_code}

do {executed_code} while (condition)

for (var i=initial_#; i++ OR i--; i<final_#) {executed_code}

loop(){if(condition) {
  break;
}}

//Arrays:

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

//Array iteration methods:

for (let i=0; i<array.length; i+=1) {const var = array[i]};

array.forEach(var => console.log(var));
OR
array.forEach(function callback_function(current_value,index,new_array));

array.filter((params) => {return some_conditional_statement_that_if_true_adds_item_to_array});
OR
array.filter(params) => return some_conditional_statement_that_if_true_adds_item_to_array;

array.map((params) => {changes_made_to_array_items});

array.reduce(callback_function(accumulator,current_value));
OR
array.reduce(callback_function(accumulator,current_value)).chained_method1().chainedmethod2();

//Longest item in array:
const longestItem = (...vals) => vals.reduce((a, x) => (x.length > a.length ? x : a));

//Most frequent element in array:
const mostFrequent = arr =>
  Object.entries(
    arr.reduce((a, v) => {
      a[v] = a[v] ? a[v] + 1 : 1;
      return a;
    }, {})
  ).reduce((a, v) => (v[1] >= a[1] ? v : a), [null, 0])[0];

//Split and categorize elements into two groups:
const bifurcate = (arr, filter) =>
  arr.reduce((acc, val, i) => (acc[filter[i] ? 0 : 1].push(val), acc), [[], []]);

//Create array of elements ordered by position in original arrays:
const zip = (...arrays) => {
  const maxLength = Math.max(...arrays.map(x => x.length));
  return Array.from({ length: maxLength }).map((_, i) => {
    return Array.from({ length: arrays.length }, (_, k) => arrays[k][i]);
  });
};

//Create array of arrays from ungrouping elements from a zip:
const unzip = arr =>
  arr.reduce(
    (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
    Array.from({
      length: Math.max(...arr.map(x => x.length))
    }).map(x => [])
  );

//Create array of elements; grouped based on position in original arrays, using function as last value specifying how grouped values are combined:
const zipWith = (...array) => {
  const fn = typeof array[array.length - 1] === 'function' ? array.pop() : undefined;
  return Array.from({ length: Math.max(...array.map(a => a.length)) }, (_, i) =>
    fn ? fn(...array.map(a => a[i])) : array.map(a => a[i])
  );
};

//Count elements in an array:
const countBy = (arr, fn) =>
  arr.map(typeof fn === 'function' ? fn : val => val[fn]).reduce((acc, val) => {
    acc[val] = (acc[val] || 0) + 1;
    return acc;
  }, {});

//Objects:

var object_name = {
  property_1 : value_1,
  property_2 : value_2,
  property_3 : value_3,
  . . .
}

object_name['property_name']
OR
object_name.property_name

object_name.property_name.sub_property_name

object_name.property_name.property_method_name

var object_name = {};
object_name.new_property_name = new_property_value;

for (var property_name in object_name) {
  console.log(property_name);
}

for (var property_name in object_name) {
  console.log(object_name[property_name]);
}

var array_name = [object_1, object_2, .., object_#];

//Return object associating valid property identifiers (props) from one array and values (values) from a second array:
const zipObject = (props, values) =>
  props.reduce((obj, prop, index) => ((obj[prop] = values[index]), obj), {});

//Map values of array to object using function (key-value pairs consisting of stringified value as key and mapped value):
const mapObject = (arr, fn) =>
  (a => (
    (a = [arr, arr.map(fn)]), a[0].reduce((acc, val, ind) => ((acc[val] = a[1][ind]), acc), {})
  ))();

//Return query string (queryString) generated from key-value pairs of given object:
const objectToQueryString = queryParameters => {
    return queryParameters
      ? Object.entries(queryParameters).reduce((queryString, [key, val], index) => {
        const symbol = queryString.length === 0 ? '?' : '&';
        queryString += typeof val === 'string' ? `${symbol}${key}=${val}` : '';
        return queryString;
      }, '')
      : '';
  };
