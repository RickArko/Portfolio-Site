import sys
import time
import requests
from pathlib import Path
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


file_path = Path(__file__).resolve().parent

if sys.platform == 'win32':
    driver_name = 'geckodriver-win64.exe'
if sys.platform == 'linux':
    driver_name = 'geckodriver'

drivers_path = file_path.joinpath(f'drivers/{driver_name}')

url = 'http://127.0.0.1:5050/'

def test_homepage():
    r = requests.get(url + 'home')
    assert r.status_code == 200

def test_experience():
    r = requests.get(url + 'experience')
    assert r.status_code == 200

def test_projects():
    r = requests.get(url + 'projects')
    assert r.status_code == 200

def test_blog():
    r = requests.get(url + 'blog')
    assert r.status_code == 200

def test_contact():
    r = requests.get(url + 'contact')
    assert r.status_code == 200

def test_contact_failure_post():
    data = {}
    data['name'] = 'admin'
    data['email'] = 'admin@admin.com'
    data['subject'] = 'pytest'
    data['message'] = 'pytest'

    r = requests.post(url + 'contact', params=data)
    assert r.status_code in (400, 500)
