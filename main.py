from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opcoes = Options()
opcoes.add_experimental_option("detach", True)

navegador = webdriver.Chrome(options=opcoes)
 #maximiza a tela
navegador.maximize_window()
 #abre o youtube
navegador.get("https://www.youtube.com")
 #essa variavel espera 5 segundos até  barra de pesquisa aparecer
barrinha_de_pesquisa = WebDriverWait(navegador,5).until(EC.presence_of_element_located((By.NAME, 'search_query')))
 #pesquisa pela palavra digitada
barrinha_de_pesquisa.send_keys("blue bird")
 #procura pelo botao da lupa
botao_da_lupa = WebDriverWait(navegador,10).until(EC.presence_of_element_located((By.XPATH ,'//*[@id="search-icon-legacy"]')))
 #clica no botao da lupa
botao_da_lupa.click()

nome_do_video = "Naruto Shippuden Opening 3 | Blue Bird (HD)"

lista_de_videos = WebDriverWait(navegador,5).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@id="video-title"]')))

for titulo_do_video in lista_de_videos:
    if nome_do_video.lower() in titulo_do_video.get_attribute("title").lower():
        titulo_do_video.click()


