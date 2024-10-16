# TODO
## Features by page
## Wireframes
## Surface colors typo
## database models
## deploy

# Community Appliances
## [Live site here](https://community-appliances-3af27dd26db9.herokuapp.com/)
## Overview
- Community Appliances is a django e-commerce app that allows users to purchase refurbished domestic appliances (washing machines and electric and gas cookers) from a fictional charity organisation. The charity accepts donations of used appliances which are refurbished for sale to raise funds. The organisation is run by volunteers and the app also enables new volunteers to sign-up if they have an account. E-commerce functionality is via the [Stripe](https://stripe.com/gb) on-line payment platform.

## User Stories
The design of the app was guided by user stories. The categories of user considered were,
- visitors without an account
- users with an account
- site owner (Admin)

To allow analysis user stories were categorised into the areas of functionality below
- Making purchases
- Registering for an account
- Users with an account
- Managing the store

### Making Purchases
The following apply to users with or without an account 
- As a user I want to view items by category, ordered by condition or price
- As a user I want to view detailed information on selected items
- As a user I want to view, add and remove items in my cart 
- As a user I want to enter my delivery details and view my cart and payment details at checkout
- As a user I want to have a familiar experience making on-line payment for my items and have access to all the relevant details
- As a user I want to get an email confirming my order has been placed.

This [video](https://github.com/user-attachments/assets/79698b64-8b53-451e-a0c8-70dce84bbfa2) gives an overview of most of the main actions in the purchasing process.

### Registering for an Account
- As a user I want to sign-up for an account to access useful/interesting additional features in the app

### Users with an Account
Visitors can make purchases with or without an account. However, signing-up for an account gives users access to additional useful or interesting functionality
- As a user with an account I want to create and update default delivery information to prefill my delivery details into a form at checkout
- As a user with an account I want to view a record of previous purchases, ie an order-history
- As a user with an account I want the option to make a volunteer profile linked to my account, in order to volunteer with the charity

### Managing the Store (Admin User)
The store admin needs access to order details in the database in order to fullfil customer orders. Additionally, the admin user needs to manage user accounts and user and volunteer profiles. The admin also needs to be able to add and remove products, and edit product details. These actions are performed via the Django admin panel.

- As an admin user I want full CRUD functionality for all models in the application database.


### User Messaging
Providing users with immediate feedback from interactions with the app was a key consideration in design. Colour coded alert Bootsrap alerts together with the Django messaging system achieved this goal.
- As a user I want immediate clear feedback messages from interactions with the app

## Features
### Main Navigation - All Pages
![screenshot](documentation/readme/features/main-nav1.png)

The main navigation contains the site logo which acts as a link back to the home page from anywhere on the site. The navbar also has an account dropdown and a link to the users cart diplaying the value of the cart.

![screenshot](documentation/readme/features/main-nav-account2.png)

For a non logged in user the account dropdown shows links to the login and registration pages.

![screenshot](documentation/readme/features/main-nav-account1.png)

For a logged in user the account dropdown contains links to a user profile and a volunteer profile page.

The main navbar displays a horizontal menu of options to search for appliances by category 

![screenshot](documentation/readme/features/nav-menu1.png)

When selected, each category displays a dropdown with options to search by price or grade (condition) ascending or descending

![screenshot](documentation/readme/features/nav-menu2.png)

On small devices the menu of options collapses behind a hamburger button

![screenshot](documentation/readme/features/nav-menu3.png)

### Home Page

The home page features a prominent "Shop Now" button to invite users to easily engage with the site and clicking this displays a default view of all appliances ordered by price descending.

![screenshot](documentation/readme/features/home-shop-now-button.png)


## Credits

### Technologies
| Source | Notes |
| --- | --- |
| [Gimp](https://www.gimp.org/) |used to crop and compress images  |
| [Simplescreenrecorder](https://www.maartenbaert.be/simplescreenrecorder/) |used to make screen recordings  |

 ### Tools
| Source | Notes |
| --- | --- |
| [Gimp](https://www.gimp.org/) |used to crop and compress images  |
| [temp-mail](https://temp-mail.org/en/) |for test email accounts|
| [Simplescreenrecorder](https://www.maartenbaert.be/simplescreenrecorder/) |used to make screen recordings  |

### Media 
| Source | Notes |
| --- | --- |
| [Favicon.io](https://favicon.io/favicon-generator/) | used to generate website favicon  |
| [Unsplash](https://unsplash.com/photos/white-\front-load-washing-machine-5cpBWEl6y6c)|background image for homepage|
| [Markselectrical](https://markselectrical.co.uk/ww11bb504daws1_samsung-washing-machine)|Washing machine placeholder image|
| [Markselectrical](https://markselectrical.co.uk/dsc626g-1bl_delonghi-gas-cooker-with-single-oven)|Gas cooker placeholder image placeholder image|
| [Markselectrical](https://markselectrical.co.uk/dsc626g-1bl_delonghi-gas-cooker-with-single-oven)|Electric cooker placeholder image placeholder image|


### Content

| Source | Location | Notes |
| --- | --- | --- |
| [W3Schools](https://www.w3schools.com/) | whole site | reference for bootstrap, html, css, javascript and python |
| [Markdown Guide](https://www.markdownguide.org/cheat-sheet/) | README.md and TESTING.md | syntax guide for writing Markdown files |
| [w3schools](https://www.w3schools.com/css/css_positioning.asp)| index.html | sticky cta button on homepage |
|[Stack Overflow](https://stackoverflow.com/questions/18838463/bootstrap-center-navbar-items)| base.html |overide Bootstrap nav style classes |
|[MDN Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)|base.html|reference on css selector specificity|
|[Chatgpt](https://openai.com/blog/chatgpt)|index.html|used to generate homepage "About us" section text content|
|[Bootstrap 5](https://getbootstrap.com/docs/5.3/components/card/#horizontal)| product details page|horizontal bootstrap card|
|[Bootstrap 5 crispy forms](https://stackoverflow.com/questions/71641974/implementing-django-bootstrap-crispy-forms-into-default-signup-login-pages)| template forms |implementing crispy forms for bootstrap5|
|[Django messages](https://www.horilla.com/blogs/how-to-enhance-user-notifications-with-django-messages-framework/)| user messaging in templates |implementing user messaging|
|[Python "in" dict operator](https://realpython.com/python-in-operator/#dictionaries-and-sets)| views.py cart app |check if item already in cart |
|[Form validation for postcode field](https://docs.djangoproject.com/en/5.0/ref/forms/validation/)| forms.py checkout app |check for valid postcode in delivery details form |
|[Django queryset order_by](https://www.w3schools.com/django/django_queryset_orderby.php)| views.py products app |implement order by descending product price |
|[Remove field labels from allauth forms](https://stackoverflow.com/a/64737110/11411026)| base.css | |
|[Raise 403 error](https://stackoverflow.com/a/67184068/11411026)| views.py profiles app | |
|[Customise Django Admin Panel](https://realpython.com/customize-django-admin-python/#modifying-a-change-list-using-list_display)| admin.py volunteers app | customise change list |


