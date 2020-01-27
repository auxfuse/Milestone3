# Milestone Project 3
***

## Table of Contents:
* [What does it do and what does it need to fulfill?](#what-does-it-do-and-what-does-it-need-to-fulfill)
* [Functionality of Project](#functionality-of-project)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Design](#design)
        * [1. Font](#1-font)
        * [2. Color Scheme](#2-color-scheme)
        * [3. Logo](#3-logo)
        * [4. Geometry](#4-geometry)
        * [5. Wireframing](#5-wireframing)
* [Technology Used](#technology-used)
* [Features](#features)
    * [Future Features](#future-features)
* [Testing](#testing)
    * [Defensive Design](#defensive-design)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Special Thanks & Acknowledgements](#special-thanks--acknowledgements)

***

## Welcome to Oly-Track!

<p align="center">
    <img src="https://github.com/auxfuse/Milestone3/blob/master/static/images/oly-track-large-logo.png" alt="Oly-Track Logo">
</p>

***

## What does it do and what does it need to fulfill?
This Milestone project creation is the culmination of learning and study from the eight, ninth and tenth modules of the Full Stack Developer Course, Python Fundamentals, Practical Python and Data Centric Development, to create a fully Mobile Responsive CRUD Web Application. This Application will allow a user to create, read, update and delete Olympic Weightlifting Sessions and is called "Oly-Track".

<p align="center">
    <img src="https://github.com/auxfuse/Milestone3/blob/master/static/images/oly-track-short-logo.png" alt="Oly-Track Favicon">
</p>

### Functionality of Project
This application contains the key CRUD requirement functionality and utilises a data handling document based database, MongoDB. The user functionality is created using Flask, HTML templates and CSS. One of the most prominent frontend frameworks was used in building the frontend interface structure, Bootstrap, and includes all the main attributable points of a modern day website/application such as a Navigation bar and Footer elements.

The application also utilises a Registration and Login system to show clear seperation between documents created by each Registered user. These functions utilise creating and reading to the database along with password hashing to protect each individuals credentials. The project also caters for un-registered users as there is functionality for documents created by a registered user to set them public to be displayed in the application without a Login, aswell as a _Fundamentals_ page to assist the user in learning the technical aspects of the subject matter, Olympic Weightlifting. 

The project is version controlled via Git & Github and is deployed via Heroku. All environment variables are held in a git ignored file and held _secret_ to ensure the project integrity is held to present day and project requirement standards.

[Back to top](#table-of-contents)

## User Experience:

#### User Stories:
_Generic (Guest/Public) User:_
* As a Generic User, I want to view the basics of Olympic Weightlifting to be equipped with the knowledge before my sessions.
* As a Generic User, I want to have the ability to view pre-made (public) Olympic Weightlifting sessions.
* As a Generic User, I want to be met with a visually appealing and easy to read layout of created sessions.
* As a Generic User, I want to be able to register/sign-up to create and track my own sessions.
* As a Generic User, I want to be able to contact someone in the event something is wrong with the app.

_Registers (Logged in) User:_
* As a Registered User, I want to view the basics of Olympic Weightlifting to be equipped with the knowledge before my sessions.
* As a Registered User, I want to have the ability to view pre-made Olympic Weightlifting sessions, both public and my own.
* As a Registered User, I want to have the ability to log in and view my list of Weightlifting sessions.
* As a Registered User, I want to be able to create and record my training sessions as I'm training.
* As a Registered User, I want to be able to delete existing training sessions as I see fit.
* As a Registered User, I want to be able to log out of my account.
* As a Registered User, I want to have a method of contacting someone in the event something is not functioning as expected in the application.

_Developer:_
* As a Developer, I want to expand my knowledge with Python and Flask by creating an extensive management database application.
* As a Developer, I want to create a fully-responsive mobile-friendly multi-language faceted project to showcase what I have learned whilst on this course.
* As a Developer, I want a project which can evolve as I grow as a developer.
* As a Developer, I want to be able to use the app for myself in my Olympic Weightlifting sessions.

#### Design

##### 1. Font
The project has a main font of <a href="https://fonts.google.com/specimen/Maven+Pro">Maven Pro</a> and a secondary font of <a href="https://fonts.google.com/specimen/Roboto">Roboto</a> which greatly complement each other throughout the site.
  
“Sans-Serif” is used as the default backup font in cases where these fonts have difficulty loading.
Maven Pro sports a unique curvature allowing it the ability to stand out and be distinguishable when in context. It is used throughout the site as the main font for headers, unique stand-out pieces of information and button text etc, drawing the user’s attention to these main focus points and calls to actions.

The secondary font used is Roboto. With its natural widths per character, and increased effectiveness for reading rhythm, it was the perfect choice using this font for the lengthier text elements. Used on all major paragraphs, it offers a pleasing reading ability to the user and is easy on the eyes. This font is a staple used in many websites and applications today worldwide and is reminiscent of how an application should look, clean, professional and very readable amongst all major languages.

##### 2. Color Scheme
This project went through multiple theme iterations whilst in Wireframe stage. Ultimately, I was always lead back to professional high contrast finish that would normally be seen in most day-to-day apps with a touch of pastel color to highlight to the user the breakaway elements.

* ![#000000](https://placehold.it/15/000000/000000?text=+) `#000000` - Primary color
* ![#aae1db](https://placehold.it/15/aae1db/000000?text=+) `#aae1db` - Secondary color
* ![#545479](https://placehold.it/15/545479/000000?text=+) `#545479` - Tertiary color
* ![#323232](https://placehold.it/15/323232/000000?text=+) `#323232` - Supplementary color #1
* ![#84afa6](https://placehold.it/15/84afa6/000000?text=+) `#84afa6` - Supplementary color #2

The logo was created with a clean black color, ![#000000](https://placehold.it/15/000000/000000?text=+) , setting the immediate tone for the rest of the application to be professional and aesthetically pleasing. All fonts used throughout the application utilise this primary color as-well.

The navbar is colored in our Secondary color choice, ![#aae1db](https://placehold.it/15/aae1db/000000?text=+) , which offered the first splash of vibrant color to contrast the logo and the nav-link elements of black. I screened this against several people and all came back commenting the contrast was fine on their preferred device.

The call to action buttons utilised the same navbar coloring of, ![#aae1db](https://placehold.it/15/aae1db/000000?text=+) , when not active, focused or hovered. When an action was captured on the button, it would turn a slightly darker hue (our supplementary color #2), ![#84afa6](https://placehold.it/15/84afa6/000000?text=+) , to show the user that this element is interact-able and something can happen when pressed.

The tertiary color, ![#545479](https://placehold.it/15/545479/000000?text=+) , was used as a subtle dark-tone to break up the solid abruptness of the black. Throughout the site you can see this is used sparingly to create some dividers and the outlines of the call to action buttons, aswell as create the hover effect on the social iconography in the Footer.

Supplementary color #1, ![#323232](https://placehold.it/15/323232/000000?text=+) , is used as a background color to break up long page, such as the Home page, for the user to distinguish between sections. 

##### 3. Logo
The logo was custom created by myself in photoshop. It incorporates straight leading lines and symmetrical shaping to reinforce the idea and importance of form in Olympic Weightlifting. In conjunction with the above, a vector of a barbell was used to extend and further delineate from a generic logo allowing the user to know at a glance that the application was intended for use with sport in general.

The centre of the logo comprises of a deconstructed hexagon which would be similar in shape and form to a hex-bar used often by Olympic/Power Lifters in accessory style sessions. It was a natural offset to the straight and narrow leading edges of the barbell and gave it a solid sturdy approach, again reinforcing the natural attribute of the sport, strength in a solid base.

<p align="center">
    <img src="https://github.com/auxfuse/Milestone3/blob/master/static/images/oly-track-large-logo.png" alt="Oly-Track Logo">
</p>

##### 4. Geometry

The application is primarily rectangular shaped with subtle rounded edges around elements such as cards, forms and interactive buttons to create a nice flow for the user that doesn't distract. Where possible a quasi-method of rule of thirds was followed for pages and their nested elements. An example of this would be the Home page:
* The main body of the page is vertically separated into thirds, we have a landing image, an about section detailing the functionality and use of the application, and finally we have a Home actions set of cards, acting as a descriptive point of focus for our user to understand where each avenue will take them.
* Following from this, the about section is also split in vertical thirds. With a header, descriptive narrative as described above, and closing with the Branding logo of the site.
* The Descriptive Card Navigation set is split horizontally in thirds, with each third allocated to an associated Card, and on mobile is split vertically due to the cascading column view by the Bootstrap col- size declaration in the code.

This is reciprocated throughout the site to ensure that User isn't overloaded with information and in a hope that the user scans and takes in as much as is humanly possible to follow in line with the rule of thirds methodology.

##### 5. Wireframing

Wireframing for this project began with Pen and paper as all my projects tend to start, but ultimately Wireframes were created using Balsamiq. Each page or view of the application was rendered as a wireframe in both Small and Medium-Large viewports to show the difference between the aesthetics and showing how the elements per page would react to differing viewport sizes. Each element planned out in this stage has made it into the physical build of the application with not much deviation occurring from the original wireframe plans.

* Base Template:

The base.html parent template contained all the default components for each page. A head element containing meta characteristics and all relevant links to Title, Frameworks, and custom CSS files for the application. A navbar containing the branding and the associated navigation set whether logged in or otherwise. A main section in the body for content control flow in the form of jinja templating's special delimiters is used to define the block that our child templates can override;
```html
{% block content %}
{& endblock %}
```

And finally our footer and associated components inside same. These wireframes are very basic but are included to show the default parent template, (skeleton), that each child template inherites from.

<details>
<summary>Base Template Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Mobile-Template.png" alt="Base template mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Tablet-Desktop-Template.png" alt="Base template tablet-desktop wireframe">
</p>
</details>

***

* Home Page:

The Home (Index) Page contained all the major navigation points for both a logged-in or non logged-in user. It contained a hero image to portray the theme and defining nature of the application aswell as a brief description surrounding the app and it's cause for creation which was added post Wireframe creation.

<details>
<summary>Home Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Mobile-Home.png" alt="Home page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Tablet-Desktop-Home.png" alt="Home page tablet-desktop wireframe">
</p>
</details>

***

* Fundamentals Page:

The Fundamentals page was the first page in the application to get and display a collection of data pre-populated in MongoDB. Utilising the cards component in Bootstrap, each card would display a Gif of the movement, title, description and movement cues. These assist in helping the User to get familiar with not only the names of the movement but how the movements should be acted out. It also acts as a key method in demonstrating one of the core components of the project, `Read`.

<details>
<summary>Fundamentals Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Mobile-Fundamentals.png" alt="Fundamental page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Tablet-Desktop-Fundamentals.png" alt="Fundamental page tablet-desktop wireframe">
</p>
</details>

***

* Public Sessions Page:

This page in the application is to show those records created by logged in users which have been set to the "Public" option, allowing those not logged in to see the session as a Read action only. 

<details>
<summary>Public Sessions Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Mobile-PublicSessions.png" alt="Public Sessions page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Tablet-Desktop-PublicSessions.png" alt="Public Sessions page tablet-desktop wireframe">
</p>
</details>

***

* Login Page:

A simple page as normal inheriting the navbar and footer from the base.html file, but containing a small form group to capture and validate the user's username and password. This page will also feature a small hyperlink so the user can register their details to login to the application.

<details>
<summary>Login Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Mobile-Login.png" alt="Login page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Tablet-Desktop-Login.png" alt="Login page tablet-desktop wireframe">
</p>
</details>

***

* Registration Page:

As with the Login page, this page is very similar with the only changes being that of language/terminology of some of the text pieces and the removal of the Register link.

<details>
<summary>Registration Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Mobile-Register.png" alt="Register page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Tablet-Desktop-Register.png" alt="Register page tablet-desktop wireframe">
</p>
</details>

***

* Create Session Page:

Navigation to this page is locked behind login. Once logged it will appear in the nav-items in the navbar. Form elements such as date selectors, dropdowns featuring collections of data to select from, and fields make up the main composition of this portion of the application. This is the `create` section for the application in keeping with the main requirement for this project. 

<details>
<summary>Create Session Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Mobile-CreateSession.png" alt="Create Session page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Tablet-Desktop-CreateSession.png" alt="Create Session page tablet-desktop wireframe">
</p>
</details>

***

* My Sessions Page:

A filtered list per User, with navigation to this locked behind login. Each record on this list will show a top level set of information on tablet-desktop, with a little bit less on mobile to save vital visual real-estate. A button per record to navigate the user to the Session page to view all the details of the session.

<details>
<summary>My Sessions Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Mobile-MySessions.png" alt="My Sessions page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Tablet-Desktop-MySessions.png" alt="My Sessions page tablet-desktop wireframe">
</p>
</details>

***

* Session View Page:

This page is to detail to the user a full view of the Session to the user and navigation to this is locked behind login. Two buttons exist on this page to act as two major call-to-actions for the record. One to navigate the user to the Edit Sessions page. And the other button acts as the only Delete functionality in the application, fulfilling the `delete` portion of the CRUD functionality for the project.

<details>
<summary>Session View Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Mobile-SessionView.png" alt="Session View page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Tablet-Desktop-SessionView.png" alt="Session View page tablet-desktop wireframe">
</p>
</details>

***

* Edit Session Page:

Navigation to this page can only be instantiated by the user once they view there own session. This layout provides the `update` portion of the CRUD functionality for which the projects main requirements are set for. All fields are editable by the user, with a button to update the session. Once updated, the user will be redirected back to their appropriate `My Sessions` page.

<details>
<summary>Edit Session Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Mobile-EditSession.png" alt="Edit Session page mobile wireframe">
</p>

<p align="center">
<img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/wireframes/Ms3-Tablet-Desktop-EditSession.png" alt="Edit Session page tablet-desktop wireframe">
</p>
</details>

***

[Back to Top](#table-of-contents)

## Technology Used

#### Languages, Frameworks, Editors & Version Control:

* HTML, CSS & Python ~ core languages used to create this multi-page CRUD application.
* <a href="https://getbootstrap.com/"> Bootstrap Framework</a> ~ Used as the core structuring layout for the application, ensuring mobile-first design and screen size fluidity.
* Bootstrap's <a href="https://getbootstrap.com/docs/4.3/getting-started/introduction/#js">Imported Javascript & JQuery</a> ~ For the Modal and Responsive Navbar expand & collapse functionality.
* <a href="https://www.jetbrains.com/pycharm/">PyCharm IDE</a> ~ PyCharm was used as the preferred IDE for this project.
* PyCharm built-in Terminal ~ Used to commit to local repository and further push to Github Repo ensuring adequate version
controlling throughout the life-cycle of the project build.
* <a href="https://git-scm.com/">Git</a> ~ Installed on local device and integrated to PyCharm as a Plugin to enable version controlling.
* <a href="https://github.com/auxfuse/Milestone1">Github</a> ~ Used to host the repository of all previous versions of the build and linked to Heroku to push the latest changes to the deployed build version held there.
* <a href="https://www.heroku.com/">Heroku</a> ~ A cloud platform as a service enabling deployment for this CRUD application.

#### Tools Used:

* <a href="https://www.mongodb.com/cloud/atlas">MongoDB Atlas</a> ~ Non-relational database hosting service used.
* <a href="https://plugins.jetbrains.com/plugin/7141-mongo-plugin/versions">PyCharm Plugin Mongo Explorer</a> ~ Used to track changes to the database from my IDE instead of using the MongoDB website in the browser.
* <a href="https://mycolor.space/">ColorSpace</a> ~ Used to find complimentary color schemes used throughout the application.
* <a href="http://eye-dropper.kepi.cz/">Eye Dropper (Color Picker)</a> ~ Open Source Google Chrome Extension used to obtain hexadecimal/rgba/hsl values of colours. Built by Kepi (<a href="https://github.com/kepi">Kepi's Github</a>)
* Google Chrome DevTools ~ Used to test the application's functionality, the responsiveness of same, and the CSS visualisation, as well as assisting in such tasks as figuring out the correct style properties to override Bootstraps user agent styling.
* <a href="https://balsamiq.com/">Balsamiq</a> ~ Used for the creation of my pre-build wireframes showing the main elements and differences in size of same through small to large screen sizes.
* <a href="https://realfavicongenerator.net/">Favicon Generator</a> ~ Used to create favicon from custom Logo I created for the project.
* <a href="https://validator.w3.org/">W3C HTML Validator</a> & <a href="https://validator.w3.org/">W3C CSS Validator</a> & <a href="https://jshint.com/">JSHint</a> ~ Used to check the validity and efficiency of my code.
* <a href="https://autoprefixer.github.io/">Autoprefixer CSS Online</a> ~ Used to check for possible webkits required in the applications stylesheet ensuring Cross-browser support.
* <a href="http://pep8online.com/">PEP 8 Online Validator</a> ~ to check my python code to be consistent with PEP8 requirements.
* Adobe Photoshop ~ to create the custom long and short variations of the Logo for this application.


## Features

The project boasts several key features:
* Create: Several instances of create functionality as per CRUD, via the Registration form creating a new user in the database and a Logged in user being able to create a new Workout via the create form.
* Read: Is implemented throughout the site from showing an un-logged user the fundamentals and such workouts deemed public by a logged in user to the filtered by personal login 'My workouts' lists.
* Update: Present for a logged in user in their own documents to update same and push back to the database.
* Delete: Present for a logged in user in their own documents to delete with confirmation from the database.
* Locate: Functionality instanced in checking a username is on the database via Login.
* Basic email functionality via html mailto attribute and assigned to a social icon in the Footer.

[Back to Top](#table-of-contents)

#### Future Features:

* Swap always-playing gifs on each fundamental card to only play on user click or use an icon overlay to simulate play/pause affect.
* Email functionality via SMTP server instead of using basic HTML href mailto attribute value.
* Search functionality to search by multiple features such as Date, Location, Focus type etc on both public and bespoke user lists of workouts.
* Pagination on both public and bespoke user lists of workouts, unfortunately due to time constraints this will be have to be implemented once the project has come back from grading.
* Coach login to create workouts for other individual users based on access control levels.
* Admin login to manage collection database records such as location names & focus types from the application instead of via the PyCharm plugin Mongo Explorer or the MongoDB Atlas Dashboard.

## Testing

Testing was done throughout the application build and when build was finished. The application structure and mobile-first layout was tested on Google Chrome, Opera, Microsoft Edge and Safari. As well as most of my testing taking place manually on my PC for which the build also took place, Chrome Devtools was used constantly to test on as many devices as possible from Android Samsung & Huawei device dimensions to Apple phones & tablet dimensions, and of course laptop and above sizes. The application was tested constantly on two at-hand smartphone devices throughout the build at home, a Hauwei P20 Pro and a Samsung Galaxy S9 aswell as a Samsung Tab2 Tablet.

Mongo Explorer, (the PyCharm Plugin for MongoDB) was used in conjunction with the built-in PyCharm terminal and the Werkzeug Online Debugger were used to test the Create, Locate, Read, Update and Delete Functionality. 

If a bug arose during testing it was dealt with during the development of the build.

#### Found Bugs and Fixes:

During manual testing of the application by one of my peers in Slack, it was brought to my attention that the cards on the Fundamentals page were offsetting to left on their mobile device, Samsung Galaxy S9+. As I had access to a Samsung Galaxy S9, I tested the same view on that device and the visual offset was not present. By creating a custom devtools Emulated Device for a Samsung Galaxy S9+ it allowed me to see the visual bug in my manual testing. See next image of the same issue also happening on the Pixel 2 device.

<p align="center">
    <img height="350" src="https://github.com/auxfuse/Milestone3/blob/master/static/images/card-offset.PNG" alt="Oly-Track Logo">
</p>

Using devtools and some basic element debugging, I was able to determine that the hard-coded `max-width` style property on the card class in my CSS file was the culprit. It wasn't causing any sizing or positional problems on device widths greater than 574px. So instead of removing the max-width property entirely from the CSS file, I decided it was best to remove it from the card class in the main portion of my CSS and add it to a media query from 575px and up device widths:

```css
@media (min-width: 575px) {
    .card {
        max-width: 20rem;
    }
}
```

[Back to Top](#table-of-contents)

##### Defensive Design

Defensive design for this application was built into each template as well as where appropriate each function in app.py file.
 * A registration system posting the user's accepted details to the collection users in the database.
 * A login system to allow the user to login and thus have access to Create documents or Update and Delete only those documents that they have created previously.
 * Constant checks for if user is logged in where applicable in the app.py file and html templates, such as differing Nav-items shown depending on login status.
 * Protection was built into each template not applicable to an un-logged user in the form of 'if logged in' validation aswell as hiding appropriate section in case of Browser URL hardcoding.
 * Custom multiple flash warnings produced depending on info entered into certain forms, for example if a user entered an already taken username on registration.

## Deployment

This multi-page application was developed in PyCharm IDE and version controlling was utilised via local (git) and online (github) repository technologies. Several github branches were used throughout the development of this application as it allowed me a learning process with same, I have left those branches available in the Github branches tab of my <a href="https://github.com/auxfuse/Milestone3">repository</a>

Deploying this application was achieved through Github pages and hosted on Heroku by:
* Selecting the Repository from my linked Github in Heroku.
* And setting up auto build from most recent commit history.
"https://oly-track.herokuapp.com/".

To clone the repository:
* Select the Repository from the Github Dashboard.
* Click on the "Clone or download" green button located above and to the right of the File Structure table.
* Click on the "clipboard icon" to the right of the Git URL to copy the web URL of the Clone.
* Open your preferred Integrated Development Environment (IDE) and navigate to the terminal window.
* Change the directory to where you want to clone the repository too. (In the case of PyCharm the directory path can be found through the "Navigate" tab).
* Paste the Git URL copied from above and click "Ok". (Again in the case of PyCharm once you click "clone", Git Root mapping will be automatically set to the project Root directory).

[Back to Top](#table-of-contents)

## Credits

* Hashing passwords using Bcrypt credit to Corey Schafer <a href="https://www.youtube.com/watch?v=CSHx6eCkmv0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=7&t=1674s">tutorial</a> on Youtube.

* Dropdown population assisted by <a href="https://github.com/TravelTimN">Tim_CI</a> via <a href="https://code-institute-room.slack.com/archives/C7JQY2RHC/p1579969487145000?thread_ts=1579965191.134700&cid=C7JQY2RHC">Slack</a>.

* Edit form population assistance by <a href="https://github.com/coderbeez">Edel O' Sullivan</a> via Slack posts <a href="https://code-institute-room.slack.com/archives/C7JQY2RHC/p1580035505186300">#1</a> & <a href="https://code-institute-room.slack.com/archives/C7JQY2RHC/p1580035823189800">#2</a>.

* 

[Back to Top](#table-of-contents)

#### Special Thanks & Acknowledgements:

* Those in Slack, Tutor Support and my Mentor Spencer Barriball for assisting with me with countless queries since starting on my Python Fundamentals journey until now.

###### <i>Disclaimer: This project was created for educational use only as part of the Code Institute Full Stack Software Development Course for Milestone 3 Grading!</i>

[Back to Top](#table-of-contents)