'''
Created on Nov 18, 2018

@author: Mgmi
'''
'''
This is doc string
This function finds the words in sentences
and stores them in a list

@param sentence_list: a list containing all the sentences
@return: a list containing the individual words
'''
def find_word(sentence_list):
    word_list=[]
    for sentence in sentence_list:
        for word in sentence.split():
            word_list.append(word)
    return word_list

def print_word(word_list):
    print ('The list of words are:')
    for word in word_list:
        print(word)
    
def main():
    sentence_list=['This is my first file','What is your name','Where is your school located']
    word_list=find_word(sentence_list)
    print_word(word_list)

if __name__ == '__main__':
    main()
    