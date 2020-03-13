//JAVASCRIPT AND HTML//

//Create an HTML element (el):
const createElement = str => {
  const el = document.createElement('div');
  el.innerHTML = str;
  return el.firstElementChild;
};

//Show all specified elements (via the show variable):
const show = (...el) => [...el].forEach(e => (e.style.display = ''));

//Hide all specified elements (via the hide variable):
const hide = (...el) => [...el].forEach(e => (e.style.display = 'none'));

//Return boolean value depending upon whether parent element (parent) contains specified child element (child):
const elementContains = (parent, child) => parent !== child && parent.contains(child);

//Insert HTML string (htmlString) before the end of specified element (el):
const insertBefore = (el, htmlString) => el.insertAdjacentHTML('beforebegin', htmlString);

//Insert HTML string (htmlString) after the end of specified element (el):
const insertAfter = (el, htmlString) => el.insertAdjacentHTML('afterend', htmlString);

//Return boolean value depending on whether element (el) has class (className):
const hasClass = (el, className) => el.classList.contains(className);

//Toggle a class (className) for an HTML element (el):
const toggleClass = (el, className) => el.classList.toggle(className);

//Trigger specific event (CustomEvent) of some event type (eventType), with optional custom data (detail), on a given element (el):
const triggerEvent = (el, eventType, detail) =>
  el.dispatchEvent(new CustomEvent(eventType, { detail }));

//Add event listener w/ event delegation (delegatorFn) to specified element (el):
const on = (el, evt, fn, opts = {}) => {
  const delegatorFn = e => e.target.matches(opts.target) && fn.call(e.target, e);
  el.addEventListener(evt, opts.target ? delegatorFn : fn, opts.options || false);
  if (opts.target) return delegatorFn;
};

//Remove event listener from specified element (el):
const off = (el, evt, fn, opts = false) => el.removeEventListener(evt, fn, opts);

//Remove HTML/XML tags from string (str):
const stripHTMLTags = str => str.replace(/<[^>]*>/g, '');

//Retrieve all images from within an element (el) and store within an array (images):
const getImages = (el, includeDuplicates = false) => {
  const images = [...el.getElementsByTagName('img')].map(img => img.getAttribute('src'));
  return includeDuplicates ? images : [...new Set(images)];
};

//Detect device type (mobile or laptop) used to open website:
const detectDeviceType = () =>
  /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
    ? 'Mobile'
    : 'Desktop';

//Callback function (onUserInputChange) to be executed whenever user input type changes:
const onUserInputChange = callback => {
  let type = 'mouse',
    lastTime = 0;
  const mousemoveHandler = () => {
    const now = performance.now();
    if (now - lastTime < 20)
      (type = 'mouse'), callback(type), document.removeEventListener('mousemove', mousemoveHandler);
    lastTime = now;
  };
  document.addEventListener('touchstart', () => {
    if (type === 'touch') return;
    (type = 'touch'), callback(type), document.addEventListener('mousemove', mousemoveHandler);
  });
  };

//Escape a string for use in HTML:
//NOTE: Use String.prototype.replace() with a regexp that matches the characters that need to be escaped, using a callback function to replace each character instance with its associated escaped character using a dictionary (object).
const escapeHTML = str =>
  str.replace(
    /[&<>'"]/g,
    tag =>
      ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        "'": '&#39;',
        '"': '&quot;'
      }[tag] || tag)
  );
