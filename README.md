# Milestone Project 3
***

## Table of Contents:
* [section link](link here)
    * [sub-section link](link here)

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

* Home Page:

The Home (Index) Page contained all the major navigation points for both a logged-in or non logged-in user. It contained a hero image to portray the theme and defining nature of the application aswell as a brief description surrounding the app and it's cause for creation.

<img align="left" width="125" height="250" src="" alt="Home page mobile wireframe">
<img align="right" width="400" height="250" src="" alt="Home page tablet-desktop wireframe">



[Back to Top](#table-of-contents)

## Technology Used

[Back to Top](#table-of-contents)

#### Languages, Frameworks, Editors & Version Control:

#### Tools Used:

## Features

[Back to Top](#table-of-contents)

#### Future Features:

#### Removed Features:

## Testing

#### Found Bugs and Fixes:

During manual testing of the application by one of my peers in Slack, it was brought to my attention that the cards on the Fundamentals page were offsetting to left on their mobile device, Samsung Galaxy S9+. As I had access to a Samsung Galaxy S9, I tested the same view on that device and the visual offset was not present. By creating a custom devtools Emulated Device for a Samsung Galaxy S9+ it allowed me to see the visual bug in my manual testing. See next image of the same issue also happening on the Pixel 2 device.

<p align="center">
    <img src="https://github.com/auxfuse/Milestone3/blob/master/static/images/card-offset.PNG" alt="Oly-Track Logo">
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

## Deployment

[Back to Top](#table-of-contents)

## Credits

[Back to Top](#table-of-contents)

#### Special Thanks & Acknowledgements:

###### <i>Disclaimer: This project was created for educational use only as part of the Code Institute Full Stack Software Development Course for Milestone 3 Grading!</i>

[Back to Top](#table-of-contents)