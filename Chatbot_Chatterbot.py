#Mrudula Bidvi
from chatterbot import ChatBot
from spacy.cli.download import download

download('en_core_web_sm')
#nlp=spacy.load('en_core_web_sm')
#bot = ChatBot('Buddy')
bot = ChatBot('Buddy', storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3')
#bot = ChatBot()
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
'Hi',
'Hello,how are you doing?',
'what,s up',
'Nothing much',
'I have a Question',
'Please elaborate your question',
'Can you tell the fees of the college per year for every department?',
'Yes,the fees for the all departments is 65,343',
'Does college provides scholarship?',
'Yes,college provides scholarships depending on your caste.',
'Which department has NBA accreditation ?',
'EXTC,COMP,IT,MECH',
'How many seats are available for each program?',
'For each program total 60 seats are available',
'Placement opportumity in college',
'Their is good placement opportunity in VCET college',
'Okay Thanks',
'No Problem! Have a Good Day!'
])
#response = bot.get_response('Hii')

#print("Bot Response:", response)
#Bot Response:( Please elaborate,your question )
name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)