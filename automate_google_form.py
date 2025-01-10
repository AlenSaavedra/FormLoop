from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Usar ChromeDriverManager para manejar el controlador de Chrome
def complete_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    actions = ActionChains(driver)

    # Enlace del formulario
    link = "https://docs.google.com/forms/d/e/1FAIpQLSd3NQLdHSV3cgaAdd0fVH-mOqjKF-dc21kQTnQGva3E2MPtug/viewform"

    # Respuestas
    rsp = [
        "Satisfecho",  # Pregunta 1
        "A veces",  # Pregunta 2
        "De acuerdo",  # Pregunta 3
        "Muy fácil",  # Pregunta 4
        "Sí, son rápidos",  # Pregunta 5
        "Sí, definitivamente",  # Pregunta 6
        "Satisfecho",  # Pregunta 7
        "Muy eficientes",  # Pregunta 8
        "Sí",  # Pregunta 9
        "Reducción en tiempos de respuesta",  # Pregunta 10
        "Escuchar mejor mis necesidades.",  # Pregunta 11
    ]

    # Abre el enlace del formulario
    driver.get(link)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "form"))
    )
    print("Formulario cargado correctamente.")

    # Responder las preguntas de forma robusta
    questions = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//div[contains(@role, "listitem")]')
        )
    )

    for i, respuesta in enumerate(rsp):
        try:
            if i < len(questions):
                question_element = questions[i].find_element(
                    By.XPATH, f".//div[@aria-label='{respuesta}']"
                )
                driver.execute_script(
                    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                    question_element,
                )
                time.sleep(0.5)  # Pausa breve para asegurar la visibilidad
                question_element.click()
                print(f"Pregunta {i + 1} respondida: {respuesta}")
                time.sleep(1)
            else:
                print(f"Pregunta {i + 1} no encontrada.")
        except Exception as e:
            print(f"Error al responder la pregunta {i + 1}: {respuesta}. Detalles: {e}")

    # Enviar formulario
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Enviar"]'))
        )
        submit_button.click()
        print("Formulario enviado.")
    except Exception as e:
        print(f"Error al intentar enviar el formulario: {e}")

    # Espera la confirmación de envío
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fHUPb"))
        )
        print("Confirmación de envío detectada.")
    except Exception as e:
        print(f"Error al detectar confirmación de envío: {e}")

    # Cierra el navegador
    driver.quit()


# Ejecutar el proceso 10 veces
for i in range(10):
    print(f"Ejecutando formulario {i + 1}/10")
    complete_form()
    time.sleep(2)  # Pausa opcional entre ejecuciones
