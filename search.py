#!/usr/bin/python3
# coding: utf-8

from bs4 import BeautifulSoup
import requests
from re import compile, sub


def towns(start, end):
    the_link = f"https://www.bonnesroutes.com/distance/?from={start}&to={end}"
    content = requests.get(the_link)
    return content


def webToFile(link):
    soupeuh = str(BeautifulSoup(link.content, "html.parser"))
    with open("workfile.html", "w") as w_file:
        w_file.write(soupeuh)


def parsFile(file):
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


def timeCompute(dist):
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
            compute += 33
            pop += 1
            if compute >= 60:
                compute -= 60
                counter_hour += 1



    hours = int(timeresult_list[0]) + counter_hour

    del timeresult_list[:]
    timeresult_list.append(str(hours))
    timeresult_list.append(str(compute))

    final_time = " : ".join(timeresult_list)
    return final_time


def writeInTab(file_name, start, end):
    concate = f"""Ville de départ, Ville d'arrivée, Temps de trajet total
{start}, {end}, {timeCompute(parsFile("workfile.html"))}"""
    with open(file_name, "w") as board:
        board.write(concate)