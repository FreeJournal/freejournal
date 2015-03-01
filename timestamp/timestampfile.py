
# coding: utf-8

# In[7]:

import requests
import hashlib
import time


# In[8]:

status_url = 'http://www.proofofexistence.com/api/v1/status'
register_url = 'http://www.proofofexistence.com/api/v1/register'


# In[9]:

"""
Timestamps a file by sending a hashed document to proofofexistence.com
after paying the minimum BTC value.

@param File_Hash A SHA256 Hash
@return Returns a dictionary with payment bitcoin address and amount to pay
"""

class timestampfile:

    def __init__(self, File_Hash):
        self.File_Hash = File_Hash
    
    def request_timestamp (self):
        returnval = {'pay_address':"", 'price':"", 'id':self.File_Hash}
        params = {'d': self.File_Hash}
        r = requests.post(status_url, data=params, timeout=10)
    
        """
        Statement will check the status code in case a problem has been detected.
        HTTP status code (200 OK) is desired.
        """
        if r.status_code != 200:
            
            print("Error: HTTP Status Code " + r.status_code + ". " + "The request was not succeeded, expected staus code '200'. \n")
            return -1
        
        text = r.json()
        
        """
        Success entry is either True or False. 
        If False, then it is possible that the document digest is not registered at proofofexistence.
        If True, then in this function the 'status' entry will be 'registered'
        then payment address and payment address return

        """
        
        if text['success'] == False:
            
            """
            Our response object returns the reason we failed, which in this case
            is because the document's digest has not been registered at proofofexistence.com.
            This will an HTTP POST request using the register_url instead of status_url to register the hash.
            """
            if text['reason'] == 'nonexistent':
                
                r = requests.post(register_url, data=params)
                text = r.json()
                
                if text['success'] == False:
                    
                        print("Opps, failed to register digest! \n")
                        return -1

        """
        after the file is registered, text['success'] turned to True.
        get and return the payment value and payment address.
        """
        if text['success'] == True:
            
            r = requests.post(status_url, data=params)
            text = r.json()
            
            if text['status'] == 'registered':
                
                    returnval['pay_address'] = text['pay_address']
                    returnval['price'] = text['price']
        
        return returnval
    


    """
    Check the file's timestamp values
    if file is not timestamp return -1
    if file is timestamp
    @:param:none
    @return: a dictionary contain whether it is timestamp, time value and transaction number
    """
    
    def check_TimeStamp(self):

        File_Hash = self.File_Hash
        params = {'d': File_Hash}
        r = requests.post(status_url, data=params, timeout=10)
        
        returnval = {'timestamp': False, 'time': "", 'Transaction': "" }
        """
        Statement will check the status code in case a problem has been detected.
        HTTP status code (200 OK) is desired.
        """
        if r.status_code != 200:
            
            print("Error: HTTP Status Code " + r.status_code + ". " + "The request was not succeeded, expected staus code '200'. \n")
            return -1
        
        text = r.json()
        
        
        """
        when text['success'] is False, return -1

        """
        
        if text['success'] == False:
            
            """
            Our response object returns the reason we failed, which in this case
            is because the document's digest has not been registered at proofofexistence.com.
            This will an HTTP POST request using the register_url instead of status_url to register the hash.
            """
            return -1

        """
        when text['success'] is True, assign data into dictionary only when text['status'] is confirmed

        """
                 
        if text['success'] == True:
            
            r = requests.post(status_url, data=params)
            text = r.json()

            if text['status'] == 'pending':

                print("Your payment has been received. Please wait at least 1 minute for your payment to be certified. \n")

                #Payment needs at least 1 minute to confirm the transaction. Set 10 minute time limit.
                ''''
                keep checking the status until pending change to confirmed
                '''''
                time_out_count = 0
                while(text['status'] == 'pending'):

                    if time_out_count > 10:

                        print("Maximum 10 minute time limit exceeded. Transaction not confirmed. \n")
                        break

                    time_out_count += 1
                    time.sleep(60)
                    r = requests.post(status_url, data=params)
                    text = r.json()

                    if text['status'] == 'confirmed':

                        returnval['timestamp']=True

                    else:
                        return -1

            elif text['status'] == 'confirmed':
                returnval['timestamp'] = True
            
            else :
                return -1

        if returnval['timestamp'] == True:
            returnval['time']= text['txstamp']
            returnval ["Transaction"] = text['transaction']
        return returnval
        #printing r
        # eponse object for debugging purposes






    
    
