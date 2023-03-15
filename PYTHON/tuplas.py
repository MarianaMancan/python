times = ("Corinthians", "Palmeiras", "Santos", "Gremio",
         "cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atlético",
         "Botafogo", "Atlético-PR", "Bahia", "São paulo", "Fluminense",
         "SportRecife", "EC Vitoria", "Coritiba", "Avai", "Ponte Petra",
         "Atlético-GO")
print("-="*15)
print(f"lista de times: {times}")
print("-="*15)
print(f"Os cincos primeiros são{times[0:5]}")
print("-="*15)
print(f"Os quatro ultimos são{times[-4:]}")
print("-="*15)
print(f"Time em ordem alfabética: {sorted(times)}")
print("-="*15)
print(f'O Chapeconese está na {times.index("Chapecoense")+1} posição')
print("-="*15)
