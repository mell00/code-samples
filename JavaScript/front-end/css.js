//CSS AND JAVASCRIPT//

//Return CSS rule (stored in the getStyle variable) defined for specified element (el):
const getStyle = (el, ruleName) => getComputedStyle(el)[ruleName];

//Returns prefix of a CSS property (prop) that the browser supports:
const prefix = prop => {
  const capitalizedProp = prop.charAt(0).toUpperCase() + prop.slice(1);
  const prefixes = ['', 'webkit', 'moz', 'ms', 'o'];
  const i = prefixes.findIndex(
    prefix => typeof document.body.style[prefix ? prefix + capitalizedProp : prop] !== 'undefined'
  );
  return i !== -1 ? (i === 0 ? prop : prefixes[i] + capitalizedProp) : null;
};
