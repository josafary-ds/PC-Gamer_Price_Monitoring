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
print(f"Preço CPU: {cpu_price}")

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
print(f"Preço Placa-mãe: {mboard_price}")

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
#### SSD ####
#############

driver.get('https://pt.aliexpress.com/item/1005006783107881.html?sourceType=620&channel=coin&improveDiscount=Y&BuyNow=true&utm=iskandarsouzo_sophie&aff_fcid=776b93166200483383f7ee2b8c7a626b-1783267233933-06465-_c3nNHgTr&tt=API&aff_fsk=_c3nNHgTr&afSmartRedirect=y&dp=gx-br-aliexpress-aliexpress-cos&aff_fcid=158f311f0235481b9d6724a876e86c26-1783274078397-07732-_c3IGhl7b&tt=CPS_NORMAL&aff_fsk=_c3IGhl7b&aff_platform=portals-tool&sk=_c3IGhl7b&aff_trace_key=158f311f0235481b9d6724a876e86c26-1783274078397-07732-_c3IGhl7b&terminal_id=e7a44edf1bc34d368a13eb65be5c194e&afSmartRedirect=y')
driver.implicitly_wait(10)

button = driver.find_element(By.XPATH, "//div[@title='1TB']")
button.click()

ssd_price_ptbr = driver.find_element(By.XPATH, "//div[@class='price-default--currentWrap--A_MNgCG']").get_property('innerText')
ssd_price = ssd_price_ptbr.split('$')[1].replace(',', '.')
ssd_price = float(ssd_price)
print(f"Preço SSD: {ssd_price}")

item = 'SSD'
descricao = 'Movespeed ssd nvme 1TB'
data = date.today()

new_data = pd.DataFrame([{
    'Item': item,
    'Descricao': descricao,
    'Preco': ram_price,
    'Data': data
}])

df = pd.concat([df, new_data], ignore_index=True)
print("Preço SSD adicionado!")



#############
#### RAM ####
#############

driver.get('https://pt.aliexpress.com/item/1005012323512000.html?pdp_ext_f=%7B"sku_id"%3A"12000058084377368"%7D&sourceType=1&spm=a2g0o.wish-manage-home.0.0&gatewayAdapt=glo2bra')
driver.implicitly_wait(10)

ram_price_ptbr = driver.find_element(By.XPATH, "//div[@class='price-default--currentWrap--A_MNgCG']").get_property('innerText')
ram_price = ram_price_ptbr.split('$')[1].replace(',', '.')
ram_price = float(ram_price)
print(f"Preço RAM: {ram_price}")

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

driver.get('https://www.kabum.com.br/produto/887046/gabinete-gaming-c3tech-aquarius-com-vidro-temperado-sem-fonte-mt-g860bk-')
driver.implicitly_wait(10)

button = driver.find_element(By.ID, "adopt-accept-all-button")
button.click()

gabinete_ptbr = driver.find_element(By.XPATH, "(//div[@class='w-full']/span/b)").get_property('innerText')
gabinete_price = gabinete_ptbr.split('\xa0')[1].replace(',', '.')
gabinete_price = float(gabinete_price)
print(f"Preço Gabinete: {gabinete_price}")

item = 'Gabinete'
descricao = 'C3tech Aquarius'
data = date.today()

new_data = pd.DataFrame([{
    'Item': item,
    'Descricao': descricao,
    'Preco': gabinete_price,
    'Data': data
}])

df = pd.concat([df, new_data], ignore_index=True)
print("Preço Gabinete adicionado!")



###############
#### MOUSE ####
###############

driver.get('https://pt.aliexpress.com/item/1005012371400759.html?spm=a2g0o.productlist.main.23.459c25f81bcfCL&algo_pvid=fe26c5bb-67a9-42a2-8835-77951b1c0678&algo_exp_id=fe26c5bb-67a9-42a2-8835-77951b1c0678-20&pdp_ext_f=%7B"order"%3A"23"%2C"eval"%3A"1"%2C"fromPage"%3A"search"%7D&pdp_npi=6%40dis%21BRL%21336.34%21147.99%21%21%21407.73%21179.40%21%402101f70717832764055654429e72c1%2112000058191763437%21sea%21BR%217714416806%21X%211%210%21n_tag%3A-29911%3Bd%3A137eff22%3Bm03_new_user%3A-29895&curPageLogUid=Lq0Biyq3hzZX&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005012371400759%7C_p_origin_prod%3A')
driver.implicitly_wait(10)


mouse_ptbr = driver.find_element(By.XPATH, "(//div[@class='price-default--currentWrap--A_MNgCG'])").get_property('innerText')
mouse_price = mouse_ptbr.split('$')[1].replace(',', '.')
mouse_price = float(mouse_price)
print(f"Preço Mouse: {mouse_price}")

item = 'Mouse'
descricao = 'Attack Shark Wireless X11'
data = date.today()

new_data = pd.DataFrame([{
    'Item': item,
    'Descricao': descricao,
    'Preco': mouse_price,
    'Data': data
}])

df = pd.concat([df, new_data], ignore_index=True)
print("Preço Mouse adicionado!")



#################
#### HEADSET ####
#################

