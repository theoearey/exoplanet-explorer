import pandas as pd
import matplotlib.pyplot as plt

# Traer los datos de exoplanetas desde NASA
url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_rade,pl_bmasse,pl_dens,pl_orbper+from+pscomppars&format=csv"
df = pd.read_csv(url)

# Reviso las primeras filas
print(df.head())

# Reviso cuántas filas y columnas hay
print(df.shape)

# Reviso cuántos datos faltan en cada variable
print(df.isna().sum())

# Elimino los planetas que no tienen radio, masa o densidad
df_complete = df.dropna(subset=["pl_rade", "pl_bmasse", "pl_dens"]).copy()

# Comparo el dataset original con el limpio
print("Dataset original:", df.shape)
print("Dataset completo:", df_complete.shape)

# Reviso las estadísticas principales
print(df_complete[["pl_rade", "pl_bmasse", "pl_dens"]].describe())

# Grafico masa contra radio
plt.scatter(df_complete["pl_rade"], df_complete["pl_bmasse"])
plt.xlabel("Radio (radios terrestres)")
plt.ylabel("Masa (masas terrestres)")
plt.title("Masa vs radio")

plt.savefig("figures/masa_vs_radio.png")
plt.show()

# Grafico densidad contra radio
plt.scatter(df_complete["pl_rade"], df_complete["pl_dens"])
plt.xlabel("Radio (radios terrestres)")
plt.ylabel("Densidad")
plt.title("Densidad vs radio")

plt.savefig("figures/densidad_vs_radio.png")
plt.show()

# Creo un dataset con periodo orbital y densidad disponibles
df_orbit = df.dropna(subset=["pl_orbper", "pl_dens"])

# Grafico densidad contra periodo orbital
plt.scatter(df_orbit["pl_orbper"], df_orbit["pl_dens"])
plt.xlabel("Periodo orbital (días)")
plt.ylabel("Densidad")
plt.title("Densidad vs periodo orbital")

plt.savefig("figures/densidad_vs_orbital.png")
plt.show()

# Gráficos con escala logarítmica
# Grafico masa contra radio con escala logarítmica
plt.scatter(df_complete["pl_rade"], df_complete["pl_bmasse"])
plt.xscale("log")
plt.yscale("log")

plt.xlabel("Radio (radios terrestres)")
plt.ylabel("Masa (masas terrestres)")
plt.title("Masa vs radio (escala logarítmica)")

plt.savefig("figures/masa_vs_radio_log.png")
plt.show()

# Grafico densidad contra radio con escala logarítmica
plt.scatter(df_complete["pl_rade"], df_complete["pl_dens"])
plt.xscale("log")
plt.yscale("log")

plt.xlabel("Radio (radios terrestres)")
plt.ylabel("Densidad")
plt.title("Densidad vs radio (escala logarítmica)")

plt.savefig("figures/densidad_vs_radio_log.png")
plt.show()

# Grafico densidad contra periodo orbital con escala logarítmica
plt.scatter(df_orbit["pl_orbper"], df_orbit["pl_dens"])
plt.xscale("log")
plt.yscale("log")

plt.xlabel("Periodo orbital (días)")
plt.ylabel("Densidad")
plt.title("Densidad vs periodo orbital (escala logarítmica)")

plt.savefig("figures/densidad_vs_orbital_log.png")
plt.show()

##Correlaciones

variables_numericas = ["pl_rade","pl_bmasse","pl_dens","pl_orbper"]

# Correlación Pearson
pearson_corr = df_complete[variables_numericas].corr(method="pearson")
print("\nCORRELACIÓN PEARSON")
print(pearson_corr)

# Correlación Spearman
spearman_corr = df_complete[variables_numericas].corr(method="spearman")

print("\nCORRELACIÓN SPEARMAN")
print(spearman_corr)

# Correlación Kendall
kendall_corr = df_complete[variables_numericas].corr(method="kendall")

print("\nCORRELACIÓN KENDALL")
print(kendall_corr)

