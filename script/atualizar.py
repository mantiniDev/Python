import time
from selenium import webdriver

# Iniciar uma instância do ChromeDriver
driver = webdriver.Chrome('E:/chromedriver')

# Navegar para a página que deseja atualizar
driver.get('https://creditasscd.securities.com.br/creditasscd/queue/7')

# Definir um loop para atualizar a página de 5 em 5 segundos
while True:
    driver.refresh()
    time.sleep(5)

# Fechar o navegador quando o script for finalizado
driver.quit()
