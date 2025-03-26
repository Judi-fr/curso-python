# Orden de precedencia de operadores

# 1. Paréntesis
# 2. Operaciones aritméticas
#      a) paréntesis
#      b) exponentes (potencias y raíces)
#      c) multiplicación y división
#      d) suma y resta
# 3. Operaciones de comparación
# 4. Operaciones lógicas

ejemplo = 2**3 > 4 or 3 == 3 and 20 > 3 + 1 * 2
#       (2**3 > 4) or (3 == 3) and (20 > 3 + 1 * 2)
#          (8 > 4) or (3 == 3) and (20 > 5)
#             True or True     and True
#             True             and True
#                                  True
print(ejemplo)
