import fcp
import telnetlib

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
        tn = telnetlib.Telnet("localhost",2323)
        tn.read_until("TMCI> ")
        tn.write("GETCHK:"+data + "\n")
        uri =tn.read_until("TMCI> ")
        uri = uri.split('\r\n')[0]
        print(uri)
        if job.isComplete():
            return uri
        else:
            print("Please wait for upload")
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

#Here's a little test we can run to practice a small put
c = FreenetConnection()
print(c.get("CHK@XNpzyZhvxvkgIBgYuZzeJTSpRBPnR0VibpISMc8rHV4,4rsKU2MpJzpQxr91fPTV-wGpd14o~ns3hjLi0HMtwFI,AAMA--8"))
c.put("Try this test out~")
