#Trie class definition
import math


class TrieNode:

    def __init__(self, end_of_word=False):
        '''
        Constructor
        :param end_of_word: be default set to false 
        '''
        self.__end_of_word = end_of_word
        self.__map = {}

    def check_for_letter(self, key):
        '''
        Function to check whether a key exists
        :param key: key to the map to check if a letter exists 
        :return: reference to the Trie Node if it exists, null if not
        '''
        if key in self.__map.keys():
            # key exists
            return self.__map[key]
        else:
            #key does not exist
            return None

    def get_end_of_word(self):
        return self.__end_of_word

    def get_map(self):
        return self.__map

    def get_node(self,key):
        return self.__map[key]

    def set_end_of_word(self, value):
        self.__end_of_word = value

    def insert_in_map(self, key, value):
        self.__map[key] = value

    def show_map(self):
        return str(self.__map)


class Trie:
    '''
        Class for Trie Data structure to insert strings
    '''
    #list_of_strings = ['keyring', 'keys', 'starwars', 'key','yek']
    #list_of_strings = ['key', 'as','yek']
    list_of_strings = ["geekf", "geeks", "or", "keeg", "abc", "bc"]

    def __init__(self):
        self.root = TrieNode(False)

    def insert_strings_into_trie(self):
        '''
        Function to insert every string into the trie data structure
        :return: true if success, false if not
        '''
        print "inserting into trie"
        for string in self.list_of_strings:
            self.insert_into_trie(string)

    def insert_into_trie(self, string):
        self.insert(string, 0, self.root, False)

    def insert(self,string, index, node, end_of_word):
        if index == len(string):
            if node.get_end_of_word() == False:
                node.set_end_of_word(True)
            return True
        #print "running the function for " + str(string[index]) + " in " + string + " having " + node.show_map()
        if node.check_for_letter(string[index]) and end_of_word == node.get_end_of_word():
            if end_of_word == False:
                if index+1 != len(string):
                    self.insert(string, index+1, node.get_node(string[index]), False)
                else:
                    self.insert(string, index + 1, node.get_node(string[index]), True)
            else:
                return True
        elif node.check_for_letter(string[index]) == None and end_of_word == node.get_end_of_word():
            #letter is not there
            if index+1 == len(string):
                new_node = TrieNode(True)
                node.insert_in_map(string[index], new_node)
                print node.show_map()
                self.insert(string, index + 1, new_node, True)
            else:
                new_node = TrieNode(False)
                node.insert_in_map(string[index], new_node)
                print node.show_map()
                self.insert(string, index + 1, new_node, False)
        else:
            return False

    def check_string_exists(self, string):
        if self.check_letter(string, 0, self.root, False):
            return True
        else:
            return False

    def check_letter(self,string,index,node, end_of_word,end_of_word_check=True):
        #print "calling check letter for " + "string: "+ string + " index " + str(index) + " Node : " + str(node.get_map())
        if index == len(string):
            if end_of_word_check == True:
                if node.get_end_of_word() != end_of_word:
                    return False
                else:
                    return True
            else:
                return True
        if node.check_for_letter(string[index]):
            print "Found letter " + string[index] + " in " + node.show_map()
            if index+1 == len(string):
                if self.check_letter(string, index + 1, node.get_node(string[index]), True):
                    pass
                else:
                    return False
            else:
                if self.check_letter(string, index + 1, node.get_node(string[index]), False):
                    pass
                else:
                    return False
        else:
            print "could not find " + string[index] + " in " + node.show_map()
            return False
        return True

    def find_letter(self, prefix, node,list):
        if node.get_end_of_word():
            list.append(prefix)
        for character in node.get_map().keys():
            self.find_letter(prefix+character,node.get_node(character),list)

    def reach_node_with_prefix(self,prefix):
        node = self.root
        for i in range(0,len(prefix)):
            if node.check_for_letter(prefix[i]):
                node = node.get_node(prefix[i])
            else:
                print "Could not find " + prefix[i] + " in node " + str(node.show_map())
                return None
        return node

    def get_words_with_prefix(self, prefix):

        node = self.reach_node_with_prefix(prefix=prefix)
        if node:
            final_list = []
            self.find_letter(prefix, node=node, list=final_list)
            return final_list
        else:
            return None


    def word_formation_concat_words(self,word):
        '''
        Function to do word formation by concatenating 
        :param word: 
        :return: 
        '''
        for i in range(1,len(word)):
            if self.check_string_exists(word[0:i]) and self.check_string_exists(word[i:]):
                print "word " + word + " can be formed from " + word[0:i] + " and " + word[i:]
                break


    def check_if_palindrome(self,string, node):
        if self.check_letter(string=string,index = 0,node = node,end_of_word=False,end_of_word_check=False):
            return True
        else:
            return False

    def check_if_two_words_form_palindrome(self):
        #reverse the list of strings
        flag = False
        new_list_of_strings = [item[::-1] for item in self.list_of_strings]
        for string in new_list_of_strings:
             if self.check_if_palindrome(string,self.root):
                 list_of_words = trie.get_words_with_prefix(string)
                 for word in list_of_words:
                     if self.is_palindrome(string[::-1], word):
                        print "Strings that are palindrome are " + string[::-1] + "  and  " + str(word)
                        flag = True
        if flag == True:
            return True
        else:
            return False

    def is_palindrome(self,word1,word2):
        word = str(word1) + str(word2)
        return word == ''.join(reversed(word))

if __name__ == '__main__':
    trie = Trie()
    trie.insert_strings_into_trie()
    print "####"
    print trie.root.get_map()
    print "####"
    #print trie.check_string_exists("keyring")
    #list_of_words = trie.get_words_with_prefix("k")
    #for item in list_of_words:
    #   print item
    #trie.word_formation_concat_words("keystarwars")
    trie.check_if_two_words_form_palindrome()
