from django.shortcuts import render
from PyDictionary import PyDictionary


# Create your views here.
def index(request):
    return render(request, "index.html")

def word(request):
    search = request.GET.get('search')
    dic = PyDictionary()
    meaning = dic.meaning(search)
    antonyms = dic.antonym(search)
    synonyms= dic.synonym(search)
    context = {
        "meaning" : meaning,
        "antonyms" : antonyms,
        "synonyms" : synonyms
    }
    return render(request, 'word.html', context)