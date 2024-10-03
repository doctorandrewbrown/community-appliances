
# Testing

Return back to the [README.md](README.md) file.

## HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files. All pages were validated on the live website. Were possible pages were validated by address. For pages only available to logged in users the html source code was copied from the browser and validated with the text input option in the validator. The same procedure was used  pages such as "cart" and "checkout" which could only be meaningfully validated were there is some user interaction with the page.

| Page | W3C URL | Screenshot/Validation Method |Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2F) | ![screenshot](documentation/testing/images/w3c-home.png) |no errors or warnings|
| Products | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2Fproducts%2F) | ![screenshot](documentation/testing/images/w3c-products.png) | no errors or warnings|
| Product Detail | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2Fproducts%2F6) | ![screenshot](documentation/testing/images/w3c-product-detail.png) |no errors or warnings|
| Checkout | n/a | text input | no errors or warnings|
| Cart | n/a | text input | no errors or warnings|
| Checkout Success | n/a | text input | no errors or warnings|
| Profile | n/a | text input | no errors or warnings|
| Order History | n/a | text input | no errors or warnings|
| Volunteers | n/a | text input | no errors or warnings|

## CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot/Validation method | Notes|
| --- | --- | --- | --- |
| base.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) |![screenshot](documentation/testing/images/w3c-css.png)| no errors|
| product.css | n/a |text input| no errors|
| checkout.css | n/a |text input| minor warning about vendor extension|

## Python PEP8 Compatibility

I have used the [CI Python Linter](https://pep8ci.herokuapp.com/)  to check Python code for compatibility with the [PEP8 standard](https://peps.python.org/pep-0008/).

| Python File | Screenshot | Notes |
| --- | --- | --- |
| cart apps.py | ![screenshot](documentation/testing/images/pep-cart-apps.png) | No errors |
| cart contexts.py | ![screenshot](documentation/testing/images/pep-cart-contexts.png) | No errors |
| cart urls.py | ![screenshot](documentation/testing/images/pep-cart-urls.png) | No errors |
| cart views.py | ![screenshot](documentation/testing/images/pep-cart-views.png) | No errors |
| cart views.py | ![screenshot](documentation/testing/images/pep-cart-views.png) | No errors |
| checkout urls.py | ![screenshot](documentation/testing/images/pep-checkout-urls.png) | No errors |
| checkout apps.py | ![screenshot](documentation/testing/images/pep-checkout-apps.png) | No errors |
| checkout forms.py | ![screenshot](documentation/testing/images/pep-checkout-forms.png) | No errors |
| checkout models.py | ![screenshot](documentation/testing/images/pep-checkout-models.png) | No errors |
| checkout signals.py | ![screenshot](documentation/testing/images/pep-checkout-signals.png) | No errors |
| checkout admin.py | ![screenshot](documentation/testing/images/pep-checkout-admin.png) | No errors |
| checkout views.py | ![screenshot](documentation/testing/images/pep-checkout-views.png) | No errors |
| home views.py | ![screenshot](documentation/testing/images/pep-home-views.png) | No errors |
| home urls.py | ![screenshot](documentation/testing/images/pep-home-urls.png) | No errors |
| products admin.py | ![screenshot](documentation/testing/images/pep-products-admin.png) | No errors |
| products models.py | ![screenshot](documentation/testing/images/pep-products-models.png) | No errors |
| products urls.py | ![screenshot](documentation/testing/images/pep-products-urls.png) | No errors |
| products views.py | ![screenshot](documentation/testing/images/pep-products-views.png) | No errors |
| profiles admin.py | ![screenshot](documentation/testing/images/pep-profiles-admin.png) | No errors |
| profiles forms.py | ![screenshot](documentation/testing/images/pep-profiles-forms.png) | No errors |
| profiles models.py | ![screenshot](documentation/testing/images/pep-profiles-models.png) | No errors |
| profiles views.py | ![screenshot](documentation/testing/images/pep-profiles-views.png) | No errors |
| profiles urls.py | ![screenshot](documentation/testing/images/pep-profiles-urls.png) | No errors |
| volunteers admin.py | ![screenshot](documentation/testing/images/pep-volunteers-admin.png) | No errors |
| volunteers forms.py | ![screenshot](documentation/testing/images/pep-volunteers-forms.png) | No errors |
| volunteers models.py | ![screenshot](documentation/testing/images/pep-volunteers-models.png) | No errors |
| volunteers urls.py | ![screenshot](documentation/testing/images/pep-volunteers-urls.png) | No errors |
| volunteers views.py | ![screenshot](documentation/testing/images/pep-volunteers-views.png) | No errors |
| community-appliances custom_storages.py | ![screenshot](documentation/testing/images/pep-custom-storages.png) | No errors |
| community-appliances settings.py | ![screenshot](documentation/testing/images/pep-settings.png) | No errors |
| community-appliances urls.py | ![screenshot](documentation/testing/images/pep-urls.png) | No errors |

## JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.


| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](documentation/testing/images/jshint-stripe-js.png) | Undefined Stripe variable from external library |

