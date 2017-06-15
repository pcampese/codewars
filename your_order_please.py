# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
  word_list_sorted = []    # Empty list to contained the sorted words
  word_list = sentence.split()    # Split sentence across whitespace, save as a list
    
  for num in range(1, len(word_list) + 1):    # For each number of total words in the sentence
      for word in word_list:                  # For each word in the word list
          if(str(num) in word):               # If the number is in that word
              word_list_sorted.append(word)   # Then append that word to a new word list
              
  sentence_sorted = ' '.join(word_list_sorted)    # Join the worted words with a space
  
  return sentence_sorted