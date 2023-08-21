
from handler import generateTweets

sample_event = {
    "Records": [
        {"name": "John", "age": "30"},
        {"name": "Jane", "age": "25"}
    ]  
}  

def main():
   print(generateTweets(sample_event,None))
 

if __name__ == "__main__":  
    main()