## Browser Compatibility

I have tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Products | Product Detail | Cart | Checkout | Checkout Success | Profile | Volunteers | Order History | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/images/browser-chrome-home.png) | ![screenshot](documentation/testing/images/browser-chrome-products.png) | ![screenshot](documentation/testing/images/browser-chrome-products-detail.png)|![screenshot](documentation/testing/images/browser-chrome-cart.png)|![screenshot](documentation/testing/images/browser-chrome-checkout.png)|![screenshot](documentation/testing/images/browser-chrome-checkout-success.png)|![screenshot](documentation/testing/images/browser-chrome-profile.png)|![screenshot](documentation/testing/images/browser-chrome-volunteers.png)| ![screenshot](documentation/testing/images/browser-chrome-order-history.png)| Works as expected 
| Opera | ![screenshot](documentation/testing/images/browser-opera-home.png) | ![screenshot](documentation/testing/images/browser-opera-products.png) | ![screenshot](documentation/testing/images/browser-opera-products-detail.png)|![screenshot](documentation/testing/images/browser-opera-cart.png)|![screenshot](documentation/testing/images/browser-opera-checkout.png)|![screenshot](documentation/testing/images/browser-opera-checkout-success.png)|![screenshot](documentation/testing/images/browser-opera-profile.png)|![screenshot](documentation/testing/images/browser-opera-volunteers.png)| ![screenshot](documentation/testing/images/browser-opera-order-history.png)| Works as expected 
| Firefox | ![screenshot](documentation/testing/images/browser-firefox-home.png) | ![screenshot](documentation/testing/images/browser-firefox-products.png) | ![screenshot](documentation/testing/images/browser-firefox-products-details.png)|![screenshot](documentation/testing/images/browser-firefox-cart.png)|![screenshot](documentation/testing/images/browser-firefox-checkout.png)|![screenshot](documentation/testing/images/browser-firefox-checkout-success.png)|![screenshot](documentation/testing/images/browser-firefox-profile.png)|![screenshot](documentation/testing/images/browser-firefox-volunteers.png)| ![screenshot](documentation/testing/images/browser-firefox-order-history.png)| Works as expected 

## Responsiveness

