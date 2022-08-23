# Jinja Notes

This Readme contains notes that i haave taken whilst learning Jinja. 
Check out the learn.py code for my jinja learning.

For all my learning code i wrap functions in typer cli applications for testing and learning.

## Part 1
 -- From [Real Python](https://realpython.com/primer-on-jinja-templating/)

Install Jinja with
`python3 -m pip install Jinja2`

Importing Jinja is done through a lowercase j.
`import jinja2`

We add jinja templating by using `{{  }}` inside strings as well as templated files. Template.render will return the rendered content substituting the variables with the templated options.

## Part 2 -- Using logic in the template

We can modify the template to include logic with `{% %}` along with internal logic such as `{% if score > 80 %}` etc. In this configuration we also need to say where the block ends with `{% endif %}`. We can also use `for` logic inside documents such as html to render all the names or items of a list.

Check out the templates directory to view this in action.
