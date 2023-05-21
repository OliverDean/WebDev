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
 What would be a good parental gate?
 intent recognition, NLU accuracy, predictive and semantic capabilities?



Should we have a main app.py a login.py and a chat.py and a database.py?


--
Potential chokepoints:
Need to set up database before the chat sequence can develop because certain responses need to be 
validated before an appropriate response can be given. Goal is to have 12 questions and responses.
----

app.route('/start') and app.route('/chat') both are called by the js
along side we need a chat.html and start.html
i think extends from a base html is the way to go

Chat logic/collecting information from the user
--
Does the chat logic depend on the database? yes it depends on the session state: session["state"] and other session variables.
----

--
Holism:
How should fundamental differences between men and women be reflected in the software?
What questions define you as a person in the context of a relationship/long term relationship?
What sort of feedback should I get from the user experience?
What problems are most suitable to be solved by this app/apps in the context of finding and maintaining a relationship?
Relationships are difficult to maintain, why?

----

--
Practical todos:
clearing whitespace when logging in
When user navigates away from the page a popup should come up saying you have been logged out. 
Can't figure out how to make the chatbox scroll to the bottom
UX flows?
----

--
Photo upload:
User Interface: Create a user interface that allows users to select and upload photos. You can use HTML and JavaScript to implement a file upload input field where users can browse and select their photos.

Backend Handling: Once the user uploads a photo, your backend server (implemented using a framework like Flask) needs to handle the incoming request and process the uploaded photo. You can use a library like Flask-Uploads to handle file uploads in Flask.

Photo Processing: After receiving the uploaded photo, you can use image processing libraries like OpenCV or PIL to perform any necessary processing tasks. For example, you may want to resize the image, apply filters, or extract certain features from the photo.

Incorporate into Chatbot Logic: Integrate the uploaded photo into your chatbot's logic. Depending on the purpose of the photo upload, you can use the processed photo as input for further analysis or personalize the chatbot's responses based on the user's photo.

Privacy and Security: Ensure that you handle user photos securely and respect privacy concerns. Implement measures such as secure file storage, encryption, and compliance with data protection regulations.

Feedback and Interactions: Consider providing feedback to the user about the uploaded photo. You can use image recognition algorithms or APIs to analyze the photo and provide relevant responses or recommendations based on the content of the photo.
----


implement history done 
search userquestionanswer databases
look into flask ngrok done
css and java script review meh 
unit testing done ish
additional selenium test done 
chat questions rout work done 
login popup done

make api calls to chatgpt and or dali done 

