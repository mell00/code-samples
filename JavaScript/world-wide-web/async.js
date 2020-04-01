//ASYNCHRONOUS JAVASCRIPT//

const button = document.querySelector('button');

const wikiUrl = 'https://en.wikipedia.org/api/rect_v1/page/summary/';

//Send AJAX request to GET data:
function getJSON(url) {
  const xhr = new XMLHttpRequest();
  xhr.open('GET',url);
  xhr.onload=()=>{
    if (xhr.status === 200){
      let data = JSON.parse(xhr.responseText);
      console.log(data);
    }
  };
  xhr.send();
}

//Initialize a promise:
const promise = new Promise(function(resolve,reject)=>{
  //asynchronous code that eventually calls either resolve(some_value) if fulfilled, or reject("failure reason"/some_other_value) if rejected
});

//.resolve()
promise.resolve(argument);

//.reject()
promise.reject(argument);

//.then()
promise.then(run_when_fullfilled[run_when_rejected]);

promise.then(value =>{//code executed when promise is fulfilled
}, reason =>{//code executed when promise is rejected
});

//.catch()
promise.catch(run_when_rejected);

promise.catch(function(reason){
  //code executed when promise is rejected
});

//.all()
promise.all([promise_1,promise_2,..,promise_n]);

promise.all([promise_1,promise_2,..,promise_n]).then(function(values){//code executed using values
});

var try_1 promise.all([promise_1,promise_2,..,promise_n]);

var try_2 promise.all([promise_3,promise_4,..,promise_n]);
.
.
var try_n promise.all([promise_5,promise_6,..,promise_n]);

setTimeout(function(){
console.log(try_1);
console.log(try_2);
console.log(try_n);});

//.finally()
promise.finally(run_when_settled);

promise.finally(function(){
  //code executed when promise is settled
});
