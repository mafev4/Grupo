import matplotlib.pyplot as plt

prom_cp1 = df.filter(regex="CP1").iloc[:, 0].mean()
prom_nf  = df.filter(regex="NF").iloc[:, 0].mean()
prom_cp2 = df["CP2"].mean()
prom_cp3 = df["CP3"].mean()
plt.figure(figsize=(6,4))
plt.title("Promedios")
plt.bar(
    ["CP1", "CP2", "CP3", "NF"],
    [prom_cp1, prom_cp2, prom_cp3, prom_nf]
)

plt.ylabel("Promedio")
plt.xlabel("Calificaciones")
plt.show()