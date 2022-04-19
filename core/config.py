from pydantic import BaseSettings
from typingOptional import  Optional
from functools import lru_cache

class settings(BaseSettings):
    DATABASE_USERNAME: str = 'postgres'
    DATABASE_PASSWORD: str =  '123123'
    DATABASE_HOST: str = 'localhost'
    DATABASE_NAME: str = 'mydb'
    
    DATABASE_URI: str = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
    class config:
        case_sensitive: bool = True
        
@lru_cache    
def get_settings()-> settings:
    return settings

settings = get_settings()
