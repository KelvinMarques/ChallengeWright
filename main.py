from pickle import FALSE
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
    print(page.title())

    html = page.inner_html('.col-md-9')
    # print(html)
    notebooks = page.query_selector_all(".thumbnail")
    cont = 0
    for note in notebooks:
        cont+=1
        # note = note.query_selector('.text')
        price = note.query_selector('.price').inner_text()
        name = note.query_selector('.title').inner_text()
        description = note.query_selector('.description').inner_text()
        print(name + price)
    # print(notebooks)
    print(cont)
    time.sleep(5)
    browser.close()