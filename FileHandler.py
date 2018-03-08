import abc

class FileHandler(metaclass=abc.ABCMeta):
# remember to close the files when done with them. posably use with. doing this saves memory

#    def __init__(self, file):
#       file_name = file
#      file_content = ''

    def read_file(self):
        file_content = open(self.file_name,'r')
        #retrives data from a file
        return file_content

    def write_to_file(self):
        file_content = open(self.file_name, 'w')
        #creates a new file puts data in it
        # if file with same name exists replaces it

    def append_to_file(self):
        file_content = open(self.file_name,'a')
        #adds data to the end of a file


    @abc.abstractmethod
    def interprater(self,file_content):
        pass

    @abc.abstractmethod
    def format_data(self, data):
        pass