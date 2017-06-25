#Trie class definition


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
        self.__map = value

    def insert_in_map(self, key, value):
        self.__map[key] = value

    def show_map(self):
        return str(self.__map)


class Trie:
    '''
        Class for Trie Data structure to insert strings
    '''

    def __init__(self):
        self.list_of_strings = ['keyring','keys','starwars','key']
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
        print "running the function for " + str(string)
        self.insert(string, 0, self.root, False)

    def insert(self,string, index, node, end_of_word):
        if index == len(string):
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
        self.check_letter(string, 0, self.root, False)
        return True

    def check_letter(self,string,index,node, end_of_word):
        if index == len(string):
            if node.get_end_of_word() != end_of_word:
                return False
            else:
                return True
        if node.check_for_letter(string[index]):
            print "Found letter " + string[index] + " in " + node.show_map()
            if index+1 == len(string):
                self.check_letter(string,index + 1,node.get_node(string[index]), True)
            else:
                self.check_letter(string, index + 1, node.get_node(string[index]), False)
        else:
            print "could not find " + string[index] + " in " + node.show_map()
            return False

if __name__ == '__main__':
    trie = Trie()
    trie.insert_strings_into_trie()
    print trie.check_string_exists("keys")
