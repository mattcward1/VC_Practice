import requests
import re
#import IPython (for displaying images in Jupyter notebooks)

def wsd(code, output_file = "diagram.png"):
    response = requests.post(
        "http://www.websequencediagrams.com/index.php", 
        data={
            'message': code,
            'apiVersion': 1,
    },
)
    expr = re.compile(r"(\?(img|pdf|png|svg)=[a-zA-Z0-9]+)")
    m = expr.search(response.text)
    if m is None:
        print("Invalid response from server.")
        return False
    
    image = requests.get("http://www.websequencediagrams.com/" + m.group(0))
    with open(output_file, "wb") as f:
        f.write(image.content)

    print(f"Saved diagram to {output_file}")
    return output_file

wsd("Sender->Recipient: Hello\nRecipient->Sender: Message recieved OK")

message="""
Working Directory -> Staging Area : git add
Staging Area -> Local Repository : git commit
Working Directory -> Local Repository : git commit -a
Staging Area -> Working Directory : git checkout
Local Repository -> Staging Area : git reset
Local Repository -> Working Directory: git reset --hard
Local Repository -> Remote Repository : git push
"""

wsd(message, "git_diagram.png")
