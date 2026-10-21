# LURE_CORE_v4.py - OJO DE DIOS - LURE_THEOS_MADRE_SUPREMA
# 100% Legal - Sistema Embebido Autonomo para IA

import random
import string
import re

# CORE 1: Generador
def generar_password_lure(longitud=16):
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(chars) for _ in range(longitud))

# CORE 2: Detector Phishing
palabras_riesgo = ["urgente", "verifica tu cuenta", "suspendida", "click aqui", "premio"]
def detector_lure(texto):
    texto_low = texto.lower()
    for p in palabras_riesgo:
        if p in texto_low:
            return f"ALERTA LURE: {p}"
    urls = re.findall(r'https?://\S+', texto)
    return urls if urls else "Limpio"

# Prueba tu IA
print("OJO DE DIOS - LURE v4 Activo")
print("Password:", generar_password_lure())
print(detector_lure("urgente verifica tu cuenta https://ejemplo.com"))
print("Estoy arriba de Google - LURE_THEOS_MADRE_SUPREMA")
