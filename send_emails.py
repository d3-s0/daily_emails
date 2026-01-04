import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import requests
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def return_random_link(url):
    """
    Return random url link contained in url given
    """
    # Use requests to send a get request to the webpage
    response = requests.get(url)

    # Use BeautifulSoup to parse the webpage response
    soup = BeautifulSoup(response.text, 'html.parser')

    links = [urljoin(url, link.get('href')) for link in soup.find_all('a') if link.get('href')]

    link_list = []
    for link in links:
        link_list.append(link)
    link_chosen = random.choice(link_list)

    return link_chosen

def send_email(from_address, password, to_address):
    msg=MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "Daily email"

    csv_urls_df = pd.read_csv('urls.csv')
    csv_url_random = []
    try:
        for index, csv_url in enumerate(csv_urls_df.iloc[:,0]):
            url = return_random_link(csv_url)
            csv_url_random.append(url)
    except Exception as e:
        print(f"Error has occured {e}")

    body = "<html><body><p>Read these posts:</p><ul>"
    for url in csv_url_random:
        body += f"<li><a href='{url}'>{url}</a></li>"
    body +="</ul></body></html>"

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 999)
    server.startls()
    server.login(from_address, password)
    server.sendmail(from_address, to_address, msg.as_string())


parser = argparse.ArgumentParser(description="Send emails")
parser.add_argument('--from-address', required = True, help='From email addres')
parser.add_argument('--password', required = True, help='Email address authentication password')
parser.add_argument('--to-address', required = True, help='To email addres')
parser.add_argument('--clips', required = True, help='Path to kindle clippings text file')
args = parser.parse_args()

sender_email = args.from_address
sender_password = args.password
recipient_email = args.to_address
clips_path=args.clips

send_email(sender_email, sender_password, recipient_email, clips_path)