# CORRELACIONES ESPECÍFICAS
print("\nCORRELACIONES ESPECÍFICAS")
print("Masa - Radio:",df_complete["pl_bmasse"].corr(df_complete["pl_rade"],method="spearman"))
print("Densidad - Radio:",df_complete["pl_dens"].corr(df_complete["pl_rade"],method="spearman"))
print("Densidad - Periodo orbital:",df_complete["pl_dens"].corr(df_complete["pl_orbper"],method="spearman"))

# OUTLIERS CON IQR

# Calcular rango intercuartil (IQR) para la densidad
Q1 = df_complete["pl_dens"].quantile(0.25)
Q3 = df_complete["pl_dens"].quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Detectar densidades atípicas
outliers_densidad = df_complete[(df_complete["pl_dens"] < limite_inferior)| (df_complete["pl_dens"] > limite_superior)]

print("\nOUTLIERS DE DENSIDAD")
print(outliers_densidad[["pl_name","pl_rade","pl_bmasse","pl_dens","pl_orbper"]].sort_values("pl_dens",ascending=False).head(20))

print("\nNúmero de outliers de densidad:")
print(len(outliers_densidad))

# Calcular densidad a partir de masa y radio
df_complete["pl_dens_calculada"] = 5.514 * (df_complete["pl_bmasse"] / (df_complete["pl_rade"] ** 3))

#Comparar densidad calculada con densidad reportada
plt.scatter(df_complete["pl_dens"], df_complete["pl_dens_calculada"])
plt.xlabel("Densidad reportada")
plt.ylabel("Densidad calculada")
plt.title("Densidad reportada vs densidad calculada")

plt.savefig("figures/densidad_reportada_vs_calculada.png")
plt.show()

# Comparar densidad calculada con densidad reportada en escala logarítmica
dens_radio = df_complete["pl_dens"] / df_complete["pl_dens_calculada"]

# Grafico densidad reportada vs densidad calculada en escala logarítmica
plt.scatter(df_complete["pl_dens"], df_complete["pl_dens_calculada"])
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Densidad reportada")
plt.ylabel("Densidad calculada")
plt.title("Densidad reportada vs densidad calculada (escala logarítmica)")

plt.savefig("figures/densidad_reportada_vs_calculada_log.png")
plt.show()

#Guardar la proporción como una nueva columna en el dataset
df_complete["dens_radio"] = dens_radio

#Filtrar los planetas donde la densidad reportada es absurdamente mayor que la densidad calculada (dens_radio > 3 veces) o absurdamente menor (dens_radio < 0.3 veces) a la densidad que su masa y radio deberían indicar
df_filtered = df_complete[(df_complete["dens_radio"] > 3) | (df_complete["dens_radio"] < 0.3)]

#Ordenar para ver los casos más extremos
df_filtered_sorted = df_filtered.sort_values("dens_radio",ascending=False)

print("\n--- ANOMALÍAS (3x o 0.3x) ---")
print(df_filtered_sorted[["pl_name", "pl_rade", "pl_bmasse", "pl_dens", "dens_radio"]].head(15))

#Filtrar los planetas donde la densidad reportada es absurdamente mayor que la densidad calculada (dens_radio > 10 veces) o absurdamente menor (dens_radio < 0.1 veces) a la densidad que su masa y radio deberían indicar
df_filtered_10x = df_complete[(df_complete["dens_radio"] > 10) | (df_complete["dens_radio"] < 0.1)]

#Ordenar para ver los casos más extremos em eñ casp de dens_radio > 10 o < 0.1
df_filtered_10x_sorted = df_filtered_10x.sort_values("dens_radio",ascending=False)

print("\n--- ANOMALÍAS EXTREMAS (10x o 0.1x) ---")
print(df_filtered_10x_sorted[["pl_name", "pl_rade", "pl_bmasse", "pl_dens", "dens_radio"]].head(15))

# Exportar el resultado físico a un archivo CSV
df_filtered_10x_sorted.to_csv("planetas_anomalos.csv", index=False)

# Mensaje final en consola
print("\n=== CONCLUSIÓN DEL PROYECTO 1 ===")
print("Los hallazgos confirman la hipótesis: los outliers más extremos no son exoplanetas súper densos,")
print("sino anomalías de catálogo donde las mediciones multivariables no tienen sentido astrofísico.")
print("Los casos identificados fueron exportados a 'planetas_anomalos.csv'.")