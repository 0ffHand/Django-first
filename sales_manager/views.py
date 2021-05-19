from django.http import HttpResponse
from django.shortcuts import render


def main_page():
    return HttpResponse("Hello, this is main page")


