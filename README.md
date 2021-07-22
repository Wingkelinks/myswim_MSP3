[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/organization/repository)

<h1 align="center">MySwim</h1>

###### Code Institute MS3 / Data-Centric Development

<img src="static/images/test_images/amiresponsive-img.png" width="800">

[View the live project here.](https://my-swim.herokuapp.com/)

---

## INDEX

- <a href="#context">Context</a>
  - <a href="#ux-overview">Project Overview/Strategy</a>
  - <a href="#ux">User Experience</a>
  - <a href="#ux-strategy">Strategy</a>
  - <a href="#ux-scope">Scope</a>
  - <a href="#ux-structure">Structure</a>
- <a href="#skeleton">Skeleton</a>
- <a href="#surface">Surface</a>
  - <a href="#features-existing">Existing Features</a>
  - <a href="#features-future">Desirable Features</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Development and Deployment</a>
- <a href="#credits">Credits</a>

---
># **CONTEXT**

<span id="context"></span>

Are you a swimmer looking for a convenient way to store and access your swim sets? If so, MySwim is made for you! Other than providing a secure place to store and access your swim sets, it also allows you to search for existing and new sets, that have been uploaded by fellow swimmers.

MySwim allows you to create a free account where you can add and save as many of your own swim sets, that are then shared with the MySwim community. You can save some of your favourite sets to your profile for convenient access. You can also print sets straight from the website.

<span id="ux-overview"></span>
<span id="ux"></span>

># **PROJECT OVERVIEW/STRATEGY** 

## USER EXPERIENCE (UX)

MySwim is my third milestone project as a Code Institute student working towards a Diploma in Full Stack Software Development. It forms part of the Data Centric Development Module where the main aim is to "build a full-stack site that allows users to manage a common dataset about a particular domain."

As a swimmer, this site will provide personal value as a convenient means to store and access swimming programmes or sets. Having always relied on bits of soggy paper, stored here-and-there, the website will aim to alleviate this. It will also be beneficial to me as a swimmmer to have access to a collection of swimming sets, submitted by other swimmers, rather than constantly having to cycle through the same sets, or come up with new ones at the last minute.

># **STRUCTURE**

<span id="ux"></span>

- ## USER STORIES

  - #### As a first time visitor, I want...

    1. To easily understand the main purpose of the site and learn more about what it offers.
    2. Access to easy and clear navigation.
    3. To experience a responsive site.
    4. To experience appealing visuals and design.
    4. To experience intuitive UX Design.
    5. A convenient and secure registration process.
  
  - #### As a returning visitor, I want...

    1. A convenient login and logout process.
    2. To be able to search for swimming sets using appropriate keywords.
    3. To have access to a personal profile.
    4. To be able to save 'favourite' swimming sets created by other users under my profile.
    5. To be able to add new swimming sets.
    6. To be able to edit or delete swimming sets from my profile.
    7. To be able to print out a selected set. 

  - #### As the site owner/admin, I want...
    1. To manage categories (add, edit or delete).
    2. To be able to edit or remove content submitted by users.

># **SCOPE**

**Minimum Viable Product** for the website will include:

- responsive navigation on all pages
- home page - featuring a hero image and call to action
- about section - offering information about the site's purpose
- error pages - in the event of 404 or 500 errors occuring
- print page - gives users access to print friendly version of a set

**C.R.U.D Principle** to be met by incorporating the following functionality within respective pages:

- Register (CREATE user instance in database)
- Log In/Log Out
- Search Sets (READ and RETRIEVE records in database)
- Profile Page (READ records in database)
- Add New Set & Add Favourite to Profile (UPDATE and add to data)
- Manage Content for Admin:
      - Add Category/Set (UPDATE records)
      - Edit Category/Set (UPDATE records)
      - Delete Category/Set (DELETE records)
- Edit a Set (UPDATE existing data)
- Delete a Set (DELETE to remove records from database)

># **SKELETON**

## WIREFRAMES
<span id="ux-skeleton"></span>

- Wireframes can be viewed [here](https://github.com/Wingkelinks/myswim_MSP3/blob/master/wireframes/myswim_wireframes.pdf)

## SITE MAP

- A site map can be viewed [here](https://github.com/Wingkelinks/myswim_MSP3/blob/master/wireframes/site_map.pdf)

># **SURFACE**
<span id="ux-surface"></span>

## DESIGN

  - #### Theme and Colour Scheme

  The theme is inspired by swimming and is intended to appeal to all types of swimmers. A clean and modern colour scheme with contrasting and complementary colours was chosen to reflect a sense of simple energy. [Coolors](https://coolors.co/) was used to generate two colour palettes which were incorporated as utility classes in the CSS file, to be easily called upon directly from the HTML files. 

  Take a closer look at the colour schemes:

  <img src="static/images/test_images/color-scheme2.png" width="400">
  <img src="static/images/test_images/color-scheme1.png" width="400">

  - [MySwim Color Scheme 1](https://coolors.co/ffbe0b-fb5607-ff006e-8338ec-3a86ff-4dec38-000000)
  - [MySwim Color Scheme 2](https://coolors.co/ffbe0b-fb5607-ff006e-8338ec-3a86ff-4c91ff-5c9bff-6ba4ff-78acff-84b4ff)


  - #### Typography
  
  ##### [Google Fonts](https://fonts.google.com/)

  - [Tourney Text](https://fonts.google.com/specimen/Tourney) was selected for the MySwim logo in the Navbar and makes an appearance in selected headings and messages throughout the site. 
  I chose it for it's 'sporty, techy' vibe (to quote Google Fonts).
    
  - [Roboto](https://fonts.google.com/specimen/Roboto) was chosen for the body of the site. It has a modern and open appeal and pairs nicely with Tourney Text.
    
  - #### Imagery

    - Appropriate images related to swimming were selected for the site. 
    - Images are all obtained from [Unsplash](https://unsplash.com/) and are free to use. 

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

## DATABASE MODEL

#### Sets Collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|category_name|string| Category Name |
|set_name|string| Set Name |
|warm_up|string| Warm up instructions |
|pre_set|array| Array allows for dynamically added fields using JQuery script |
|main_set|array| Array allows for dynamically added fields using JQuery script |
|cool_down|string| Cool down instructions |
|total_km|string| Set Distance |
|created_by|string| Created when a session user submits a new set|


#### Categories Collection

|**Key**|**Type**|**Description**|
|:-----|:-----|:-----|
|_id|ObjectId||
|category_name|string| Category Name provided by Admin |

#### Users Collection

|**Key**|**Type**|**Description**|
|:-----|:-----|:-----|
|_id|ObjectId||
|username|string| User's username |
|password|string| Password gets hashed when user creates an account |

#### Favourites Collection

|**Key**|**Type**|**Description**|
|:-----|:-----|:-----|
|_id|ObjectId| Created when a user saves a set as a favourite |
|set_id|string| Associated set id |
|set_name|string| Associated set name |
|user|string| User id |

># **FEATURES**

## EXISTING 

- **Register Account**
- **Log In to Account**
- **Log Out of Account**
- **View Swim Sets**
- **Search Sets**
- **Add a Set**
- **Edit a Set**
- **Delete a Set**
- **Add a Set to Favourites**
- **Print a Set** 

In addition to the above, the *admin* user has the following features available:
- **Add a Category**
- **Edit a Category**
- **Delete a Category**
- **Edit any Set**
- **Delete any Set**

*Defensive Programming* Features include **Deletion Confirmation** alerts that appear as a modal, when a user clicks on any 'delete' related button. 

## DESIRABLE

- **Pagination**: 
  I would have loved to have included pagination to the site, as I am fully aware that it contributes to a better user experience. Due to time constraints, it was necessary to prioritise other elements/features. 

- **Remove Set from Favourites**: 
  Again, this is an important companion feature to the 'Add Favourites' feature, however I did not have the time to make it work. 

---
<span id="technologies"></span>

># **TECHNOLOGIES USED**

## LANGUAGES

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

## FRAMEWORKS AND LIBRARIES

- [Materialize](https://materializecss.com/)
- [Tachyons](https://tachyons.io/)
- [Google Fonts](https://fonts.google.com/)
- [Material Icons by Google Fonts](https://fonts.google.com/icons)
- [Font Awesome](https://fontawesome.com/)
- [jQuery](https://jquery.com/)
- [CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

## EXTENSIONS AND PACKAGES

- [PIP](https://pypi.org/project/pip/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Jinja Templating Engine](https://jinja.palletsprojects.com/en/3.0.x/)
- [Werkzeug](https://palletsprojects.com/p/werkzeug/)
- [PyMongo](https://pypi.org/project/pymongo/)

## PROJECT MANAGEMENT

- [Visual Studio Code](https://code.visualstudio.com/) - Coding Editor
- [Git](https://git-scm.com/) - Version Control
- [GitHub](https://github.com/) - Repository Storage
- [Imgbot](https://github.com/marketplace/imgbot) 
    - A Github app that optimizes images (free    for open source projects).
    > Imgbot sends an auto pull request with images optimized. The pull request is merged and Imgbot keeps working as changes are made to the repository.
- [MongoDB](https://www.mongodb.com/) - Database Management
- [Heroku](https://www.heroku.com/about) - App Hosting 
- [Balsamiq](https://balsamiq.com/) - Wireframes, Site Map
 
---
<span id="testing"></span>

># **TESTING**

Full testing details can be found [here](TESTING.md)

--- 
<span id="deployment"></span>

># **DEVELOPMEMNT AND DEPLOYMENT**

The deployed version of MySwim has been created using the master branch.

## LOCAL DEPLOYMENT 

The following is required to run this project in your local environment:

[Python 3](https://www.python.org/downloads/) - to run the code

[PIP](https://pypi.org/project/pip/) - for package installation

[Git](https://git-scm.com/) - used for version control

[MongoDB or MongoDB Atlas](https://www.mongodb.com/) - for database development 

[Visual Studio Code](https://code.visualstudio.com/) - or your own choice of IDE 

### First you need to clone MySwim

To clone this project from its [GitHub repository](https://github.com/Wingkelinks/myswim_MSP3):

1. Click on the **Code** button 
2. Copy the clone URL for the repository: https://github.com/Wingkelinks/myswim_MSP3.git
3. From within your IDE, open your integrated terminal
4. Make sure you are in the correct folder location 
5. Then type **git clone** and paste the URL: https://github.com/Wingkelinks/myswim_MSP3.git
6. From there create an env.py file to store your credentials as follows:

```console 
      import os

      os.environ.setdefault("IP", "0.0.0.0")
      os.environ.setdefault("PORT", "5000") 
      os.environ.setdefault("SECRET_KEY", "") 
      os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ofgqg.mongodb.net/<database_name>?retryWrites=true&w=majority") 
      os.environ.setdefault("MONGO_DBNAME", "my_swim")
```

You can use a random key generator if you wish. 

7. This file MUST be hidden in your .gitignore file to keep credentials from being visibly pushed to the repository
8. You should be able to run the app by typing **python3 app.py** into the terminal

- In MongoDB you will need to create a database called MySwim.
- The following collections should be created:
  - sets
  - categories
  - users
- A document in categories should be created with the following fields:

| **Key**       | **Value** | **Type** |
| :------------ | :-------- | :------- |
| category_name | aerobic   | String   |

- The same applies for sets and users, however the sets collection has two fields of arrays:

| **Key**       | **Value** | **Type** |
| :------------ | :-------- | :------- |
| pre_set       | []        | Array    |
| main_set      | []        | Array    |


### How to deploy to Heroku

MySwim is deployed on Heroku from the master branch. To do this, the following steps were taken:

1. From your terminal, create a **requirements.txt** and **Procfile** using these commands:

```console
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

2. Sign up and login to Heroku, **create a new app**
3. Name your app
3. Go to the **Deploy** tab and then **Deployment Method** and select **Github**
4. Under **Connect to Github** enter your details and connect your repository 
5. Next, go to **settings** and select **Config Vars** and then **Reveal Config Vars**
6. You need to enter the following variables to match what you have stored in your env.py file
    
    - **IP** : `0.0.0.0`
    - **PORT** : `5000`
    - **MONGO_URI** : `MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ofgqg. mongodb.net/<database_name>?retryWrites=true&w=majority`
    - **SECRET_KEY** : `<app secret key>`

7. Under the **Deploy** tab go to **Automatic Deploys** and enable 
8. Under **Manual Deploy**, choose **Master** and click **Deploy Branch**
9. Heroku will begin building the app. When it is ready, you can click **Open app** to launch it.  

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

--
<span id="credits"></span>

># **CREDITS**

## TUTORIALS AND RESOURCES

- Code Institute Task Manager Project ([Tim Nelson](https://github.com/TravelTimN))
- MS3 Strategy and Tips ([Ed Bradley](https://github.com/Edb83))
- Fellow Students MS3 Project ([Ed Bradley](https://github.com/Edb83))
- [Code Institute course material](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment)
- Code Institute **Slack** channel
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) - Guide to markdown on .md files.
- [CSS Tricks](https://css-tricks.com/) - convenient CSS resources. Regularly referenced their **Flexbox** tutorial.
- [Stack Overflow](https://stackoverflow.com/) - general questions and problem solving.
- [MDN Web Docs](https://developer.mozilla.org/en-US/) - general questions and problem solving.

## REFERENCED AND MODIFIED CODE SOURCES

- [CSS3 Animation Notification](https://codepen.io/sugimo/pen/DgLty) - referenced to create custom flash messages
- [Print Page JQuery](https://www.geeksforgeeks.org/how-to-print-a-page-using-jquery/) - to initialise my print functionality
- [Tutorial by Cody Mind](https://www.youtube.com/watch?v=jSSRMC0F6u8) - dynamically add and delete form input fields
- [Dogfalo](https://github.com/Dogfalo/materialize/issues/192) - to customise the Materialize form input fields 

## CONTENT AND MEDIA

- All initial site content is written by the developer. 
- Images obtained from [Unsplash](https://unsplash.com/), an open source photography platform. 

## ACKNOWLEDGEMENTS 

- Thanks to my Mentor, Sebastian Immel for his guidance and support.
- Thank you to Ed Bradley, for his MS3 Tips and Strategies video.
- Thank you to the Code Institute and the top quality course content.
- Thank you to the Code Institue Slack community - a great place to check in and learn from others.

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

