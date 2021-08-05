from django.shortcuts import render

from pos_api.models import *
from django.template import loader
from django.http import HttpResponse, JsonResponse



# Create your views here.

def index(request):
    print('in index')

      
    
    context = {
      
         
    }


 
   
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def mainpage_ajax(request):
    print('input_str.....')
    if request.method == "GET" and request.is_ajax():


        input_str=request.GET.get('inputStr')
        print('input_str.....',input_str)

        word_tokens = nltk.word_tokenize(input_str)
        word_with_tag = nltk.pos_tag(word_tokens)

        print(word_with_tag)

        word_list= []
        for o in word_with_tag:
            print(o)
            word_list.append({'word':o[0],'pos':o[1]})

        print(word_list)




        context = [{
            'output':word_list
        }]        
     
        return JsonResponse(context, safe = False)

    return JsonResponse({"success":False}, status=400)

# def mainpage(request):    

    

#     context = {
#         # 'obj':obj
#     }

#     if request.method=="POST":
#         input_str=request.POST.get('input-str')
#         print('input_str.....',input_str)

#         word_tokens = nltk.word_tokenize(input_str)
#         word_with_tag = nltk.pos_tag(word_tokens)

#         context = {
#             'output':word_with_tag
#         }
     
    
#     html_template = loader.get_template( 'output.html')    
#     return HttpResponse(html_template.render(context, request))
