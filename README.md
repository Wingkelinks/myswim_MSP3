[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/organization/repository)

<h1 align="center">MySwim</h1>

![alt text](amiresponsive-img.png "Image generated from Am I Responsive")

[View the live project here.](https://my-swim.herokuapp.com/)

---

## Index

- <a href="#context">Context</a>
- <a href="#ux">UX</a>
  - <a href="#ux-overview">Overview</a>
  - <a href="#ux-stories">User stories</a>
  - <a href="#ux-wireframes">Wireframes</a>
  - <a href="#ux-design">Design</a>
- <a href="#database-model">Database Model</a>
- <a href="#features">Features</a>
  - <a href="#features-current">Existing</a>
  - <a href="#features-future">Desirable/Future</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>

---

<span id="context"></span>

Are you a swimmer looking for a convenient way to store and access your swim sets? If so, MySwim is made for you! Other than providing a secure place to store and access your swim sets, it also allows you to search for existing and new sets, that have been uploaded by fellow swimmers.

MySwim allows you to create a free account where you can add and save as many of your own swim sets, that are then shared with the MySwim community. You can save some of your favourite sets to your profile for convenient access. You can also print sets straight from the website.

<h2 align="center"><img src=""></h2>

--

<span id="ux-overview"></span>

## User Experience (UX)

MySwim is my third milestone project as a Code Institute student working towards a Diploma in Full Stack Software Development. It forms part of the Data Centric Development Module where the main aim is to "build a full-stack site that allows users to manage a common dataset about a particular domain."

As a swimmer, this site will provide personal value as a convenient means to store and access swimming programmes or sets. Having always relied on bits of soggy paper, stored here-and-there, the website will aim to alleviate this. It will also be beneficial to me as a swimmmer to have access to a collection of swimming sets, submitted by other swimmers, rather than constantly having to cycle through the same sets, or come up with new ones at the last minute.

<span id="ux-stories"></span>

- ### User stories

  - #### As a first time visitor, I want...

    1. To easily understand the main purpose of the site and learn more about what it offers.
    2. To see a large portion of the content without registering.
    3. To be able to search for swimming sets using appropriate keywords.
    4. A convenient registration process.

  - #### As a returning visitor, I want...

    1. A convenient login and logout process.
    2. To be able to search for swimming sets using appropriate keywords.
    3. To have access to a personal profile.
    4. To be able to save 'favourite' swimming sets created by other users under my profile.
    5. To be able to add new swimming sets.
    6. To be able to edit or delete swimming sets from my profile.

  - #### As the site owner/admin, I want...
    1. To manage categories (add, edit or delete).
    2. To be able to edit or remove content submitted by users.

<span id="ux-design"></span>

- ### Design
  - #### Colour Scheme
    -
  - #### Typography
    -
  - #### Imagery
    -

<span id="ux-wireframes"></span>

- ### Wireframes

  - Wireframes can be viewed [here]()

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

<span id="database-model"></span>

## Database Model

## Features

<!-- - Responsive on all device sizes

- Interactive elements -->

--
<span id="technologies"></span>

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

### Frameworks and Libraries

- [Materialize](https://materializecss.com/)
- [Google Fonts:](https://fonts.google.com/)
- [Font Awesome:](https://fontawesome.com/)
- [jQuery:](https://jquery.com/)
- [Icons8](https://icons8.com/) - for custom icons used on map.
- [CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/): used to create responsive layouts.
- [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/): used to create responsive layouts.

### Extensions and kits

- [Flask Paginate](https://pythonhosted.org/Flask-paginate/)
- [Werkzeug](https://palletsprojects.com/p/werkzeug/)

### Project Management

- [Git](https://git-scm.com/)
- [GitHub:](https://github.com/)
- [MongoDB](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/about)
- [Balsamiq:](https://balsamiq.com/)
  - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.

--
<span id="testing"></span>

## Testing

Full testing details can be found [here](TESTING.md)

--
<span id="deployment"></span>

## Deployment

The deployed version has been created using the master branch.

### Prerequisites

[Python 3](https://www.python.org/downloads/) - core code

[PIP](https://pypi.org/project/pip/) - package installation

[Git](https://git-scm.com/) - version control

[MongoDB](https://www.mongodb.com/)

- MongoDB is the database used by the app to store content uploaded by its users.
- The following collections should be created:
  - sets
  - categories
  - users
- A document in categories should be created with the following fields:

| **Key**       | **Value** | **Type** |
| :------------ | :-------- | :------- |
| category_name | aerobic   | String   |

### How to clone MySwim

To clone this project from its [GitHub repository]():

### How to deploy to Heroku

To deploy the app to Heroku from its [GitHub repository](), the following steps were taken:

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

### Forking the GitHub Repository

### Making a Local Clone

--
<span id="credits"></span>

## Credits

### Tutorials / Resources

- Code Institute Task Manager Project ([Tim Nelson](https://github.com/TravelTimN))
- MS3 Strategy and Tips ([Ed Bradley](https://github.com/Edb83))
- [Code Institute course material](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment)
- Code Institute **Slack** channel
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) - Guide to markdown on .md files.
- [CSS Tricks](https://css-tricks.com/) - convenient CSS resources. Regularly referenced their **Flexbox** tutorial.
- [Stack Overflow](https://stackoverflow.com/) - general questions and problem solving.
- [MDN Web Docs](https://developer.mozilla.org/en-US/) - general questions and problem solving.

### Code

-

### Content

- All content was written by the developer.

### Media

-

### Acknowledgements

- Thanks to my Mentor, Sebastian Immel...

- Thank you to the Code Institue Slack community - a great place to check in and learn from others.

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

