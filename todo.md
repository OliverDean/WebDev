
----
Overall concept tasks:
Task 1--
Collect information from the user with the ultimate aim being using that information to match people with each other. Should allow the user to upload photos as well. Connect fb, spotify? We need to understand which couples stay together, for what reasons and quantify the quality of the relationship.
 ----

----
Idea free flow:

 What information do I need? How do I ask for it in a creative way? In a storytelling format? 
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
----

--
Potential chokepoints:

Need to set up database before the chat sequence can develop because certain responses need to be 
validated before an appropriate response can be given. Goal is to have 12 questions and responses. /done
----

----
Chat logic/collecting information from the user:

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
When user navigates away from the page a popup should come up saying you have been logged out. 
Can't figure out how to make the chatbox scroll to the bottom
UX flows?
----

--
Product Features:

Photo upload:
User Interface: Create a user interface that allows users to select and upload photos. You can use HTML and JavaScript to implement a file upload input field where users can browse and select their photos.

Backend Handling: Once the user uploads a photo, your backend server (implemented using a framework like Flask) needs to handle the incoming request and process the uploaded photo. You can use a library like Flask-Uploads to handle file uploads in Flask.

Photo Processing: After receiving the uploaded photo, you can use image processing libraries like OpenCV or PIL to perform any necessary processing tasks. For example, you may want to resize the image, apply filters, or extract certain features from the photo.

Incorporate into Chatbot Logic: Integrate the uploaded photo into your chatbot's logic. Depending on the purpose of the photo upload, you can use the processed photo as input for further analysis or personalize the chatbot's responses based on the user's photo.

Privacy and Security: Ensure that you handle user photos securely and respect privacy concerns. Implement measures such as secure file storage, encryption, and compliance with data protection regulations.

Feedback and Interactions: Consider providing feedback to the user about the uploaded photo. You can use image recognition algorithms or APIs to analyze the photo and provide relevant responses or recommendations based on the content of the photo.

----
General questions:
What is the skill in prompt generation?
You need people who are willing to do 60 percent of the work?

----


