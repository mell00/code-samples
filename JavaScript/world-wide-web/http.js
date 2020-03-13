//JAVASCRIPT HTTP//

//Make GET request to specified URL (url):
const httpGet = (url, callback, err = console.error) => {
  const request = new XMLHttpRequest();
  request.open('GET', url, true);
  request.onload = () => callback(request.responseText);
  request.onerror = () => err(request);
  request.send();
};

//Make POST request to specified URL (url):
const httpPost = (url, data, callback, err = console.error) => {
  const request = new XMLHttpRequest();
  request.open('POST', url, true);
  request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
  request.onload = () => callback(request.responseText);
  request.onerror = () => err(request);
  request.send(data);
};

//Return boolean value depending upon whether or not the current runtime environment (window and document) is a browser, so that front-end modules can run on the server (Node) without throwing errors:
const isBrowser = () => ![typeof window, typeof document].includes('undefined');

//Return current URL:
const currentURL = () => window.location.href;

//Redirect to specified URL (url); stimulate link click (asLink=true) or HTTP redirect (asLink=false):
const redirect = (url, asLink = true) =>
  asLink ? (window.location.href = url) : window.location.replace(url);

//Redirect page to HTTPS if currently in HTTP:
  const httpsRedirect = () => {
    if (location.protocol !== 'https:') location.replace('https://' + location.href.split('//')[1]);
  };

//Return object (getURLParameters) containing parameters of the current URL (url):
  const getURLParameters = url =>
    (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
      (a, v) => ((a[v.slice(0, v.indexOf('='))] = v.slice(v.indexOf('=') + 1)), a),
      {}
    );

//Return boolean value depending upon whether or not given string (str) is an absolute URL or not:
const isAbsoluteURL = str => /^[a-z][a-z0-9+.-]*:/.test(str);

//Join all inputted URL segments to form normalized URL:
const URLJoin = (...args) =>
  args
    .join('/')
    .replace(/[\/]+/g, '/')
    .replace(/^(.+):\//, '$1://')
    .replace(/^file:/, 'file:/')
    .replace(/\/(\?|&|#[^!])/g, '$1')
    .replace(/\?/g, '&')
    .replace('&', '?');

//Generate UUID in a browser:
const UUIDGeneratorBrowser = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, c =>
    (c ^ (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))).toString(16)
  );

//Generate UUID in Node.js:
const crypto = require('crypto');
const UUIDGeneratorNode = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, c =>
    (c ^ (crypto.randomBytes(1)[0] & (15 >> (c / 4)))).toString(16)
  );

//Parse an HTTP cookie header string and return an object of all cookie name-value pairs:
const parseCookie = str =>
  str
    .split(';')
    .map(v => v.split('='))
    .reduce((acc, v) => {
      acc[decodeURIComponent(v[0].trim())] = decodeURIComponent(v[1].trim());
      return acc;
    }, {});

//Serialize given cookie name-value pair (name, val) into a set-cookie header string (serializeCookie):
const serializeCookie = (name, val) => `${encodeURIComponent(name)}=${encodeURIComponent(val)}`;
