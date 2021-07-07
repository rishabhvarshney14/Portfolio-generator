# Portfolio Generator

Portfolio Generator is a webapp that let users to create responsive portfolio without any frontend or backend knowledge.

You can check the web app at https://portfolio-generator1.herokuapp.com/

A sample portfolio built with this can be seen at https://portfolio-generator1.herokuapp.com/lorum01/

Portfolio Generator is created with Django.

You provide it your data and it will create a portfolio website for you without worrying much about Setting up your System or anything.

## Running the project locally

Before setting up the project please create a virtual enviornment (check [this tutorial](https://realpython.com/lessons/creating-virtual-environment/) for more info).

1. Clone this repo and navigate to the cloned directory from your terminal or cmd.
2. run ```pip install -r requirements.txt``` to install the required libraries.
3. You also need to generate a secret id to run this project which can be generated from [here](https://djecrety.ir/). Once you have your secret key paste it into portfolio_gen/settings.py line: 12.
4. run ```python manage.py migrate``` to make all the required migrations.
5. To run the server, run ```python manage.py runserver```
6. Enjoy!