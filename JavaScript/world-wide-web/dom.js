//JAVASCRIPT AND THE DOM//

const element = document.getElementById('id');

const element = document.getElementsByTagName('tagName');

const element = document.getElementsByClassName('className');

const element = document.getElementsByName('name');

const element = document.querySelector('selector(s)');

const element = document.querySelector('element_name[attribute]');

element.textContent

element.innerHTML

element.type

element.className

element.title

element.getAttribute

const attribute = element.setAttribute;

element.setAttribute = 'attribute';

element.style.color = 'color';

element.style.width = #;

element.tagName

parent_node = child_node.parentNode;

previous_element_sibling_node = child_node.previousElementSibling;

previous_sibling_node = child_node.previousSibling;

next_element_sibling_node = child_node.nextElementSibling;

new_child_node = parent_node.insertBefore(new_child_node,child_node);

element.target

parent_node.children

parent_element_node.firstElementChild

parent_node.firstChild

parent_element_node.lastElementChild

parent_node.lastChild



var toggleList = document.getElementById('toggleList');
toggleList.addEventListener('click', () => {
  if(){listDiv.style.display = 'block';
  } else {listDiv.style.display = 'none';}});
button.addEventListener('click', () => {
  p.innerHTML = input.value + ':'});

document.createElement('element_name');

parent_element.appendChild('child_element');

node_element.appendChild('child_element');

parent_element.removeChild('child_element');

setTimeout(function(){executed_code;}, #_time_countdown);

target.addEventListener('event_type',listener[options]);

EventTarget.addEventListener('event_type', () => {executed_code;});
