
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
@return Returns a bitcoin transaction id (txid). Returns -1 if failed.
"""


def TimeStamp(File_Hash):
    
    params = {'d': File_Hash}
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
    If True, then the 'status' entry is either 'registered', 'pending' or 'confirmed'.
        If entry is 'registered' then payment needs to be made.
        If entry is 'pending' then payment has been made and is awaiting entry into the blockchain to confirm transaction.
        If entry is 'confirmed' then payment for that particular digest has been made.
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
             
    if text['success'] == True:
        
        r = requests.post(status_url, data=params)
        text = r.json()
        
        if text['status'] == 'registered':
            
                BTC_price = text['price']
                Pay_Address = text['pay_address']
                print("Please pay a minimum value of " + str(BTC_price) + " satoshis to address " + "'" + Pay_Address + "'" + "\n")
                input("If you have submitted your payment. Press Enter to continue...")
        
        if text['status'] == 'pending':
            
            print("Your payment has been received. Please wait at least 1 minute for your payment to be certified. \n")
            
            #Payment needs at least 1 minute to confirm the transaction. Set 10 minute time limit.
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
                
                txid = text['transaction']
                txstamp = text['txstamp']
                
                print("Done, confirmed documents! \n"  + "Bitcoin transaction id (txid): " + txid + "\n"+ "Transaction timestamp: " + txstamp + "\n")
                return txid
            
        elif text['status'] == 'confirmed':
            
            print("Document already confirmed! \n")
            return(text['transaction'])
        
        else:
            #Statement is called if the function is run again after the hash has already been registered and no payment has been made.
            print("A payment was not recieved. Please submit a payment in order to perform a timestamp. \n")
            
            
    #printing reponse object for debugging purposes        
    print(r.json())
    return -1


# In[10]:




# In[27]:




# In[ ]:



