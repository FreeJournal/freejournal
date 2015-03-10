import fcp


class FreenetConnection:
    def __init__(self):
        self.fcpNode = fcp.FCPNode(host="localhost")
          
    '''
    Put a text file onto the freenode network
    
    @param filename - String that will be used for the CHK
                      or content-hash keys
    @param data - The text data to add to freenode
    @return - complete URI for the file
    '''
    def put(self,data):
        job = self.fcpNode.put(data=data, mimetype="text/plain", async=True)
        '''
        Note, currently the async aspect is nullified by the wait 
        going on below, however it is useful for debugging purposes 
        so for now I will leave it as such.
        '''
        if job.isComplete(): 
            return uri
        else:
            job.wait()
        return uri

    '''
    Retrieve a text file from the freenode network
    @param uri - the 'CHK@' prepended URI for the file on the network
    @return - The textual data 
    '''
    def get(self, uri):
        job = self.fcpNode.get(uri, asynch=True)
        #Note, this currently returns just the data
        #other info like header, completion time is stored in the
        #dictionary in job[2]
        return job[1]
