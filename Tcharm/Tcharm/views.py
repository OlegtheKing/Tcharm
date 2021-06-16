from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import re
import requests as r
import json


def land(request):
    return render(request, "Tcharm/body.html")


def about(request):
    return render(request, "Tcharm/about.html")


def correctspelling(request):
    if request.method == "POST":
        text = request.POST["content"]
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r",+", ",", text)
        text = re.sub(r" \.", ".", text)
        text = re.sub(r" ,", ",", text)
        text = re.sub(r" !", "!", text)
        text = re.sub(r" \?", "?", text)

        url = "https://montanaflynn-spellcheck.p.rapidapi.com/check/"
        headers = {
            'x-rapidapi-host': "montanaflynn-spellcheck.p.rapidapi.com",
            'x-rapidapi-key': "9d96c490a0msh8b403a297ed25e7p1e6973jsn46068b8bf8c7"
        }
        querystring = {"text": text}
        response = r.request("GET", url, headers=headers, params=querystring)
        return JsonResponse({"corrected": response.text}, safe=False)


def searchforoverused(request):
    if request.method == "POST":
        text = request.POST["content"]
        splitted = re.findall(r"\w+", text)
        grouped = {}
        for i in splitted:
            if i in grouped:
                grouped[i] += 1
            else:
                grouped[i] = 1
        overused = {}
        for k, v in grouped.items():
            if v > 2:
                overused[k] = v
        return JsonResponse({"overused": overused})

def suggestsyn(request):
    word = request.GET["content"]
    key = "8aa6d395-2730-478a-8bc5-5b3fbeb88c62"
    url = f"https://www.dictionaryapi.com/api/v3/references/ithesaurus/json/{word}?key={key}"
    responsestr = r.request("GET", url).text
    response = json.loads(responsestr)
    return JsonResponse({"word": response})
