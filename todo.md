Do I want the information returned from the prompts to be authenticated? How will I do the authentification? What if it's too slow using constant calls to openai? Do I need my own model/server? Seems like some information needs to authenticated and processed and modified at point of entry.

 I need the entire chatlog to be saved to the original database.

The current idealogy is using a language learning model to generate text responses based on previous text replies? Is that solid? What is wrong with this approach?

Task 1--
Collect information from the user with the ultimate aim being using that information to match people with each other. Should allow the user to upload photos as well. Connect fb, spotify? We need to understand which couples stay together, for what reasons and quantify the quality of the relationship.

 Task 2
 I need to provide guidelines on helping the user to date. I need to call openai to help with these guidelines. Not sure how to present them to the user. Through video or avatar? Will that be too slow?

 What information do I need? How do I ask for it in a creative way? In a storytelling format? 
 --
 Age
 Sex
 What relationships are they interested in?
 What is their description of their previous relationships? How do I tease out this information?
 What do they look like? 
 What do they want out of life? Should guidance or leading statements be offered here? Shouls something visual be presented here?
 How do they speak? Allow option to record audio? allow access to microphone? 
 Do you care about brands? 1-5
 How much do you care about being efficient?
 Are you talking to anyone atm?
 Can you describe them? I need to turn this description into some sort of guidance? 

 How do i gamify this experience?
 Story and art? Avatars?
 Should I have a conversation starter? 



Should we have a main app.py a login.py and a chat.py and a database.py?


 installs list
 1. pip install flask
 2. pip install flask_sqlalchemy
 3. pip install flask_login
 4. pip install openai
 6. pip install dotenv
 7. pip install -r requirements.txt

Potential chokepoints:
Need to set up database before the chat sequence can develop because certain responses need to be 
validated before an appropriate response can be given. Goal is to have 12 questions and responses.


