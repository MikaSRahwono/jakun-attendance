import requests
import json

def get_qr(url):
    qr = 'https://chart.googleapis.com/chart?cht=qr&chs=300x300&chl='+url
    return qr