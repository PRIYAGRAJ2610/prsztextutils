# I've created this file - "Priyag Raj Sharma"
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'index.html')
    # return HttpResponse("WELCOME TO PRS CREATION")

def analyze(request):
    # get the text
    djtext = request.GET.get('text','default')

    # check the checkbox value
    removepunc = request.GET.get('removepunc','off')
    uppercase = request.GET.get('uppercase', 'off')
    charactercounter = request.GET.get('charactercounter', 'off')
    print(removepunc)
    print(djtext)

    #check which checkbox is on
    if removepunc  == "on":




        punctuations = '''"":;()[]{}'~`!/?<>.@#$%^&*-+=,|'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'remove punctuations','analyzed_text':analyzed}
    #analyze the text
        return render(request , 'analyze.html', params)
    elif uppercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charactercounter == "on":


        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed = analyzed + 1


        params = {'purpose': 'charactercounter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else :
        return HttpResponse("  ERROR : check box is not checked")