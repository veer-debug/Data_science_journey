import json


class Database:
    def insert(self,name,email,password):
        with open(r'C:\Users\theve\OneDrive\Desktop\DATA-S\IPL_GUI_API\users.json','r') as rf:
            user=json.load(rf)
            
            if email in user:
                return 0
            else:
                user[email]=[name,password]
                
        with open(r'C:\Users\theve\OneDrive\Desktop\DATA-S\IPL_GUI_API\users.json','w')as wf:
            json.dump(user,wf,indent=4)
            return 1
        
        
    def search(self,email,password):
        with open(r'C:\Users\theve\OneDrive\Desktop\DATA-S\IPL_GUI_API\users.json','r') as rf:
            user=json.load(rf)
            
            if email in user:
                if user[email][1]==password:
                    return 1;
                else:
                    return 0
            else:
                return 0
        