import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.ebay.com/p/8033753133?iid=184100936380'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}


def check_product():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(class_="product-title").get_text()
    price = soup.find(class_="display-price").get_text()
    converted_price = float(price[1:4])

    if(converted_price > 500):
        send_mail()


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('rajsuthan666@gmail.com', 'nopuqjkxgxuaursw')

    name = input("Enter Reciever's name : ")

    subject = "Price Fell Down"
    heading = f'Hi {name}'
    body = 'Check this link https://www.ebay.com/p/8033753133?iid=184100936380'

    msg = f'Subject: {heading}\n\n\n {subject}\n\n {body}'

    email_to = input("Enter Reciever's Email :")

    server.sendmail(
        'rajsuthan666@gmail.com',
        email_to,
        msg
    )
    print("Email is succesfully sent!!!")

    server.quit()


while(True):
    check_product()
    time.sleep(60*60)
