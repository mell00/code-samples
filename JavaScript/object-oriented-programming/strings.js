//JAVASCRIPT STRINGS//

//Capitalize selected character of string:
char.toUpperCase()

//Decapitalize selected character of string:
char.toLowerCase()

//Converts string to camelcase:
const toCamelCase = str => {
  let s =
    str &&
    str
      .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
      .map(x => x.slice(0, 1).toUpperCase() + x.slice(1).toLowerCase())
      .join('');
  return s.slice(0, 1).toLowerCase() + s.slice(1);
};

//Return boolean value depending on whether string is upper-case:
char.isUpperCase()

//Return boolean value depending on whether string is lower-case:
char.isLowerCase()

//Capitalize first letter of string:
const capitalize = ([first, ...rest], lowerRest = false) =>
  first.toUpperCase() + (lowerRest ? rest.join('').toLowerCase() : rest.join(''));

//Decapitalize first letter of string:
  const decapitalize = ([first, ...rest], upperRest = false) =>
    first.toLowerCase() + (upperRest ? rest.join('').toUpperCase() : rest.join(''));

//Determine whether pattern string (pattern) matches with main string (str):
  const isSimilar = (pattern, str) =>
    [...str].reduce(
        (matchIndex, char) =>
            char.toLowerCase() === (pattern[matchIndex] || '').toLowerCase()
                ? matchIndex + 1
                : matchIndex,
        0
    ) === pattern.length;

//Capitalize first letter of every word of string:
const capitalizeEveryWord = str => str.replace(/\b[a-z]/g, char => char.toUpperCase());

//Create new string (mapString) from mapping function (fn) onto every character in calling string (str):
const mapString = (str, fn) =>
  str
    .split('')
    .map((c, i) => fn(c, i, str))
    .join('');

//Indent each line in string (str):
const indentString = (str, count, indent = ' ') => str.replace(/^/gm, indent.repeat(count));

//Converts string object -> base-64 encoded ASCII string where each string char treated as a byte of binary data:
const btoa = str => Buffer.from(str, 'binary').toString('base64');

//Decodes base-64 encoded ASCII string -> string object
const atob = str => Buffer.from(str, 'base64').toString('binary');
