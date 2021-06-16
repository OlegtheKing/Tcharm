from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import TTS
import requests as r
import os

@login_required
def saved(request):
    if request.user.is_authenticated:
        saved = TTS.objects.filter(owner=request.user).values("file")
        print()
        sizes = []
        for i in saved:
            name = i["file"][i["file"].find("response"):]
            pathfile = r"C:\Users\Олег\Desktop\Tcharm\Tcharm\media\tts" + "\\" + name
            try:
                filesize = str(round(os.path.getsize(pathfile)/1024, 2)) + "KB"
                sizes.append(filesize)
            except WindowsError:
                pass
        print(sizes)
        urls = [saved[i]["file"] for i in range(len(saved))]
        data = zip(urls, sizes)
        return render(request, "TTS/saved.html", {"data": data})


@login_required
def converttoaudio(request):
    if request.method == "POST":
        phrase = request.POST["content"]
        key = "15c6798df7724f159641a19267bd97a2"
        lang = "en-us"
        codec = "MP3"
        quality = "48khz_16bit_stereo"
        url = f"http://api.voicerss.org/?key={key}&hl={lang}&c={codec}&f={quality}&src={phrase}"
        response = r.request("GET", url)
        with open("response.mp3", "wb") as f:
            f.write(response.content)
        with open("response.mp3", "rb") as f:
            djfile = File(f)
            tts = TTS(owner=request.user, file=djfile)
            tts.save()
        pathfile = r"C:\Users\Олег\Desktop\Tcharm\Tcharm" + tts.file.url
        filesize = str(round(os.path.getsize(pathfile)/1024, 2)) + "KB"
        return JsonResponse({"audiopath": tts.file.url, "filesize": filesize})

# def download(request, filepath):
#     fname = "tts/" + filepath
#     try:
#         object = TTS.objects.get(owner=request.user, file=fname)
#         fullpath = r"C:\Users\Олег\Desktop\Tcharm\Tcharm" + object.file.url
#         return FileResponse(open(fullpath, "rb"), as_attachment=True)
#     except ObjectDoesNotExist:
#         pass

