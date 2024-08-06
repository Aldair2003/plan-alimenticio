def obtener_plan_alimenticio(peso_actual, horas_ejercicio, objetivo, peso_ideal, compromiso):
    # Lógica para determinar el plan adecuado
    if objetivo == 'estetico' and horas_ejercicio >= 1 and compromiso == 'si':
        return plan_estetico_intenso
    elif objetivo == 'salud' and peso_actual > peso_ideal:
        return plan_perdida_peso
    else:
        return plan_mantenimiento

plan_estetico_intenso = {
    "lunes": "Desayuno: Avena con frutas, Almuerzo: Pechuga de pollo con ensalada, Cena: Pescado a la plancha con vegetales",
    # ... resto de los días
}

plan_perdida_peso = {
    "lunes": "Desayuno: Yogur con frutas, Almuerzo: Ensalada de atún, Cena: Sopa de verduras",
    # ... resto de los días
}

plan_mantenimiento = {
    "lunes": "Desayuno: Tostadas integrales con aguacate, Almuerzo: Pasta integral con verduras, Cena: Tortilla de espinacas",
    # ... resto de los días
}