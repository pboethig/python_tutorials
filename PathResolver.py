import os

class PathResolver():

    path = ''


    def __init__(self, path):
        ''':param:path '''

        self.path = path

    def getPath(self):
        '''
        resolves an array with pathelements to a real path on the system
        :return: string the real path
        '''
        return os.path.join(* self.path) #asterics depacks a list to single arguments


resolved = PathResolver(['usr','local','bin'])

path = resolved.getPath()

print (path)



