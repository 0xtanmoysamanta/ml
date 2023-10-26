import requests, json, time

def getFacts(data):
    """ returns a list, contains facts of dogs.
    Arg :Json object"""

    data = json.loads(data)
    body_01 = data["data"][0]["attributes"]["body"]
    body_02 = data["data"][1]["attributes"]["body"]
    body_03 = data["data"][2]["attributes"]["body"]
    body_04 = data["data"][3]["attributes"]["body"]
    body_05 = data["data"][4]["attributes"]["body"]

    content = [body_01, body_02, body_03, body_04, body_05]

    return content 

print('------------ Learn about Dogs -----------')    

while True:

    start_time = time.perf_counter()
    # ... code block ...
    
    url = "https://dogapi.dog/api/v2/facts?limit=5"

    data = requests.get(url)

    List = getFacts(data.content)

    for sentense in List:
        print(sentense)

    
    end_time = time.perf_counter()

    execution_time = end_time *1000  - start_time*1000 

    print(f"Time taken:{execution_time} milli seconds")

    user_input = input("Do you want to know the next facts? (y/n)")

    if user_input !='y':

        break 

    print("----------")
    
    


    
print('Thanks for your valuable time.')
