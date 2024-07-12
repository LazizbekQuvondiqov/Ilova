import sqlite3 
import random

from fuzzywuzzy import process



class search_herb:
    @staticmethod
    def connect_db()->list:
        
        conn = sqlite3.connect('data.db')
        c= conn.cursor()

        data = c.execute('SELECT * FROM data')
       
        return [
            {
                

            'title': row[0],
            
            'data': {
                'title': row[0],
                'description': row[1],
                'img_link': row[2] ,
                'disease': row[3],
                  }
            }
             
             for row in data
        ]
       
    @staticmethod
    def search(query:str)->float:
        data = search_herb.connect_db()
        titles = [item['title'] for item in data]
        best_match = process.extractOne(query, titles, score_cutoff=70)
        if best_match:
            result = next((item['data'] for item in data if item['title'] == best_match[0]), None)
            return [result] if result else []
        return []  


    @staticmethod
    def random()->list:
        data = search_herb.connect_db()
        # get 5 items random from data at list 
        return random.sample([item['data'] for item in data], 6)    
    



        
    
    
    



    


        

    

  
    

        

      


        
        
