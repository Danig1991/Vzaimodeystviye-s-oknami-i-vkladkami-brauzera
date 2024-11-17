import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = 'https://demoqa.com/browser-windows'

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# выбрать и нажать кнопку New Tab
driver_chrome.find_element(By.ID, "tabButton").click()
print("Открыта новая вкладка.")

# перейти на открытую вкладку
driver_chrome.switch_to.window(driver_chrome.window_handles[1])
print("Переход на новую вкладку.")

# проверка присутствия на новой вкладке
value_text_on_tab = driver_chrome.find_element(
    By.ID, "sampleHeading"
).text
assert value_text_on_tab == "This is a sample page", \
    "Ошибка: Текст должен совпадать."
print("Проверка пройдена.")

# пауза
time.sleep(2)

# переход на начальную вкладку
driver_chrome.switch_to.window(driver_chrome.window_handles[0])
print("Переход на начальную вкладку.")

# пауза
time.sleep(2)

# выбрать и нажать кнопку New Window
driver_chrome.find_element(By.ID, "windowButton").click()
print("Открыто новое окно.")

# пауза
time.sleep(2)

# переход на открытое окно
driver_chrome.switch_to.window(driver_chrome.window_handles[2])
print("Переход на открытое окно.")

# проверка присутствия в новом окне
value_text_in_window = driver_chrome.find_element(
    By.ID, "sampleHeading"
).text
assert value_text_in_window == "This is a sample page", \
    "Ошибка: Текст должен совпадать."
print("Проверка пройдена.")

# пауза
time.sleep(2)

# переход на начальную вкладку
driver_chrome.switch_to.window(driver_chrome.window_handles[0])
print("Переход на начальную вкладку.")

# пауза
time.sleep(2)

# закрыть браузер
driver_chrome.quit()
print("Браузер закрыт.")
