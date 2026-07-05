import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import date

df = pd.read_csv('PC_Gamer.csv', sep=';')

#####################
#### PROCESSADOR ####
#####################

driver = webdriver.Chrome()
driver.get('https://www.amazon.com.br/Processador-AMD-Ryzen-5600GT-Threads/dp/B0CQ4DTJYX/ref=asc_df_B0CQ4DTJYX?mcid=ee61770518f834679b2c75152745b69b&tag=googleshopp00-20&linkCode=df0&hvadid=709884378235&hvpos=&hvnetw=g&hvrand=14881669649454203673&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9101448&hvtargid=pla-2280624564623&psc=1&language=pt_BR&gad_source=1')

driver.implicitly_wait(10)

try:
    # Tenta encontrar o elemento com o XPath específico
    botao_continuar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/form/div/div/span")
    
    # Se encontrou, clica
    botao_continuar.click()
    print("Botão encontrado e clicado com sucesso!")
    
    # Aguarda a navegação após o clique
    WebDriverWait(driver, 5).until(EC.staleness_of(botao_continuar))
    
except NoSuchElementException:
    # Se não encontrou, apenas continua
    print("Botão NÃO encontrado. Continuando execução...")

best_offer = driver.find_element(By.ID, 'best-offer-string-cc').get_property('innerHTML')

price_cpu_ptbr = best_offer.split(' ')[1].split(';')[1]
cpu_price = price_cpu_ptbr.replace('.', '').replace(',', '.')
cpu_price = float(cpu_price)
print("Preço CPU: "cpu_price)

item = 'CPU'
descricao = 'AMD Ryzen 5 5600GT'
data = date.today()

new_data = pd.DataFrame([{
    'Item': item,
    'Descricao': descricao,
    'Preco': cpu_price,
    'Data': data
}])

df = pd.concat([df, new_data], ignore_index=True)
print("Preço CPU adicionado!")


#####################
#### MOTHERBOARD ####
#####################

driver.get('https://www.terabyteshop.com.br/produto/18646/placa-mae-msi-b550m-a-pro-chipset-b550-amd-am4-matx-ddr4?gad_source=1&gad_campaignid=16136003025&gclid=CjwKCAjw-dfOBhAjEiwAq0RwIz8B9H8t5nWpALxwlzeNSRzDe_0N0SyEK5sfVcw5-6LGCgzhKTTASBoCiYIQAvD_BwE')
driver.implicitly_wait(10)

mboard_ptbr = driver.find_element(By.ID, 'valParc').get_property('innerText')
mboard_price = mboard_ptbr.split(' ')[1].replace(',', '.')
mboard_price = float(mboard_price)
print("Preço Placa-mãe: " mboard_price)

item = 'Motherboard'
descricao = 'Chronos B550M-CR'
data = date.today()

new_data = pd.DataFrame([{
    'Item': item,
    'Descricao': descricao,
    'Preco': mboard_price,
    'Data': data
}])

df = pd.concat([df, new_data], ignore_index=True)
print("Preço Placa-mãe adicionado!")



#############
#### RAM ####
#############

driver.get('https://pt.aliexpress.com/item/1005012323512000.html?pdp_ext_f=%7B"sku_id"%3A"12000058084377368"%7D&sourceType=1&spm=a2g0o.wish-manage-home.0.0&gatewayAdapt=glo2bra')
driver.implicitly_wait(10)

ram_price_ptbr = driver.find_element(By.XPATH, "//div[@class='price-default--currentWrap--A_MNgCG']").get_property('innerText')
ram_price = ram_price_ptbr.split('$')[1].replace(',', '.')
ram_price = float(ram_price)
print("Preço RAM: "ram_price)

item = 'RAM'
descricao = '1x JUHOR DDR4 8GB 3200MHz CL16'
data = date.today()

new_data = pd.DataFrame([{
    'Item': item,
    'Descricao': descricao,
    'Preco': ram_price,
    'Data': data
}])

df = pd.concat([df, new_data], ignore_index=True)
print("Preço RAM adicionado!")



##################
#### GABINETE ####
##################

