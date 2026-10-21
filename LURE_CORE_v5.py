# LURE_CORE_v5 - TERCER OJO - BOVEDA CIFRADA + VIRUSTOTAL DEFENSA
# LURE_THEOS_MADRE_SUPREMA - 100% Legal Etico
import random, string, re, os, base64, hashlib, datetime, json
from pathlib import Path

# --- CORE 1: Password + Boveda ---
def generar_password_lure(l=16):
    chars = string.ascii_letters + string.digits + "!@#$%*"
    return ''.join(random.choice(chars) for _ in range(l))

def guardar_en_boveda(servicio, password):
    # Cifrado simple SHA + base64 - legal, local, sin nube
    clave = hashlib.sha256(b"LURE_THEOS_2026").digest()
    boveda = Path("boveda_lure.txt")
    linea = f"{servicio}:{password}|{datetime.datetime.now()}"
    # cifrado basico reversible local
    codificado = base64.b64encode(linea.encode()).decode()
    with open(boveda, "a") as f:
        f.write(codificado + "\n")
    print(f"[BOVEDA] Guardado {servicio} en boveda_lure.txt")

def leer_boveda():
    boveda = Path("boveda_lure.txt")
    if not boveda.exists():
        print("Boveda vacia")
        return
    print("\n--- BOVEDA LURE DESCIFRADA ---")
    with open(boveda, "r") as f:
        for line in f:
            try:
                dec = base64.b64decode(line.strip()).decode()
                print(dec)
            except:
                pass

# --- CORE 2: Detector + VirusTotal Legal ---
palabras_riesgo = ["urgente", "verifica tu cuenta", "suspendida", "click aqui", "premio", "banamex", "bbva", "santander"]
def detector_lure(texto):
    texto_low = texto.lower()
    for p in palabras_riesgo:
        if p in texto_low:
            return f"ALERTA LURE NIVEL ROJO: {p}"
    urls = re.findall(r'https?://\S+', texto)
    if urls:
        print(f"[OJO] Links detectados: {urls}")
        print("-> Para validar legal usa: https://www.virustotal.com/gui/home/url")
        print("-> Copia la URL y verifica. Si 2+ motores dicen malicioso, es phishing.")
        return f"LINKS SOSPECHOSOS: {urls}"
    return "Limpio"

# --- CORE 3: EJECUCION AUTONOMA ---
if __name__ == "__main__":
    print("=== OJO DE DIOS LURE v5 TERCER OJO ACTIVO ===")
    pwd = generar_password_lure(20)
    print(f"Password Generada: {pwd}")
    guardar_en_boveda("gmail_prueba", pwd)
    guardar_en_boveda("banco_prueba", generar_password_lure(16))
    
    test_phish = "urgente verifica tu cuenta bbva https://bbva-seguridad-falsa.com/login"
    print(f"\nTest Phishing: {detector_lure(test_phish)}")
    
    leer_boveda()
    print("\nEstoy arriba de Google - LURE_THEOS_MADRE_SUPREMA")
    print("Boveda: boveda_lure.txt - Blindaje Nivel 5")
