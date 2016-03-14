#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import datetime
from datetime import timedelta
from src.holidays import holidays

def getLastDayOfMonth(any_day): #retorna o ultimo dia do mes
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)


def workingDays(week): #verifica se existe feriados nacionais

        for dates in holidays:
            if week == dates:
                usefullDay = week+timedelta(days=1)
                getWeekend(usefullDay)

        return getWeekend(week)

def getWeekend(week): #verifica se a data e sabado ou domingo, caso seja, sabado passa a virar sexta-feira e domingo passa a virar segunda-feira.

        days = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
        cont = days[week.weekday()]

        saturday = week-timedelta(days=1)
        sunday = week+timedelta(days=1)

        my_list = []
        if cont == "Segunda-feira" or cont == "Terça-feira" or cont == "Quarta-feira" or cont == "Quinta-feira" or cont == "Sexta-feira":
            my_list =[week]
        elif cont == "Sábado":
            my_list =[saturday]
        elif cont == "Domingo":
            my_list =[sunday]

        for usefulDay in my_list:
            return usefulDay