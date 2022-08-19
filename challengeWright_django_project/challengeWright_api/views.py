
from re import search
from django.shortcuts import redirect, render

# Create your views here.
from rest_framework import viewsets

from challengeWright_api.serializers import NoteLenovoSerializer
from challengeWright_api.models import NoteLenovo

from pickle import FALSE
from playwright.sync_api import sync_playwright
import time
import string
from asgiref.sync import sync_to_async



@sync_to_async
def ScraperBot(requests):
    

    with sync_playwright() as p:
        browser =  p.chromium.launch()
        page = browser.new_page()
        page.goto("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
        
        notebooks = page.query_selector_all(".thumbnail")
        cont = 0
        for note in notebooks:
            cont+=1
        
            
            price =  note.query_selector('.price')
            price =  price.inner_text()
            name = note.query_selector('.title')
            name = name.inner_text()
            descript =  note.query_selector('.description')
            descript = descript.inner_text()
            # print(name + price)

            if search("Lenovo", name) and search("Lenovo", descript):
                print(name + price)
                
                name = name.translate(str.maketrans('', '', string.punctuation))
                price = price.translate(str.maketrans('', '', "$"))
                price = float(price)
                new_notebook = NoteLenovo(cont, name,descript, price)
                time.sleep(1)
                new_notebook.save()
                
            else:
                continue
            
        
        print()
        time.sleep(5)
        browser.close()

        serializer = NoteLenovoSerializer(new_notebook)
        serializer.data
        return render(
            requests,
            "index.html",
        )
    
        
            
class NoteLenovoViewSet(viewsets.ModelViewSet):
   queryset = NoteLenovo.objects.order_by("price").all()
   serializer_class = NoteLenovoSerializer

