
# Jinja Notes

This Readme contains notes that i have taken whilst learning Flask. 
Check out the learn.py code for my flask learning.

## Part 1
 -- From [Real Python](https://realpython.com/primer-on-jinja-templating/)
### Working with Flask and Jinja2

Install Flask with
`python3 -m pip install flask`

We can created a basic web app with a single route using the `@` syntax of flask.
`@app.route("/")`
This will allow us to create a single endpoint at the route of the website.

We can run the flask development webserver with `python3 learn.py`. This will start a server on localhost at port 5000.

## Part 2
### Adding Jinja to the webserver.

We can use Jinja in the base.html file to template our html file. Once done we can import render_template from flask to do the same thing as Jinja provided in my notes on Jinja.

## Part 3
### Making a route for the school grades

We can take the example inside the jinja learning and convert the results to a served up page with flask. By adding a `/results` route. Inside the `/results` route we render the template with a `**context` to load all values from the dictionary into the render_template as it only accepts keyword arguments.

## Part 4
### Nesting templates

We use a parent child template structure to keep code maintainable. The child inherits from the parent.
We can use the `{% block %}` tag to define what can be overwritten in the base template.
We use names in the block to show what can be overwritten by what. For example a `{% block title %}` will be overwritten by any title tag. In the children.

## Part 5

Jinja has built in filter functions, many of which reflect python builtins. We can adjust things like case with the `|` pipe symbol. For example we can change the mnu item with `menu_item|upper`

