#Mrudula Bidvi
from nltk.chat.util import Chat, reflections

QA=[
    [
      r"hi|hey|hello",
        ["Hello","Hey there"]
    ],
    [
    r"(.*) companys had came for the placements of final year students?",
        ["TCS,Infosys,TATA,and many more"]
    ],
    [
        r"How are the faculty of (.*) department?",
        [ "The faculty of %1 department  are exceptional!With varied interests and miltidisciplinary skills." ]
    ],
    [
        r"Please give the contact no of college",
        [ "The contact of college is +91 984376549 " ]
    ],
    [
        r"On which site does college provides free courses for students",
        ["The free courses are provided o Coursera "]
    ],
]
def bott():
    print("Hii,Bott I know you want to know about VCET college,i beleive thats why you are here")
    chat=Chat(QA,reflections)
    chat.converse()

if __name__ == "__main__":
    bott()