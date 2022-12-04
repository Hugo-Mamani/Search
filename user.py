import requests, json

name = input("your name > ")

host = "http://127.0.0.1:8080"

memory = ""
    
while True:
    
    res = requests.get(host)
    
    if res.status_code != 404:
        dusr = res.json()
        if dusr["msg"] != memory:
            print('by [{}] message: {}'.format(dusr["user"], dusr["msg"]))
            memory = input(f"your message {name} > ")
            requests.post(host, data={"user":name, "msg":memory})

    else: 
        memory = input(f"your message {name} > ")
        requests.post(host, data={"user":name, "msg":memory})
    if memory == 'q': break; print("exit by user")

