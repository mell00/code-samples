//CALLBACK FUNCTIONS IN JAVASCRIPT//

function callback_function(){executed_code};
function executor_function(callback){more_executed_code};
executor_function(callback_function);

function (){executed_code};

() => {executed_code};

() => executed_code;

setTimeout(callback_function, delay_of_#_milliseconds);

setTimeout (() => {executed_code}, delay)

const timeoutID = setTimeout(callback, delay);
clearTimeout(timeoutID);

setInterval (() => {executed_code}, delay);

const intervalID = setInterval (() => {executed_code}, delay);
clearInterval(intervalID);

function callback_function(){executed_code};
element.addEventListener('event_type', callback_function)
