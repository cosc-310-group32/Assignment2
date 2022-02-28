# Elon Musk Bot ![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?logo=flask&logoColor=white)

<p align="center"> 
<img width="620" height="414" src="static/img/ElonMusk.png">
</p>

Elon Musk Bot is a chatbot inspired by the entrepreneur and billionaire Elon Musk. It can answer questions about Tesla, SpaceX, cryptocurrencies - give it a try!

## Setting Up and Launching

To launch the Elon Musk bot, first [install Python](https://realpython.com/installing-python/) on your machine. Once Python is installed, launch your terminal on the folder containing the repository and run:

```
pip install -r requirements.txt
```

After `pip` has finished installing the requirements, run:

```
python app.py
```

To launch the bot. Access `http://127.0.0.1:5000/` on your browser to interact with the Elon Musk bot!

### Note

It is possible port 5000 is already being used by another process. In this case, look at the output in the terminal:

```
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Click on the link that says `Running on http://127.0.0.1:abcd/`, it will take you to the bot.

## Code Structure

```
    .
    ├── app.py                    # Code for the Python back-end - it handles requests to the bot
    ├── data.json                 # Answers to the predefined topics Elon Musk bot can answer
    ├── template                  # Contains the front-end logic for the user interace
    └── README.md                 # This file!
```

## Built With

* [Python](https://www.python.org/) and [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Back End

## Authors

- [Kiet Phan](https://github.com/ketphan02)
- [Ivan Carvalho](https://github.com/IvanIsCoding)
- [Lydia Lin](https://github.com/yuqi88)
- [Akshat Singal](https://github.com/aksingal-dev)
- [Paula Wong-Chung](https://github.com/KafkaNoNeko)