I have tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Products | Product Detail | Cart | Checkout | Checkout Success | Profile | Volunteers | Order History | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mobile (iPhone SE) Dev Tools| ![screenshot](documentation/testing/images/responsive-mobile-home.png) | ![screenshot](documentation/testing/images/responsive-mobile-products.png) | ![screenshot](documentation/testing/images/responsive-mobile-product-details.png)|![screenshot](documentation/testing/images/responsive-mobile-cart.png)|![screenshot](documentation/testing/images/responsive-mobile-checkout.png)|![screenshot](documentation/testing/images/responsive-mobile-checkout-success.png)|![screenshot](documentation/testing/images/responsive-mobile-profile.png)|![screenshot](documentation/testing/images/responsive-mobile-volunteers.png)| ![screenshot](documentation/testing/images/responsive-mobile-order-history.png)| Works as expected 
| tablet (iPad Mini) Dev Tools| ![screenshot](documentation/testing/images/responsive-tablet-home.png) | ![screenshot](documentation/testing/images/responsive-tablet-products.png) | ![screenshot](documentation/testing/images/responsive-tablet-product-detail.png)|![screenshot](documentation/testing/images/responsive-tablet-cart.png)|![screenshot](documentation/testing/images/responsive-tablet-checkout.png)|![screenshot](documentation/testing/images/responsive-tablet-checkout-success.png)|![screenshot](documentation/testing/images/responsive-tablet-profile.png)|![screenshot](documentation/testing/images/responsive-tablet-volunteers.png)| ![screenshot](documentation/testing/images/responsive-tablet-order-history.png)| Works as expected 
| Laptop (real device 1366x768px)| ![screenshot](documentation/testing/images/responsive-laptop-home.png) | ![screenshot](documentation/testing/images/responsive-laptop-products.png) | ![screenshot](documentation/testing/images/responsive-laptop-product-details.png)|![screenshot](documentation/testing/images/responsive-laptop-cart.png)|![screenshot](documentation/testing/images/responsive-laptop-checkout.png)|![screenshot](documentation/testing/images/responsive-laptop-checkout-success.png)|![screenshot](documentation/testing/images/responsive-laptop-profile.png)|![screenshot](documentation/testing/images/responsive-laptop-volunteers.png)| ![screenshot](documentation/testing/images/responsive-laptop-order-history.png)| Works as expected 


