__version__ = '0.0.1'

print(__version__)

Skip
to
content
Search or jump
to…
Pulls
Issues
Codespaces
Marketplace
Explore


@JimmyTRT


JimmyTRT
/
HealthClient
Public
Fork
your
own
copy
of
JimmyTRT / HealthClient
Code
Issues
Pull
requests
Actions
Projects
Wiki
Security
Insights
More
Beta
Try
the
new
code
view
HealthClient / main.py /


@Jimvdb


Jimvdb
hello
api
get
respons
uuid
…
Latest
commit
ec9cff7
3
weeks
ago
History
1
contributor
91
lines(70
sloc)  2.22
KB

import uvicorn as uvicorn
import time
import threading
from www import app
from api import api
from schedule import every, repeat, run_pending
from logger import setup_logger
import utils
import requests

# create logger
logger = setup_logger()

controller_id = None


# check the config file tov source
@repeat(every(1).hour)
def check_config():
    print("run config check")
    controller_config = utils.read_controller_config()
    logger.info(controller_config)
    print(controller_config)


@repeat(every(10).seconds)
def show():
    # todo: poort nummer meegeven in de dict
    logger.info("try send config")
    controller_config = utils.read_controller_config()
    if controller_id == None:
        url = "http://127.0.0.1:9090/hello"
        try:
            response = requests.post(url, json=controller_config)
            logger.info(response.status_code)
            logger.info(response.content)
            logger.info(response.text)
        except:
            print("auw")


@repeat(every(10).seconds)
def check_something():
    pass


def schedule():
    while True:
        run_pending()
        time.sleep(1)


def check_calendar():
    pass


def fast_api():
    uvicorn.run(api, host="0.0.0.0", port=9080)


# todo: Poort numers variable maken

# print(utils.ntp.get_ntp())

# start de applicatie
if __name__ == '__main__':
    logger.info("Starting application")
    logger.info("Read config file")
    controller_config = check_config()
    if controller_id == None:
        url = "http://127.0.0.1:9090/hello"
        try:
            response = requests.post(url, data=controller_config)
            logger.info(response.text)

        except:
            print("failed")

    # start routine 1 - Flask applicatie
    logger.info("Starting www on port 8080")
    threads = []
    t_app = threading.Thread(target=app.run, kwargs={'port': 8090}).start()
    threads.append(t_app)
    # start routine 2 - FastAPI applicatie
    logger.info("Starting api on port 9090")
    t_api = threading.Thread(target=fast_api).start()
    threads.append(t_api)
    # start routine 3 - leest en schrijft data naar de database en voert tijdgebonden functies uit
    threading.Thread(target=schedule).start()
    threading.Thread(target=check_calendar).start()
Footer
© 2023
GitHub, Inc.
Footer
navigation
Terms
Privacy
Security
Status
Docs
Contact
GitHub
Pricing
API
Training
Blog
About
HealthClient / main.py
at
main · JimmyTRT / HealthClient