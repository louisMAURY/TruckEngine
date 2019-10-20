#!/usr/bin/python3
# coding: utf-8

import sys
from bs4 import BeautifulSoup
from six.moves import urllib
import requests
import re

# ville1 = input("Entrez une ville de départ: \n")
# ville2 = input("Entrez une ville de sortie: \n")
# print(f"Lien: https://www.bonnesroutes.com/distance/?from={ville1}&to={ville2}")

# lien = requests.get(f"https://www.bonnesroutes.com/distance/?from={ville1}&to={ville2}")
lien = requests.get("https://www.bonnesroutes.com/distance/?from=Bordeaux&to=Marseille")


def web_to_file(link):
    soupeuh = str(BeautifulSoup(link.content, "html.parser"))
    with open("workfile.html", "w") as w_file:
        w_file.write(soupeuh)


def pars_file(file):
    web_to_file(lien)
    work_list = []
    list_seption = []

    with open(file, 'r') as work_file:
        soup = BeautifulSoup(work_file, "html.parser")
        dat_id = soup.find(id="total_distance")
        for code in dat_id:
            work_list.append(code)

        # There is 3 '\n' in the work_list
        for i in "...":
            work_list.remove("\n")

        for div in work_list:
            list_seption.append(str(div))
        the_string = "".join(list_seption)

        re.compile(the_string)
        regex = re.sub("[^0-9]", "", the_string)
        distance = int(regex)
        return distance

def time_calcul():
    dist = pars_file("workfile.html")
    speed = 90
    # t = d/v <==
    # d = v * t
    # v = d/t

    timeresult = round(dist/speed, 2)
    print(timeresult)
    timeresult_list = str(timeresult).split(".")
    print(timeresult_list)








time_calcul()