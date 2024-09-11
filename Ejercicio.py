diccionario = {
    "maximo":7,
    "minimo":2.5,
    "promedio":4,
    "dalton":1.5
}

porcentaje_max=diccionario["maximo"]-diccionario["dalton"]
porcentaje_max=round(porcentaje_max*100/7,2)
porcentaje_min=diccionario["minimo"]-diccionario["dalton"]
porcentaje_min=round(porcentaje_min*100/2.5,2)
porcentaje_promedio=diccionario["promedio"]-diccionario["dalton"]
porcentaje_promedio=round(porcentaje_promedio*100/4,2)
print(f"{porcentaje_max} %") 
print(f"{porcentaje_min} %") 
print(f"{porcentaje_promedio} %") 
