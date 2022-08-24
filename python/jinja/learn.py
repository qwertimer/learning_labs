import jinja2
from jinja2 import Environment, FileSystemLoader
import typer

app = typer.Typer()

@app.command()
def basics():
    environment = jinja2.Environment()
    template = environment.from_string("Hello, {{ name }}!")
    template.render(name = "World")


@app.command(name="grade")
def school_grades():
    max_score = 100
    test_name = "Python Challenge"
    students = [
        {"name":"Tim", "score":100},
        {"name":"Harry", "score":80},
        {"name":"Mary", "score":50},
        {"name":"Ron", "score":33},
        {"name":"Bob", "score":76},
    ]
    env = Environment(loader=FileSystemLoader("templates/"))
    template = env.get_template("message.txt")
    for student in students:
        filename = f"message_{student['name'].lower()}.txt"
        content = template.render(
            student,
            max_score = max_score,
            test_name = test_name
        )
        with open(filename, mode="w", encoding="utf-8") as m:
            m.write(content)
            print(f"wrote {filename}")

@app.command(name="grade_html")
def school_grades_html():
    max_score = 100
    test_name = "Python Challenge"
    students = [
        {"name":"Tim", "score":100},
        {"name":"Harry", "score":80},
        {"name":"Mary", "score":50},
        {"name":"Ron", "score":33},
        {"name":"Bob", "score":76},
    ]
    res_filename = "students_results.html"
    env = Environment(loader=FileSystemLoader("templates/"))
    res_template = env.get_template("results.html")
    content ={
        "students":students,
        "test_name":test_name,
        "max_score": max_score,
        }
    with open(res_filename, mode="w", encoding="utf-8") as m:
        m.write(res_template.render(content))
        print(f"wrote {res_filename}")
if __name__=="__main__":
    app()