driver.get('https://pt.aliexpress.com/item/1005009495386384.html?aff_fcid=24cb7ac286da4a1dac72bd6b45a01629-1779218687223-01059-_c3gITj9D&tt=CPS_NORMAL&aff_fsk=_c3gITj9D&aff_platform=shareComponent-detail&sk=_c3gITj9D&aff_trace_key=24cb7ac286da4a1dac72bd6b45a01629-1779218687223-01059-_c3gITj9D&terminal_id=d874b61df0ea490bb40119dc36685fe8&afSmartRedirect=y')
driver.implicitly_wait(10)

button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[1]/div[1]/div[2]/div[8]/div/div/div[2]/div/div/div/div/div[5]')
button.click()

headset_ptbr = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[1]/div[1]/div[2]/div[4]/div/div[2]/div[1]/div[1]/span').get_property('innerText')
headset_price = headset_ptbr.split('$')[1].replace(',', '.')
headset_price = float(headset_price)
print(f"Preço Headset: {headset_price}")

item = 'Headset'
descricao = 'BINNUNE Bluetooth'
data = date.today()

new_data = pd.DataFrame([{
    'Item': item,
    'Descricao': descricao,
    'Preco': headset_price,
    'Data': data
}])

df = pd.concat([df, new_data], ignore_index=True)
print("Preço Headset adicionado!")



##################
#### SOUNDBAR ####
##################

driver.get('https://pt.aliexpress.com/item/1005006436035998.html?spm=a2g0o.productlist.main.2.26c7y0DSy0DSur&algo_pvid=a6a82e3c-ebe8-41ee-9da0-1fe9c6c92b4a&algo_exp_id=a6a82e3c-ebe8-41ee-9da0-1fe9c6c92b4a-1&pdp_ext_f=%7B"order"%3A"4969"%2C"spu_best_type"%3A"price"%2C"eval"%3A"1"%2C"fromPage"%3A"search"%7D&pdp_npi=6%40dis%21BRL%21229.12%21100.55%21%21%21287.08%21125.98%21%402103212b17798072772552193e62f7%2112000037173402947%21sea%21BR%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Aeaf596e%3Bm03_new_user%3A-29895%3BpisId%3A5000000207258923&curPageLogUid=jr5V9vRJV1Bl&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006436035998%7C_p_origin_prod%3A')
driver.implicitly_wait(10)

soundbar_ptbr = driver.find_element(By.XPATH, "(//div[@class='price-default--currentWrap--A_MNgCG'])").get_property('innerText')
soundbar_price = soundbar_ptbr.split('$')[1].replace(',', '.')
soundbar_price = float(soundbar_price)
print(f"Preço Soundbar: {soundbar_price}")

item = 'Soundbar'
descricao = 'NIYE V8'
data = date.today()

new_data = pd.DataFrame([{
    'Item': item,
    'Descricao': descricao,
    'Preco': soundbar_price,
    'Data': data
}])

df = pd.concat([df, new_data], ignore_index=True)
print("Preço Soundbar adicionado!")



#####################
#### SAVING DATA ####
#####################

df.to_csv('PC_Gamer.csv', sep=';', index=None)

driver.close()



#########################
#### GENERATING PLOT ####
#########################

itens = df.groupby('Item')

# Armazenar em dicionário
df_itens = {item: group.copy() for item, group in itens}

# Configurar estilo dos gráficos
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (12, 8)

# 1. Ler o arquivo CSV
df = pd.read_csv('PC_Gamer.csv', sep=';', encoding='utf-8-sig', parse_dates=['Data'])

print("Dados carregados:")
print(df.tail(10))
print(f"\nShape: {df.shape}")
print(f"Tipos de item únicos: {df['Item'].unique()}")

# 2. Agrupar por Item e armazenar em variáveis
# Criar um dicionário para armazenar os DataFrames de cada item
df_itens = {}

for item in df['Item'].unique():
    df_itens[item] = df[df['Item'] == item].copy()
    df_itens[item] = df_itens[item].sort_values('Data')  # Ordenar por data

# 3. Gráficos separados para cada item (subplots)
fig, axes = plt.subplots(4, 2, figsize=(15, 12))
axes = axes.flatten()

cores = ['black', 'blue', 'red', 'green', 'magenta', 'orange', 'darkviolet', 'firebrick']

for idx, (item, df_item) in enumerate(df_itens.items()):
    if idx < len(axes):
        cor = cores[idx % len(cores)]

        axes[idx].plot(df_item['Data'], df_item['Preco'], 
                       marker='o', 
                       linewidth=2, 
                       markersize=6,
                       color=cor)
        axes[idx].set_title(f'{item}', fontsize=12, fontweight='bold')
        axes[idx].set_xlabel('Data', fontsize=10)
        axes[idx].set_ylabel('Preço (R$)', fontsize=10)
        axes[idx].grid(True, alpha=0.3)
        axes[idx].tick_params(axis='x', rotation=30)

# Remover subplots vazios (se houver menos de 8 itens)
for idx in range(len(df_itens), len(axes)):
    fig.delaxes(axes[idx])

plt.tight_layout()

plt.savefig('plots/pcgamer_prices.png', dpi=300)

plt.show()