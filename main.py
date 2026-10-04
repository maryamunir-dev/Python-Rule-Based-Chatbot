#mini project
import datetime

presentHour = datetime.datetime.now().hour

if 5<= presentHour <= 11:
    print("Good Morning")
elif 11<= presentHour <= 17:
    print("Good Afternoon")
elif 17<= presentHour <= 20:
    print("Good Evening")
else: 
    print("Good Night")

print("Welcome! I'm your personal chat assistant.")
print("How can I help you today? Type 'bye' anytime to exit.")

#Chatbot memory creation
responses = {
    "hello": "Hello! Nice to meet you.",
    "hi": "Hi! How are you doing?",
    "hey": "Hey!  How can I help you?",
    "how are you": "I'm doing great! Thanks for asking. ",
    "what is your name": "I'm your personal chat assistant.",
    "who are you": "I'm a simple Python-based personal chat assistant.",
    "what can you do": "I can chat with you, answer simple questions, and keep you company.",
    "thank you": "You're welcome!",
    "thanks": "You're welcome! Happy to help.",
    "motivate me": "Believe in yourself! Every small step brings you closer to your goals. ",
    "i am tired": "Take a short break, breathe, and come back when you're ready. ",
    "i am happy": "That's wonderful! Keep that positive energy going! ",
    "i am sad": "I'm sorry you're feeling this way. Take it one step at a time. ",
    "bye": "Goodbye!  Have a great day!"
}

#Method / Function to get the response of chatbot 
def getResponseofbot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return"I am not able to answer yet.I am still learning."

#Clean Single Chat Loop
while True:
    userinput = input("Ask Question!: ")


    if "bye" in userinput.lower():
        print("Bot Response: Goodbye! Have a great day!")
        break

    reply = getResponseofbot(userinput)
    print("Bot Response:", reply)