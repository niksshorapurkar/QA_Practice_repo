import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch chrome browser')
def browser_launcher(context):
    context.driver = webdriver.Chrome()


@when(u'I open orangeHRM homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when(u'Enter the username "{user}" and password "{pwd}"')
def username(context, user, pwd):
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)


@when(u'click on login button')
def login(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()


@then(u'User must successfully login to the Dashboard page')
def dashboard(context):
    time.sleep(15)
    text = context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    assert text == "Dashboard"
    context.driver.close()
