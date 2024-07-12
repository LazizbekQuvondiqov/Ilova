from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from search import search_herb
from qa import qa_class

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

class search_answer(BaseModel):
    title: str
    description: str
    img_link: str
    disease: str

class random_answer(BaseModel):
    title: str
    description: str
    img_link: str
    disease: str
   
    
class search_name(BaseModel):
    name: str 



class question(BaseModel):
    name: str 

@app.post('/search',response_model=List[search_answer])
def search(form:search_name):
    
    return   search_herb.search(form.name)


@app.post('/answering',response_model=List[search_answer] )
def answering(form:question):
    return  qa_class.answering(str(form.name.lower()).split(','))
        
    

@app.post('/random',response_model=List[random_answer])
def random():
    return search_herb.random()









# uvicorn server:app --reload