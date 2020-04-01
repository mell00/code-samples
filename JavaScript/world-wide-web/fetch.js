//FETCH JAVASCRIPT//

fetch()

fetch(data).then(response => response.json());

fetch(data).catch(response => response.json());

function fetch(url){
  return fetch(url).then(response=>response.json())}
  
const variable =(async function(){
  const response = await fetch ('...');})();
