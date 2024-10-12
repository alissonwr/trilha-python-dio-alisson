# from datetime import date, datetime, timedelta

# tipo_carro = "M"  # P, M, G
# tempo_pequeno = 30
# tempo_medio = 45
# tempo_grande = 60
# data_atual = datetime.now()

# if tipo_carro == "P":
#     data_estimada = data_atual - timedelta(days=tempo_pequeno)
#     print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
# elif tipo_carro == "M":
#     data_estimada = data_atual - timedelta(days=tempo_medio)
#     print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
# else:
#     data_estimada = data_atual - timedelta(days=tempo_grande)
#     print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


# print(date.today() - timedelta(days=1))

# resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
# print(resultado.time())

# print(datetime.now().date())

from datetime import datetime, timedelta

tipo_carro = "M"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()
print(data_atual)

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"""
    ====================================================
    Data e hora de entrada: {data_atual}\n
    Data e hora de saída: {data_estimada}
    ====================================================
    """)
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes = tempo_medio)    
    print(f"""
    ====================================================
    Data e hora de entrada: {data_atual}\n
    Data e hora de saída: {data_estimada}
    ====================================================
    """)
else:
    data_estimada = data_atual + timedelta(minutes = 60)
    print(f"""
    ====================================================
    Data e hora de entrada: {data_atual}\n
    Data e hora de saída: {data_estimada}
    ====================================================
    """)