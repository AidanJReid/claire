[![Build Status](https://travis-ci.org/AidanJReid/claire.svg?branch=master)](https://travis-ci.org/AidanJReid/claire)

# Claire's Massages - Full Stack eCommerce site offering a range of massage and alternative therapy treatments.

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Colour Scheme**](#colour-scheme)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)
    - [**User Journey**](#user-journey)
    - [**General**](#general)
    - [**Validators**](#validators)
    - [**Issues**](#issues)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

![Responsiveness Test](/static/assets/images/wireframe/screencap.JPG)

This is the fourth milestone project of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies. 
The objective for this project is to...

It is designed for...


### User Stories

1. **User story 1**: 
2. **User story 2**: 
3. **User story 3**: 
4. **User story 4**: 

### Design


#### Framework

- [Bootstrap v.]()
    - 
- [jQuery 3.4.1](https://code.jquery.com/jquery/)
    - I used the most recent version of jQuery for my Javascript framework.
- [Flask 1.1.1](http://flask.pocoo.org/)
    - Flask is a web framework that enable web applications builds which I was determined to use to make backend coding easier.

#### Colour Scheme

TBC
- `#00bcd4` (**cyan** - *primary colour*)
- `#f44336` (**red** - *secondary colour*) 
- `#fb8c00` (**orange darken-1** - *tertiary colour*)

#### Icons


#### Typography


### Wireframes

I used **Balsamiq for desktop** wireframes for two reasons:
- Students have free access to the desktop version until the end of 2020.
- I really enjoyed how simple and easy it is to use for mockups especially in conversations with my assigned mentor for brainstorming.

![claire.png](/static/img/claire.png)


## Features

### Existing features

##### Navbar
- Used Bootstrap [Template]() for its ease of use and simple design.
- Deployed a **Sticky navbar** which makes navigation easier for the user, especially on mobile.
- Navigation items from left to right:
  *  **Logo**

Sidenav pops out on small to medium devices (max-width 992 px) and contain the aforementioned nav links.

##### Footer
- Used Bootstrap footer and simply indicated purpose of site, share my *Github* and linking to *Facebook*.

### Features Left to Implement

**Pagination** -

## Technologies Used

- [Gitpod](https://www.gitpod.io/) - Used for the closing stages of my project because I ran out of credits on AWS.
- [GitHub](https://github.com/) - Used to store code in a remote repository, hosting and for successful deployment of site.

### Front-End Technologies
- **HTML**
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used to structure pages, forms and associated content with user profiles as well as database. 
It also featured in the nav and footer sections of the page.
- **CSS**
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- **JQuery**
    - [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used to improve and simplify Javascript code.

### Back-End Technologies
- **Flask**
    - [Flask 1.1.1](http://flask.pocoo.org/) - Used as a microframework.
    - [Jinja 2.10.3](http://jinja.pocoo.org/docs/2.10/) - Used as a template engine w/ Flask.
- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for app hosting.
- **Python**    
    - [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language.


## Testing

### User Journey

Testing for each user scenario:

1. **User story 1**: :white_check_mark:
2. **User story 2**: :white_check_mark:
3. **User story 3**: :white_check_mark:
4. **User story 4**: :white_check_mark:

### General

Regular testing was conducted throughout the course of this project, especially before commits to Github.

**Responsive/Mobile-first design** was tested using Chrome developer tools to ensure desired layout was achieved. 
As well as Chrome, I also used Safari (12.0) and Firefox (68.0.2) which collectively successfully affirmed my project's responsiveness.
To test responsiveness, the following mobiles were tested Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5/SE 6/7/8 Plus X, iPad and iPad Pro. All successfully passed in mobile responsiveness of the page.

### Validators

**HTML**
- [HTML Checker](https://validator.w3.org/).

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

### Issues


| Number | Issue            | Resolution   |
|--------|------------------|--------------|
|  1  | Security vulnarability with Django 1.11.24  | Fixed - Upgraded Django to 1.11.27  |
|  2  | Pagination  | TBC  |
|  3  |   |   |
|  4  |   |   |
|  5  |   |   |
|  6  |   |   |
|  7  |   |   |
|  8  |   |   |

## Deployment

### Github

Deployed using the Master Branch on hosting platform GitHub Pages. 

The following steps were taken:

  1. 
  2. 
  3. 
  4. 
  5. 

### Heroku

Deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `sudo pip3 freeze --local > requirements.txt`
    - My file can be found [here]().
2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: python run.py > Procfile`
    - My file can be found [here]().
3. Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as follows:
    - **IP** : `0.0.0.0`
    - **PORT** : `8080`
5. App should be successfully deployed to Heroku at this point.


## Credits

### Content

### Media

* Responsiveness and device images from [Responsive Design](http://ami.responsivedesign.is/)
* Favicon created at [Favicon.io](https://favicon.io/)
* Logo created at [Logohub.io](https://logohub.io/)
* Image Gallery:
    - 

### Acknowledgements

* Inspiration and structural format for this README from [Travel Tim's oustanding project](https://github.com/TravelTimN/ci-milestone04-dcd)
* Brian Macharia, my CI mentor, for his support and patience.