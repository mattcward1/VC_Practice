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
participant "Cleese's remote" as M
participant "Cleese's repo" as R
participant "Cleese's index" as I
participant Cleese as C

note right of C: nano index.md
note right of C: nano lakeland.md

note right of C: git add index.md
C->I: Add *only* the changes to index.md to the staging area

note right of C: git commit -m "Include lakes"
I->R: Make a commit from currently staged changes: index.md only

note right of C: git add lakeland.md
note right of C: git commit -m "Add Helvellyn"
C->I: Stage *all remaining* changes, (lakeland.md)
I->R: Make a commit from currently staged changes

note right of C: git push
R->M: Transfer commits to Github
"""

wsd(message, "git_diagram.png")
