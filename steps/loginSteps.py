import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('user launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    #raise NotImplementedError(u'STEP: Given user launch chrome browser')

@when('user navigated to Guru99 Demo Login')
def step_impl(context):
    context.driver.get("https://demo.guru99.com/test/newtours/")
    #raise NotImplementedError(u'STEP: When user navigated to Guru99 Demo Login')


@when('user login using username and password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='userName']").send_keys("test@gmail.com")
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456")
    context.driver.find_element(By.XPATH, "//input[@name='submit']").click()
    #raise NotImplementedError(u'STEP: When user login using username and password')


@then('user was able to navigate to Homepage successfully')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Login Successfully')]")  # Replace "some-id" with the actual ID of the element
    assert element.text == "Login Successfully", f"Assertion failed! Found text: {element.text}"
    print("Assertion passed: The element contains 'Login Successfully'.")
    #raise NotImplementedError(u'STEP: Then user was able to navigate to Homepage successfully')