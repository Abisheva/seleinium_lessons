from selenium import webdriver
import time
import math

"""Расчет значения для капчи"""
def med_func(x):
    return  str(math.log(abs(12*math.sin(int(x)))))

window = webdriver.Chrome() # открываем браузер
window.get("http://suninjuly.github.io/alert_accept.html") #открываем страницу
button = window.find_element_by_css_selector("button.btn") #ищем кнопку по css_selecory
button.click() # кликаем на кнопку
conform = window.switch_to.alert #переключаемься на окно alert
conform.accept() #принимает условие окна alert
var = window.find_element_by_id("input_value") #поиск элемента по id
input1 = window.find_element_by_id("answer") #поиск окна введения по id
button1 = window.find_element_by_css_selector("button.btn") #поиск кнопки
input1.send_keys(med_func(var.text)) #введение значения в найденном окне
button1.click() #нажатие кнопки, после введения в окно ввода
print(window.switch_to.alert.text) #печать значение текста окна alert
window.quit() #закрытие браузера