## User Story Testing
[User stories](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#user-stories) were used to specify a program of manual testing of the app functionality. The manual tests involved going through the steps required by the user stories to check correct functioning.
### [Making Purchases](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#making-purchases)
| User Story | Tests |Video/Screenshot | Notes | Pass/Fail |
|:--- | :--- |----| --- | --- |
| As a user I want to view items by category, ordered by condition or price|for each item category order results by price (ascending and descending) or grade A-C (ascending and descending) |[video](https://github.com/user-attachments/assets/24115b06-a8c4-474d-9c52-bfeff6b01373) |video shows ordering the "All Appliances" category by price and grade (ascending and descending). Similar tests were conducted for other appliance categories| Pass|
| As a user I want to view detailed information on selected items|for an item selected from the search results user can view enlarged image, product description, condition details and saftey details|[video](https://github.com/user-attachments/assets/850f2d43-b192-4bd5-9469-74e48cd183f0) |video shows a product details view with the more detailed information including a product description, a dropdown with condition details, safety details (in this case electrical)| Pass|
| As a user I want to view, add and remove items in my cart |user can view items in cart, add and remove items (with informative messages)|[video](https://github.com/user-attachments/assets/d7879cee-eb48-4672-884a-c6b9aa2b508b) |video shows items being added and removed from cart with cart total in navbar incrementing and decrementing correctly. User messaging is shown at each stage| Pass|
| As a user I want to enter my delivery details and view my cart and payment details at checkout |user should be able to view an itemised breakdown of the cost of their order and any discount. The amount to be charged to the card should be clearly indicated|    ![screenshot](documentation/testing/stories/stories-view-checkout.png) |the screenshot shows an itemised break down of the order with sums correctly calculated and clearly shown. The payment details are again shown in warning text next to the payment button| Pass|
| As a user I want to have a familiar experience making on-line payment for my items and have access to all the relevant details |user should have a familiar payment interface and immediate confirmation of their order |[video](https://github.com/user-attachments/assets/19345825-03eb-4914-8e0d-48e923e0e52a) |video shows payment via a familiar interface provided by Stripe. The user gets immediate confimation that the order has been successfully placed with a breakdown of all the order information. The user is informed they will get an email| Pass|
| As a user I want to get an email confirming my order has been placed. |user should receive email confirmation of their order containing all relevant details |![screenshot](documentation/testing/stories/stories-email.png) |the screen shot shows an example order confirmation email containing all the order details| Pass|

### [Registering for an Account](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#registering-for-an-account)
- As a user I want to sign-up for an account to access useful/interesting additional features in the app

This user story was tested by going through the registration process with a temporary email for a fictional user.

|sign-up form|verify email|email confirm link|email confirmed|
| --- | --- | --- | --- |
| ![screenshot](documentation/testing/stories/authentication-signup-form.png)| ![screenshot](documentation/testing/stories/authentication-verify-email.png)| ![screenshot](documentation/testing/stories/authentication-temp-email-link.png)| ![screenshot](documentation/testing/stories/authentication-email-confirmed.png)|


### [Users with an Account](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#users-with-an-account)
| User Story | Tests |Video/Screenshot | Notes | Pass/Fail |
|:--- | :--- |----| --- | --- |
| As a user with an account I want to create and update default delivery information to prefill my delivery details into a form at checkout|delivery details form is pre-filled at checkout |[video](https://github.com/user-attachments/assets/adb4dab8-e8dc-4357-b607-2bc45d54a1d3) |video shows form prefilled at checkout once user signs in| Pass |
| |user can edit default delivery details|![screenshot](documentation/testing/stories/stories-account-profile-update.png)| |Pass|
| As a user with an account I want to view a record of previous purchases, ie an order-history|user can view list and detail views of previous orders |[video](https://github.com/user-attachments/assets/f7294884-af53-4828-95a9-d3ba5523c9a5) |video shows list and detail views to signed in user| Pass |
| As a user with an account I want the option to make a volunteer profile linked to my account, in order to volunteer with the charity|user can create and update a volunteer profile |[video](https://github.com/user-attachments/assets/0bd4dd42-967d-477a-bb32-f3c4335ff03c) |video shows signed in user editing volunteer profile including toggling 'checkbox to indicate availability| Pass |

### [User Messaging](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#user-messaging)
- As a user I want immediate clear feedback messages from interactions with the app

This user story was tested by ensuring messaging was triggered as intended and was informative to the user. Examples of messaging used in the app are shown below

|info| success |warning | error |
| --- | --- | --- | --- |
| ![screenshot](documentation/testing/stories/stories-messages-info.png)  |![screenshot](documentation/testing/stories/stories-messages-success.png)| ![screenshot](documentation/testing/stories/stories-messages-warning.png)| ![screenshot](documentation/testing/stories/stories-messages-error.png)|

### [Managing the Store (Admin User)](https://github.com/doctorandrewbrown/community-appliances/blob/main/README.md#managing-the-store)
- As an admin user I want full CRUD functionality for all models in the application database.

This user story was tested by manually performing create, read, update and delete test actions on each model from within the admin panel. The admin panel screenshots below show the list view and the change form for each model.

| app | model| admin list view| admin change form | Pass/Fail |
| --- | --- | --- | --- | --- | 
| Checkout | Orders | ![screenshot](documentation/testing/stories/stories-admin-orders-list.png) | ![screenshot](documentation/testing/stories/stories-admin-orders-change.png)  | Pass | 
| Products | Products | ![screenshot](documentation/testing/stories/stories-admin-products-list.png) | ![screenshot](documentation/testing/stories/stories-admin-products-change.png)  | Pass | 
| Products | Categories | ![screenshot](documentation/testing/stories/stories-admin-categories-list.png) | ![screenshot](documentation/testing/stories/stories-admin-categories-change.png)  | Pass | 
| Products | Certificates | ![screenshot](documentation/testing/stories/stories-admin-certificates-list.png) | ![screenshot](documentation/testing/stories/stories-admin-certificates-change.png)  | Pass | 
| Products | Condition | ![screenshot](documentation/testing/stories/stories-admin-condition-list.png) | ![screenshot](documentation/testing/stories/stories-admin-condition-change.png)  | Pass | 
| Profiles | User profiles | ![screenshot](documentation/testing/stories/stories-admin-profiles-list.png) | ![screenshot](documentation/testing/stories/stories-admin-profiles-change.png)  | Pass | 
| Profiles | User profiles | ![screenshot](documentation/testing/stories/stories-admin-volunteers-list.png) | ![screenshot](documentation/testing/stories/stories-admin-volunteers-change.png)  | Pass | 


