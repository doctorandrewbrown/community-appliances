# TODO
## Features by page
## Wireframes
## Surface colors typo
## database models
## deploy
## future work

# Community Appliances
## [Live site here](https://community-appliances-3af27dd26db9.herokuapp.com/)
# Strategy
## Overview
- Community Appliances is a django e-commerce app that allows users to purchase refurbished domestic appliances (washing machines and electric and gas cookers) from a fictional charity organisation. The charity accepts donations of used appliances which are refurbished for sale to raise funds. The organisation is run by volunteers and the app also enables new volunteers to sign-up if they have an account. E-commerce functionality is via the [Stripe](https://stripe.com/gb) on-line payment platform.
# Scope
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

# Structure
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

The home page introduces the charity and gives users some background information.
The page features a prominent "Shop Now" button to invite users to easily engage with the site and clicking this takes the user to the products page which initially displays a default view of all appliances ordered by price descending.

![screenshot](documentation/readme/features/home-shop-now-button.png)

### Products Page

The products page shows appliances in the chosen category (or "All Appliances") with the selected ordering. The products are presented in an attractive card format with some initial information. Clicking on a card takes the user to a product details page for the selected product.

![screenshot](documentation/readme/features/products-cards.png)

To assist the user the products page title clearly indicates the the category of products displayed,

![screenshot](documentation/readme/features/products-title.png)

### Product Details Page

Product details for a selected item are again presented in a familiar card format. 

![screenshot](documentation/readme/features/product-details-card1.png)

The product details card contains a number of features to assist the user
- A clickable image to open a larger view of the item
- A dropdown on hover giving a more detailed description of the item grade

 ![screenshot](documentation/readme/features/product-details-dropdown.png)

- A button to add the item to the users cart

 ![screenshot](documentation/readme/features/product-details-add-button.png)

- When an item is successfully added to the cart a message informs the user

 ![screenshot](documentation/readme/features/product-details-message-success.png)

 - If the item is already in the cart a message alert informs the user 

 ![screenshot](documentation/readme/features/product-details-message-warning.png)

-  The "Keep Shopping" button is included to quickly return the user to the products page initially displaying all items ordered by price descending

 ![screenshot](documentation/readme/features/product-details-keep-shopping-button.png)

### Cart Page

- Clicking the cart icon link in the main navigation takes the user to the cart page

![screenshot](documentation/readme/features/cart-icon-link.png)

- Details of cart contents are shown to the user in a clear table format

![screenshot](documentation/readme/features/cart-table-header.png)

- A button is provided to remove an item if desired

![screenshot](documentation/readme/features/cart-remove-button.png)

- On removing an item a message is shown to inform the user

![screenshot](documentation/readme/features/cart-message-warning.png)

- For extra-small devices a condensed version of the cart contents table is displayed with the description column ommited and a smaller remove button

![screenshot](documentation/readme/features/cart-small-table.png)

- If the cart is empty the user is informed

![screenshot](documentation/readme/features/cart-empty-message.png)

-   The "Continue Shopping" button is included to quickly return the user to the products page initially displaying all items ordered by price descending

 ![screenshot](documentation/readme/features/cart-continue-shopping-button.png)

- Once the user is ready to checkout the "Checkout" link button takes the user to the checkout page

![screenshot](documentation/readme/features/cart-checkout-button.png)

### Checkout Page

The checkout page contains the form for delivery details, a summary of the cart contents and a card payment details input facility for making payments via Stripe.

- For non logged in users a form containing prompts is provided for delivery details

![screenshot](documentation/readme/features/checkout-delivery-details-form.png)

- If the user is not logged in links are shown below the form to the log in and sign-up pages if the user wishes to change or save their delivery details to a user profile.

![screenshot](documentation/readme/features/checkout-login-to-save.png)


- If the user has an account the delivery details form will be prefilled by any default details contained in their "profile". If the user wishes to update their default details with the information entered in the form a checkbox is provided

![screenshot](documentation/readme/features/checkout-checkbox.png)

- Basic postcode validation is implemented for the delivery details form which results in an alert message for an invalid form entry

![screenshot](documentation/readme/features/profile-error-message.png)

- A clear summary of the cart contents, and payment breakdown is provided to the user in tabular format

![screenshot](documentation/readme/features/checkout-order-summary.png)

- The payment details are again highlighted in warning text next to the payment button to alert the user before they confirm the purchase. If a discount applies this is displayed.

![screenshot](documentation/readme/features/checkout-warning.png)

- A Stripe card payment input box is located at the end of the form

![screenshot](documentation/readme/features/checkout-card-input.png)

- Next to the button to confirm the purchase, is a button link titled "Adjust Cart" back to the users cart. This gives the user an opportunity if they wish, to add or remove items from the cart before proceding with payment

![screenshot](documentation/readme/features/checkout-adjust-button.png)

- A "Complete Order" button submits the completed form to process the payment via the Stripe platform.

![screenshot](documentation/readme/features/checkout-complete-order-button.png)


### Checkout Success Page

- A successful checkout triggers the checkout success page informing the user the user they will get email confimation of their purchase.

![screenshot](documentation/readme/features/checkout-success-message.png)

- An order breakdown with all relevant details is displayed.

![screenshot](documentation/readme/features/checkout-success-order-confirmation.png)

- The "Continue Shopping" button at the bottom of the order confirmation invites the user to continue engagement with the site. The button provides a link to the products page displaying the default of all products ordered by descending price.

![screenshot](documentation/readme/features/checkout-success-continue-shopping-btn.png)

### Profile Page

A user profile is created for all account holders and can be accessed via the link in the dropdown from the account icon in the main navbar.

The profile can be used to store default delivery details to prefill into the checkout form, and also to access details of previous orders ie an order history.

- The page displays a form showing default delivery details and a table showing a summary of previous orders. The entries in the order history table are clickable links to a more detailed order history view for the particular order.

![screenshot](documentation/readme/features/profile-page.png)

- The default delivery details can be edited by the user and clicking the update button notifies the user of a successful update

![screenshot](documentation/readme/features/profile-update-button.png)


![screenshot](documentation/readme/features/profile-message.png)

- Basic postcode validation is implemented for the default delivery details form which results in an alert message for an invalid form entry

![screenshot](documentation/readme/features/profile-error-message.png)

### Order History Page

The details of previous purchases are available to account holders by clicking a link for a particular order in the order history table of the profile page.

- An info alert box reminds the user they are viewing details of a previous order

![screenshot](documentation/readme/features/order-history-message.png)

- Previous order details are displayed in a tabular format

![screenshot](documentation/readme/features/order-history-table.png)

- A button provides a link back to the profile page

![screenshot](documentation/readme/features/order-history-button.png)

### Volunteers Page
A volunteers profile is created for all account holders and logged in users access their profile via a link in the account icon dropdown in the main navbar. 

![screenshot](documentation/readme/features/volunteers-nav-link.png)

- Users who wish to volunteer with the charity can leave their details in the form

![screenshot](documentation/readme/features/volunteers-form.png)

- Users can toggle the "Active" checkbox to indicate their availability

![screenshot](documentation/readme/features/volunteers-checkbox.png)

- Users can save changes to their details via an "Update Information" button

![screenshot](documentation/readme/features/volunteers-update-btn.png)

- An alert success message informs the user of a successful update 

![screenshot](documentation/readme/features/volunteers-message.png)

# Skeleton
## Wireframes
| Page | Device | Wireframe |
| --- | --- | --- |
| Home | mobile | [wireframe](documentation/readme/wireframes/wireframe-mobile-home.jpg) |
| Products |mobile  | [wireframe](documentation/readme/wireframes/wireframe-mobile-products.jpg) |
| Product Details | mobile | [wireframe](documentation/readme/wireframes/wireframe-mobile-product-details.jpg) |
| Cart | mobile | [wireframe](documentation/readme/wireframes/wireframe-mobile-cart.jpg) |
| Checkout | mobile | [wireframe](documentation/readme/wireframes/wireframe-mobile-checkout.jpg) |
| Checkout Success | mobile | [wireframe](documentation/readme/wireframes/wireframe-mobile-checkout-success.jpg) |
| Profile | mobile | [wireframe](documentation/readme/wireframes/wireframe-mobile-profile.jpg) |
| Volunteers | mobile | [wireframe](documentation/readme/wireframes/wireframe-mobile-volunteers.jpg) |
| Order History | mobile | [wireframe](documentation/readme/wireframes/wireframe-mobile-order-history.jpg) |
| Home | tablet | [wireframe](documentation/readme/wireframes/wireframe-tablet-home.jpg) |
| Products | tablet  | [wireframe](documentation/readme/wireframes/wireframe-tablet-products.jpg) |
| Product Details | tablet | [wireframe](documentation/readme/wireframes/wireframe-tablet-product-details.jpg) |
| Cart | tablet | [wireframe](documentation/readme/wireframes/wireframe-tablet-cart.jpg) |
| Checkout | tablet | [wireframe](documentation/readme/wireframes/wireframe-tablet-checkout.jpg) |
| Checkout Success | tablet | [wireframe](documentation/readme/wireframes/wireframe-tablet-checkout-success.jpg) |
| Profile | tablet | [wireframe](documentation/readme/wireframes/wireframe-tablet-profile.jpg) |
| Volunteers | tablet | [wireframe](documentation/readme/wireframes/wireframe-tablet-volunteers.jpg) |
| Order History | tablet | [wireframe](documentation/readme/wireframes/wireframe-tablet-order-history.jpg) |
| Home | desktop | [wireframe](documentation/readme/wireframes/wireframe-desktop-home.jpg) |
| Products | desktop  | [wireframe](documentation/readme/wireframes/wireframe-desktop-products.jpg) |
| Product Details | desktop | [wireframe](documentation/readme/wireframes/wireframe-desktop-product-details.jpg) |
| Cart | desktop | [wireframe](documentation/readme/wireframes/wireframe-desktop-cart.jpg) |
| Checkout | desktop | [wireframe](documentation/readme/wireframes/wireframe-desktop-checkout.jpg) |
| Checkout Success | desktop | [wireframe](documentation/readme/wireframes/wireframe-desktop-checkout-success.jpg) |
| Profile | desktop | [wireframe](documentation/readme/wireframes/wireframe-desktop-profile.jpg) |
| Volunteers | desktop | [wireframe](documentation/readme/wireframes/wireframe-desktop-volunteers.jpg) |
| Order History | desktop | [wireframe](documentation/readme/wireframes/wireframe-desktop-order-history.jpg) |

# Surface

### Colour Palette
The colour palette used for site styling was chosen to be bold and clean in keeping with the site theme of domestic appliances,
- blue #0000ff
- black #000000
- white #ffffff

### Bootstrap Alerts
Colour coded bootstrap [alerts](https://getbootstrap.com/docs/4.1/components/alerts/) were used for messaging

### Typography
[Roboto](https://fonts.google.com/specimen/Roboto) font was used for all site text.

# Database
- The app uses a Postgresql relational database deployed on the [ElephantSQL](https://www.elephantsql.com/) platform. For local development the app used a **SQLite** database.

### Database Relationships

The app uses three custom models in addition to those used in the Boutique Ado walkthrough and these are shown in the entity relationship diagram below. Only relationships involving the custom models are shown and not all fields in the default User model are included.
The diagram shows
- A one-to-one relationsip of the VolunteerProfile model to the User model
- A many-to-one relationship between the Certificate model and the Product model
- A many-to-one relationship between the Condition model and the Product model

![screenshot](documentation/readme/features/database-erd.png)


# Tools and Technologies

### Languages
- HTML5
- CSS3
- Python3
- Javascript

### Frameworks
- [Django v4.2](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)

### Libraries
- [jQuery](https://jquery.com/)
- [Googlefonts](https://fonts.google.com/)
- [Fontawsome](https://fontawesome.com/)

### Platforms
- [Github](https://github.com/)
- [Gitpod](https://www.gitpod.io/)
- [Heroku](https://www.heroku.com/)
- [AWS](https://aws.amazon.com/)
- [ElephantSQL](https://www.elephantsql.com/)

### Database Management Systems
- [SQLite](https://www.sqlite.org/)
- [PostgreSQL](https://www.postgresql.org/)

### Packages

The following packages were used in the app (taken from the [requirements.txt](requirements.txt) file)
```bash
asgiref==3.7.2
boto3==1.34.62
botocore==1.34.62
crispy-bootstrap5==2024.2
dj-database-url==0.5.0
Django==4.2.13
django-allauth==0.50.0
django-crispy-forms==2.3
django-storages==1.14.2
gunicorn==21.2.0
jmespath==1.0.1
oauthlib==3.2.2
pillow==10.2.0
psycopg2==2.9.9
PyJWT==2.8.0
python-dotenv==1.0.1
python3-openid==3.2.0
pytz==2024.1
requests-oauthlib==1.3.1
s3transfer==0.10.0
sqlparse==0.4.4
stripe==9.6.0
urllib3==1.26.18

```
 ### Tools
| Source | Notes |
| --- | --- |
| [W3C HTML Validator Tool](https://validator.w3.org/nu/) |used for validating HTML code|
| [W3C CSS Validator Tool](https://jigsaw.w3.org/css-validator/validator) |used for validating CSS code|
| [Code Institute pep8 Python Validator Tool](https://pep8ci.herokuapp.com/) |used for validating python code|
| [JSHint Javascript Validator Tool](https://jshint.com/) |used for validating javascript code|
| [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) |used for testing and checking deployed website|
| [Gimp](https://www.gimp.org/) |used to crop and compress images  |
| [temp-mail](https://temp-mail.org/en/) |for test email accounts|
| [Simplescreenrecorder](https://www.maartenbaert.be/simplescreenrecorder/) |used to make screen recordings  |
| [Lucid Chart](https://www.lucidchart.com/blog/) |used to make erd diagams|
| [tinypng](https://tinypng.com/) |used to compress images|

# Testing
For all testing please see [TESTING](TESTING.md)

# Credits

### Media 
| Source | Notes |
| --- | --- |
| [Favicon.io](https://favicon.io/favicon-generator/) | used to generate website favicon  |
| [Unsplash](https://unsplash.com/photos/white-\front-load-washing-machine-5cpBWEl6y6c)|background image for homepage|
| [Markselectrical](https://markselectrical.co.uk/ww11bb504daws1_samsung-washing-machine)|Washing machine placeholder image|
| [Markselectrical](https://markselectrical.co.uk/dsc626g-1bl_delonghi-gas-cooker-with-single-oven)|Gas cooker placeholder image|
| [Markselectrical](https://markselectrical.co.uk/dsc626g-1bl_delonghi-gas-cooker-with-single-oven)|Electric cooker placeholder image|


### References

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


