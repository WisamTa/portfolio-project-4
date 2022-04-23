# Project Description
This project is developed as my 4th portfolio project during my course at Code Institute and I call it shareit.
shareit is a social media website, where users can register an account, login and create a user profile. users can upload posts with text and images on a feed for others to like and comment. users can follow other users and get along with them even in a private chat.

* [Project Description](https://github.com/WisamTa/portfolio-project-4#project-description)
* [UX](https://github.com/WisamTa/portfolio-project-4#ux)
  * [User Stories](https://github.com/WisamTa/portfolio-project-4#user-stories)
  * [Site Owner Goals](https://github.com/WisamTa/portfolio-project-4#site-owner-goals)
  * [Structure](https://github.com/WisamTa/portfolio-project-4#structure)
  * [Wireframes](https://github.com/WisamTa/portfolio-project-4#wireframes)
* [Features](https://github.com/WisamTa/portfolio-project-4#features)
  * [Data storage](https://github.com/WisamTa/portfolio-project-4#data-storage)
  * [Existing Features](https://github.com/WisamTa/portfolio-project-4#existing-features)
  * [Features Left To Implement](https://github.com/WisamTa/portfolio-project-4#features-left-to-implement)
* [Technologies Used](https://github.com/WisamTa/portfolio-project-4#technologies-used)
  * [Languages](https://github.com/WisamTa/portfolio-project-4#languages)
  * [Frameworks](https://github.com/WisamTa/portfolio-project-4#frameworks)
  * [Other Programmes](https://github.com/WisamTa/portfolio-project-4#other-programmes)
* [Testing](https://github.com/WisamTa/portfolio-project-4#testing)
  * [Manually test user storys](https://github.com/WisamTa/portfolio-project-4#manual-testing-by-user-storys)
  * [Validator Testing](https://github.com/WisamTa/portfolio-project-4#validator-testing)
  * [Bugs](https://github.com/WisamTa/portfolio-project-4#bugs)
* [Deployment](https://github.com/WisamTa/portfolio-project-4#deployment)
* [Credits](https://github.com/WisamTa/portfolio-project-4#credits)
* [Ackmowledgements](https://github.com/WisamTa/portfolio-project-4#acknowledgements)
# Content
# UX
## User Stories
### EPIC 1 
* As a user, I can easily and safely register an account so that I can use my account for the website's purpose
* As a user, I can use my email or username so that I can login into my account
* As a user, I can easily navigate through the site from anywhere I am on the site so that makes it easier to use and do what I suppose to

### Epic 2 
* As a user, I can Add and change my profile image so that Other users can see who I am.
* As a user, I can Add information to my biography about myself so that other users get to know me better through a personalized profile page.
* As a user, I can save all my posts on my page so that it is easy to view what I uploaded and to see what other users have shared on their profiles.
* As a user, I can Edit my profile page, add/edit and delete pictures and information so that I can control what to share, and make my profile more flexible.
* As a user, I can comment/edit on a user post so that I can give feedback or discuss what users upload and delete if I want to remove it.
* As a user, I can choose to upload something from the homepage or from anywhere I am on the site so that I don't have to go back or forward to do that task.

### Epic 3 
* As a user, I can search after other users by usernames, names, locations so that I can find other users in my location or find a user that I want to check out their profile page.
* As a user, I can add a friend to a friend list or a follow list so that I can see what this person uploads easy and get in touch.
* As a user, I can unfollow or unfriend a user so that I can regret it or if I follow by mistake can undo it.

### Epic 4
* As a user, I can Send a private message to another user so that Its easy to start a conversation and speak to other users one by one.
* As a user, I can get private messages from other users in an inbox so that I can sort and see where my messages go and save.
* As a user, I can Delete messages from my inbox so that I can easily clear my inbox and delete those who I don't want to save.

[Back to top](https://github.com/WisamTa/portfolio-project-4#project-description)

## Site owner goals
* As a site owner my goals is to create a website that is easy to understand and to seem interesting to know more about.
* Follows adapted structure and using eye catching colours and fonts though the site.
* Have features that users want to use and meet the ux from similar sites that users is comfortable with.
* Have a site that works propely without many errors. 

## Structure
* Landing page.
  * Start page for un authentical users Showing some information of what the site is about, have an about us file and a login and register form.  
![](https://github.com/WisamTa/portfolio-project-4/blob/main/media/imagesReamde/landingpage.PNG)  
  * Sign in, which is a form that will lead to exploring the app and using it 
![](https://github.com/WisamTa/portfolio-project-4/blob/main/media/imagesReamde/signin.PNG)
![](https://github.com/WisamTa/portfolio-project-4/blob/main/media/imagesReamde/start-menu.PNG)
  
* Landingpage for logged in users
  * Feed, when the user signs up, they are provided some information on how to upload, create more info on the profile page. This text will disappare when users upload their first post or start following users who have uploaded posts earlier.  
* Profile page
  * Personal page for the user, with fields of information to add about themself
  * Add profile image and edit profile.
  * See how many followers (moon friends) they have and a button to follow or unfollow other users.
  * Uploaded posts that the user have is collected on their own pages.
  ![](https://github.com/WisamTa/portfolio-project-4/blob/main/media/imagesReamde/editprofile.PNG)
    
* Inbox
  * An inbox that gathers all active threads
  * Start a new chat and search for a user to start chatting with
  * The conversation/chat with send and received messages.
  ![](https://github.com/WisamTa/portfolio-project-4/blob/main/media/imagesReamde/inboxpic.PNG)
  ![](https://github.com/WisamTa/portfolio-project-4/blob/main/media/imagesReamde/searchforcaht.PNG)
  ![](https://github.com/WisamTa/portfolio-project-4/blob/main/media/imagesReamde/conversation.PNG)
  ![](https://github.com/WisamTa/portfolio-project-4/blob/main/media/imagesReamde/inbox.PNG)
* Search
  * search input box on its own template, from the navbar.
  * shows all users that include the search query.
  ![](https://github.com/WisamTa/portfolio-project-4/blob/main/media/imagesReamde/searchuser.PNG)
* Upload
  * From navbar users can upload a post/image that uploads in the feed (and profile page)
    ![](https://github.com/WisamTa/portfolio-project-4/blob/main/media/imagesReamde/upload.PNG)
* post detail
  * When user want to comment or like, the user has to click on the post to get more details and show comments.
  * From post detail you can edit or delete your own posts and delete comments that user have made.  
* Footer
  * contains links to site owners social media  
    ![](https://github.com/WisamTa/portfolio-project-4/blob/main/media/imagesReamde/footer.PNG)

## Design Choises
### Fonts
### Colours
## Wireframes
# Features
## Data storage
### Post model
| Title      	| Key in Database   	| Form Validaton 	| Data Type       	|
|------------	|-------------------	|----------------	|-----------------	|
| body       	| body         	| max_length=500 	| TextField       	|
| created_on 	| created_on 	| None           	| DateTimeField    	|
| author     	| author              	| None           	| ForeignKey      	|
| upload     	| upload             	| image          	| CloudinaryField 	|
| likes      	| likes             	| None           	| ManytoManyField 	|
### Comment model
| Title      	| Key in Database   	| Form Validaton 	| Data Type     	|
|------------	|-------------------	|----------------	|---------------	|
| comment    	| comment           	| max_length=500 	| TextField     	|
| created_on 	| created_on 	| None           	| DateTimeField 	|
| author     	| author              	| None           	| ForeignKey    	|
| post       	| post              	| None           	| ForeignKey    	|
### Users (profile)
| Title     	| Key in Database   	| Form Validaton          	| Data Type       	|
|-----------	|-------------------	|-------------------------	|-----------------	|
| username      	| user 	| None                    	| OnetoOneField   	|
| name      	| name              	| max_length=50           	| CharField       	|
| profile picture   	| picture             	| None                    	| CloudinaryField 	|
| birthday  	| birthday          	| blank=True              	| DateField       	|
| gender    	| gender  	| default=Gender.other.id 	| IntegerField    	|
| location  	| location          	| max_length=100          	| CharField       	|
| bio       	| bio               	| max_length=500          	| TextField       	|
| followers 	| followers         	| User, blank=True        	| ManyToManyField 	|

## Existing features
* Create an account
  - Using Register from navigationbar
* Login as existing user
  - Login from navbar in the start page
* Add information on an profile page
  - When logged in, you can add profile page and more information
* Upload texts and images saved on the profile page
  - users can upload posts that automatic save in  profile page and upload in the feed.
* Share posts with other users 
  - Post that uploads shares with users that follows you.
* Follow or unfollow other users 
  - users can follow other by clicking on follow button in their profile page
* Edit profile page
  - users can edit your profile information and change profile image
* Like and comment other posts 
  - When click on the post, you get more information and can like and comment it from the detail view.
* Edit or delete posts
  - users can edit and delete your own posts in the detail view
* Delete comments
  - Comments that you have made can be deleted
* Send private messages to other users
  - You can message other existing users and receive message from other users.
* Delete threads from inbox
  - Threads that have been made in the inbox can be deleted
* search for other users by username
  - In the search part you can search for other users and the search field will show all users containing the letters you write.
* Visit other users profile pages
  - You can visit other user by their posts in the feed, comment section or search.
## Features left to implement
# Technologies used
## Languages
* HTML5
* CSS
* Javascript
* Python
## Frameworks
* Django
* Bootstrap
* Jquery
* PostgreSQL
## Other programmes
* [Heroku](https://id.heroku.com/login) - Deploy my site
* [Pep8](http://pep8online.com/) - Validate python code
* [Gitpod](https://gitpod.io/workspaces) -  Workspace 
* [GitHub](https://github.com/) -  Repository and save my user storys and code.
* [Balsamiq](https://balsamiq.com/) - Make my wireframes
* [Font Awsome](https://fontawesome.com/) - Got all the icons for the site
* [Google Fonts](https://fonts.google.com/) - Got my fonts
* [W3C Validator](https://jigsaw.w3.org/css-validator/validator.html.en) - Validate CSS and HTML
* [JShint](https://jshint.com/)
* [Markdown table generator](https://www.tablesgenerator.com/markdown_tables#) - Help with generate my tables for the readme
* [Color palett generator](https://coolors.co/) - Make my palette of colors
* Chrome Devtools - Fins issues, bugs and errors during the development on the liveserver.
* [Cloudinary](https://cloudinary.com/) - Store all the static images that users upload on the site.
* [Designhill](https://www.designhill.com/) - Paid Logo maker, from this website I generated my project/app logo.
# Testing
I have testing this project with manual testing. I have test i by myself during the development and once it was deployed.
## Manual testing by user storys
### EPIC 1
**Implementations**: As a user, I can easily and safely register an account so that I can use my account for the website's purpose.   
**Test**: I test this by first installing all auth, getting URLs done and the templates, I try to register and the account created, I use to receive signals for register users for saving them without errors in the database.  
**Result**: This test pass and works fine. 

---
**Implementations**: As a user I can use my email or username so that i can login with my account  
**Test**: Testing this by log in with the created account after logging out, using the chosen username when registerd. Not using Email for this site.
**Result**: This test pass and works how it should.

---
**Implementations**: As a user, I can easily find where to register and create an account so that I can be a member and join the community.    
**Test**: During the site, there are options on the landing page and about us page to register and log in and in the menu in the navbar.
**Result**: This test pass and works how it should. 

---
**Implementations**: As a user, I can easily navigate through the site from anywhere I am on the site, so that makes it easier to use and do what I suppose to.       
**Test**: Users have access to the navbar menu from anywhere they are on the site, with options to upload, go to inbox, go to home/feed or search, go to the profile page, or log out from the menu.   
**Result**: This test pass and works how it should.

---
### EPIC 2 Profile
**Implementations**: As a user, I can edit my profile page, add/edit and delete pictures and information so that I can control what to share and make my profile more flexible.      
**Test**: From the users' profile page, you can click on every post that I, as a user, have uploaded and, from there, delete or edit a post.    
**Result**: This test pass and works how it should. 

---
**Implementations**: As a user, I can Add and change my profile image so that Other users can see who I am.      
**Test**: From the profile page the user can edit its personal information and add and change a profile picture from the edit page.    
**Result**: This test pass and works how it should.   

---
**Implementations**: As a user, I can add information to my biography about myself so that other users get to know me better through my profile page.      
**Test**:  You can edit your personal information from the profile page to add a bio or edit/remove it.    
**Result**: This test pass and works how it should.   

---
**Implementations**: As a user, I can save all my posts on my page so that it is easy to view what I uploaded and see what other users have shared on their profiles.      
**Test**: When a user has uploaded a post, the post is shared on the feed and saved on the profile page automatically.    
**Result**: This test pass and works how it should.   

---
**Implementations**: As a user, I can choose to upload something from the homepage or from anywhere I am on the site so that I don't have to go back or forward to do that task.      
**Test**: In the navigation bar on the top, there is a link for upload, and you can click on it from anywhere on the site. And takes you to the uploading form, and when you submit and upload the post, you get to the feed    
**Result**: This test pass and works how it should.   

---
**Implementations**: As a user, I can like a photo from the feed so that the user who uploaded the post can see that I liked it.      
**Test**: You can like the photo by clicking on the post for the detail page, then selecting it, but there is no notification to see who has liked it.    
**Result**: This test does not pass because it doesn't do precisely as the implementations, but it has a similar function.

---
**Implementations**: As a user, I can comment/edit or delete a user's post so that I can give feedback or discuss what users upload and regret if I want to change or remove it.      
**Test**: As a user, you can comment on other users or your posts from the post detail page when you click on it. You can edit or delete your comments too.      
**Result**: This test pass.   

---
**Implementations**: As a user, I can edit or delete my uploaded posts so that I can change something in my already uploaded post or delete it if I regret uploading it.      
**Test**: As a user, I can click on my own post in the feed or from my profile page so that  I see it in the post detail view, and from there, I have an edit button and a delete button to make changes to my post or delete it completely.      
**Result**: This test pass.   

---
### EPIC 3 Search User
**Implementations**: As a user, I can search after other users by their usernames, names, and locations so that I can find other users in my area or find a user that I want to check out their profile page.      
**Test**: As a user, I can choose to click on search from the navbar and search after other users by their username only, and not location or name.      
**Result**: This test pass but it is not fully functional with all the search choices yet.   

---
**Implementations**: As a user, I can add a friend to a friend list or follow list so that I can see what this person uploads quickly and get in touch.      
**Test**: When I, as a user, visit other users' profile pages, I can choose to follow them by a button, and when I follow someone, I can see what that user uploads in my feed.      
**Result**: This test pass.   

---
**Implementations**: As a user, I can unfollow or unfriend a user so that I can regret it or, if I follow by mistake, can undo it.      
**Test**: From a user's profile page, you can choose to follow or unfollow by a button with no problem.      
**Result**: This test pass.   

---
### EPIC 4 Direct Messages
**Implementations**: As a user, I can Send a private message to another user so that It's easy to start a conversation and speak to other users one by one.      
**Test**: As a user, I can go to my inbox and search for a user I want to start to chat with and send messages to, or if I get a message, I can go to that thread from my inbox.      
**Result**: This test pass.   

---
**Implementations**: As a user, I can get private messages from other users in an inbox so that I can sort and see where my messages go and save.      
**Test**: All messages that have been created from different users are stored in threads in my inbox.      
**Result**: This test pass.   

---
**Implementations**: As a user, I can Delete messages from my inbox so that I  can clear my inbox and delete those that I don't want to save.      
**Test**: As a user, I can delete threads that I have in my inbox, and all the messages that have been sent to that user will be deleted for me.      
**Result**: This test pass. 

 ## Validator testing
### CSS
### Javascript
### HTML
### Python
## Bugs

# Deployment
When I started this project, I had to use Code Institutes template to be able to deploy it in Heroku and save all files that is secret in an gitignore file that came along the template. 
Then I used Gitpod IDE to bult this project and saved it with **git add**, **git commit** and then pushed it to github with the command **gitpush**. 
For saving code from django, I need to save it by the commands **python3 manage.py makemigrations** and then **python3 manage.py migrate** before I push the code to github and to finally deploy the project to Heroku. And the last step set the Debug to False in my app setting in django to get all the static files to show on the final deployment.

### Project deployment to Heroku
1. Log in to my account at Heroku
2. Select "new" and "Create new app" from the dashboard.
3. Create a unique name for the project
4. Navigate from the deploy tab at the top and select the setting tab.
5. Because I use Code Institute template, I need to add a config var for creating this app. (Not necessary if you do not use the template)
6. Select Reveal config vars button. In KEY field, input PORT with capital letters. In VALUE field, input 8000 and then select add button.
Select Python as yout first bulid pack in buildpacks window and save that.
9. Select the deploy tab again and go to the deployment method section.
10. Select GitHub - connect to GitHub button and follow the steps to connect to your GitHub account.
11. Select your account and enter the name of your repository and then select search.
12. When Heroku has find your repository select connect to connect the repository to the app within Heroku.
13. Below App connected section, I choose to manual deployments options further down.
14. When that is done correctly this will provide me the live link for this programe.
15. Then I choose Automatic Deploys button that will automatically rebuild the app everytime you add, commit and push from GitPod.

# Credits
* [Django Documentation](https://docs.djangoproject.com/en/4.0/) - I used alot of help to understand django and find solutions for my problems from the django documentation for this project!

* I also used very much help from the Django- I Think Therefore I Blog, walkthough project to start the project and fore some ideas how to do with the comments and likes and to start the project, helped me with the basic structure.

* [Receiver/signals](https://www.codeunderscored.com/signals-in-django/) - using receiver when create new users to not get errors.

* [This](https://www.youtube.com/watch?v=dIcCi2SG1CU) tutorial helped me with the search problem and how to implement ajax and jquery for it.

* [Help with how to upload all images and static](https://www.geeksforgeeks.org/python-uploading-images-in-django/)

* [Following system](https://itsvinayak.hashnode.dev/creating-a-follow-and-unfollow-system-in-django) - Using help from this tutorial how to manage the following system.

* [See followers post in feed](https://stackoverflow.com/questions/55675757/django-queryset-for-getting-feeds-from-following-users)

* [One tutorial for messages](https://www.youtube.com/watch?v=j1voZAmVw9I&t=648s)
[Another for private messages](https://www.youtube.com/watch?v=oxrQdZ5KqW0) - Using help from this two tutorials for making the private message function.

* All the images that i used is my own or users uploaded photos.
# Acknowledgements




