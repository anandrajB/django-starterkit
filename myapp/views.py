import logging

from django.shortcuts import render

# Create your views here.


logging.basicConfig(
    filename="myproject.log", format="%(asctime)s %(message)s", filemode="w"
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def index(request):
    logger.info("this is a index page")
    return render(request, "index.html")


def page1(request):
    logger.info("moved to page1 from index page")
    return render(request, "page1.html")
