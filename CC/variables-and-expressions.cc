//C VARIABLES AND EXPRESSIONS//

#include <stdio.h>
#include <filename.h> OR "filename.h"

#define PI 3.14
#define HALFOF(x) x/2
#define abs(x) ((x) >= 0 ? (x) : -(x))
#define sgn(x) ((x) > 0 ? 1 : ((x) < 0 ? -1 : 0))

//Initialize variable:
type var_name;

type var_name1,var_name2,var_name3;

type *var_name;

type var_name = value;

type *var_name = value;

var_name = value;

//Initialize pointer (variable)

//Data types:
  char = 'ASCII_character';
  int = 1;
  float = 1.0;
  double = 1.00;
  unsigned = +1;
  signed = ±1;
  long = 2(1);
  short = 0.5(1);

  void = 'no_data_type_,_reserved_for_functions';

  void main(int argc, char *argv[]){
    function_name()
    {
      //insert code here
    }

  void_function(void){
    executed_code;
  }

  if (condition){
    executed_code;
  }

  if (condition){
    executed_code;
  } else {
    alternate_executed_code;
  }


  switch (condition){
    case 0:
      executed_code_0;
      break;
    case 1:
      executed_code_1;
      break;
    case 2:
      executed_code_2;
      break;
    case 3:
      executed_code_3;
      break;
    case 4:
      executed_code_4;
      break;
    default:
      executed_code;
      break;
  }

for (int i = 0; i < count; i++) {
  executed_code;
}

int i = initial_#;

while (condition_involving_i){
  executed_code;
  iteration_statement_like_i++;
}

do {
  executed_code;
  iteration_statement_like_i++
} while (condition_involving_i);

for (int i = 0; i < count; i++) {
  executed_code;
  if (i < 10){
    continue;
  }
  if (i >= 10){
    break;
  }
}


goto statement;
for (int i = 0; i < count; i++) {
  executed_code;
  if (i < 10){
    continue;
  }
  if (i >= 10){
    break;
  }
statement:

for (int i = 0; i < count; i++) {
  executed_code;
  if (i < 10){
    continue;
  }
  if (i >= 10){
    goto statement;
  }}
statement: statement_executed_when_goto_statement_is_called


function(argc){
  argc++;
  return argc;
}

}
