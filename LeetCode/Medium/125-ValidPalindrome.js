/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  /**

  Iterate through the string and and check if it's ASCII Code is in between the alphanumeric values

  We can pop the last value of the array

  Range (64, 90) and (97, 122)

  */

  const word = s.split('').filter(char => {
    let letter = char.charCodeAt()
    if ((letter >= 65 && letter <= 90) || (letter >= 97 && letter <= 122) || (letter >= 48 && letter <= 57)) {
      return true
    }
  })

  // let word = s.split('').filter(char => {
  //     // (char >= 64 && char <= 90) || (char >= 97 && char <= 122)
  //     true
  // })

  let finalWord = ''

  for (let i = s.length - 1; i > -1; i -= 1) {
    let letter = s[i].charCodeAt()

    if ((letter >= 65 && letter <= 90) || (letter >= 97 && letter <= 122) || (letter >= 48 && letter <= 57)) {
      finalWord += String.fromCharCode(letter)
    }

  }

  console.log(word.join('').toLowerCase(), finalWord.toLowerCase())
  return word.join('').toLowerCase() === finalWord.toLowerCase()

};