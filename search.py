#!/usr/bin/python3
# coding: utf-8

import sys
from bs4 import BeautifulSoup
import requests
from re import compile, sub

# town1 = input("Entrez une town de départ: \n")
# town2 = input("Entrez une town de sortie: \n")
# print(f"Lien: https://www.bonnesroutes.com/distance/?from={town1}&to={town2}")

# the_link = requests.get(f"https://www.bonnesroutes.com/distance/?from={town1}&to={town2}")
the_link = requests.get("https://www.bonnesroutes.com/distance/?from=Bordeaux&to=Marseille")


def web_to_file(link):
    soupeuh = str(BeautifulSoup(link.content, "html.parser"))
    with open("workfile.html", "w") as w_file:
        w_file.write(soupeuh)


def pars_file(file):
    web_to_file(the_link)
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

        compile(the_string)
        regex = sub("[^0-9]", "", the_string)
        distance = int(regex)
        return distance


def time_compute():
    dist = pars_file("workfile.html")
    speed = 90
    counter_hour = 0
    # t = d/v <==
    # d = v * t
    # v = d/t

    timeresult = round(dist / speed, 2)

    timeresult_list = str(timeresult).split(".")
    compute = round(int(timeresult_list[1]) * 60 / 100 + 18)

    nb_pause = round(int(timeresult_list[0]) / 2)

    if nb_pause > 0:
        pop = 0
        while pop < nb_pause:
            compute += 15
            pop += 1

    if compute >= 60:
        compute -= 60
        counter_hour += 1

    hours = int(timeresult_list[0]) + counter_hour

    del timeresult_list[:]
    timeresult_list.append(str(hours))
    timeresult_list.append(str(compute))

    final_time = "h ".join(timeresult_list)
    print(f"Le temps total est : {final_time}min. ")
    return final_time


time_compute()
