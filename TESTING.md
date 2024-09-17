# Testing

Return back to the [README.md](README.md) file.

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files. All pages were validated on the live website. Were possible pages were validated by address. For pages only available to logged in users the html source code was copied from the browser and validated with the text input option in the validator. The same procedure was used  pages such as "cart" and "checkout" which could only be meaningfully validated were there is some user interaction with the page.

| Page | W3C URL | Screenshot/Validation Method |Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2F) | ![screenshot](documentation/testing/images/w3c-home.png) |no errors or warnings |
| Products | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2Fproducts%2F) | ![screenshot](documentation/testing/images/w3c-products.png) | no errors or warnings|
| Product Detail | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2Fproducts%2F6) | ![screenshot](documentation/testing/images/w3c-product-detail.png) | no errors or warnings|
| Checkout | n/a | text input | no errors or warnings|
| Cart | n/a | text input | no errors or warnings|
| Checkout Success | n/a | text input | no errors or warnings|
| Profile | n/a | text input | no errors or warnings|
| Order History | n/a | text input | no errors or warnings|
| Volunteers | n/a | text input | no errors or warnings|

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot/Validation method | Notes|
| --- | --- | --- | --- |
| base.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcommunity-appliances-3af27dd26db9.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) |![screenshot](documentation/testing/images/w3c-css.png)| no errors|
| product.css | n/a |text input| no errors|
| checkout.css | n/a |text input| minor warning about vendor extension|

### Python PEP8 Compatibility

I have used the [CI Python Linter](https://pep8ci.herokuapp.com/)  to check Python code for compatibility with the [PEP8 standard](https://peps.python.org/pep-0008/).

| App | Python File | Screenshot | Notes |
| --- | --- | --- | --- |
| cart |routes.py | ![screenshot](documentation/testing/images/pep-cart-apps.png) | No errors |
| cart |contexts.py | ![screenshot](documentation/testing/images/pep-cart-contexts.png) | No errors |
| cart |urls.py | ![screenshot](documentation/testing/images/pep-cart-urls.png) | No errors |
| cart |views.py | ![screenshot](documentation/testing/images/pep-cart-views.png) | No errors |









