"""
EJERCICIO 14: ANALIZADOR DE CONTRASEÑAS
Escribe un programa que valide contraseñas según criterios:
- Mínimo 8 caracteres
- Al menos 1 mayúscula
- Al menos 1 minúscula
- Al menos 1 número
- Al menos 1 carácter especial (!@#$%^&*)
- No contiene espacios

El programa debe:
- Pedir contraseña y validar
- Mostrar qué criterios cumple y cuáles no
- Pedir cambios hasta que sea válida
- Permitir guardar múltiples contraseñas

Ejemplo:
  Introduce contraseña: abc

  Validación:
  ❌ Mínimo 8 caracteres (actual: 3)
  ❌ Al menos 1 mayúscula
  ✓ Al menos 1 minúscula
  ❌ Al menos 1 número
  ❌ Al menos 1 carácter especial

  Contraseña NO válida. Intenta de nuevo.

  Introduce contraseña: MiPass123!

  Validación:
  ✓ Mínimo 8 caracteres
  ✓ Al menos 1 mayúscula
  ✓ Al menos 1 minúscula
  ✓ Al menos 1 número
  ✓ Al menos 1 carácter especial

  ✓ Contraseña válida!
"""
