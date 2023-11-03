# INF601 - Advanced Programming in Python
# Adam Staggenborg
# Mini Project 3

# x(5/5 points) Initial comments with your name, class and project at the top of your .py file.
# x(5/5 points) Proper import of packages used.
# x(70/70 points) Using Flask you need to setup the following:
# x(10/10 points) Setup a proper folder structure, use the tutorial as an example.
# x(20/20 points) You need to have a minimum of 5 pages, using a proper template structure.
# x(10/10 points) You need to have at least one page that utilizes a form and has the proper GET and POST routes setup.
# x(10/10 points) You need to setup a SQLlite database with a minimum of two tables, linked with a foreign key.
# x(10/10) You need to use Bootstrap in your web templates. I won't dictate exactly what modules you need to use but the more practice here the better. You need to at least make use of a modal.
# x(10/10) You need to setup some sort of register and login system, you can use the tutorial as an example.
# x(5/5 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# x(5/5 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# x(10/10 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations. You will need to explain the steps of initializing the database and then how to run the development server for your project.


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

