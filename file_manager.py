class FileManager():
    """
    Class is used to open, read, write, and close text files.
    """

    def open_file( self, filename : str ) -> str:
        """
        Open file based on filename and parameters passed
        """
        file = open( filename, "r+" ) # Open file
        data = file.readlines() # Read data in file

        return( data ) # print data