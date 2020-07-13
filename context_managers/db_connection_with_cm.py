import mysql.connector

class MYSQLConnectionManager(): 
    def __init__(self, hostname,user, password): 
        self.hostname = hostname  
        self.user=user
        self.password=password
        self.con = None
  
    def __enter__(self): 
        self.con = mysql.connector.connect(host=self.hostname, user=self.user, password=self.password)
        self.cur=self.con.cursor()
        return self
  
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.con.close() 

with MYSQLConnectionManager('localhost', 'root','Neerav123!') as mys:
    #do what you want to watch 
             
  
