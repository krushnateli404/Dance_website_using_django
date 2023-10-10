from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return  render(request,'index.html')

    # return  HttpResponse("Home")
def analyze(request):
    # Get the text
    djtext = request.GET.get('text','default')
    removepunct = request.GET.get('removepunct','off')
    capfirst = request.GET.get('capfirst', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    spaceremove   = request.GET.get('spaceremove', 'off')
    charcount   = request.GET.get('charcount', 'off')

    # print(removepunct)
    print((djtext))
    # return HttpResponse("remove punc")
    # analyzed = djtext
    if removepunct =="on":
        punctuations = '''!%&-()'{}",./?*@$^<>%#~`:;'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctutions', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html','contact.html','about.html', params)
    elif (capfirst =="on"):
        analyzed = ""
        for char in djtext:
            if char  in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html','contact.html','about.html', params)
    elif (newlineremove =="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n":
                analyzed = analyzed + char
        params = {'purpose': 'Newline remove', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html''contact.html','about.html', params)
    elif (spaceremove == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'space remove', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html','contact.html','about.html', params)
    elif (charcount == "on"):
        analyzed = ""
        for char in (str(djtext)):
            analyzed = len(analyzed + char)
        params = {'purpose': 'space remove', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')

# def capfirst(request):
#     return  HttpResponse("capitalize")
# def newlineremove(request):
#     return  HttpResponse("newlineremovel")
# def spaceremove(request):
#     return  HttpResponse("spaceremovel")
# def charcount(request):
#     return  HttpResponse("charcounter")

