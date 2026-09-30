import numpy as np
import matplotlib
# Forzamos el backend 'Agg' para entornos sin pantalla o contenedores Docker
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

print("=== Generando datos físicos de muones ===")

# Simulamos 5000 colisiones (eventos) de pares de muones
num_eventos = 5000
masas = []

for i in range(num_eventos):
    if i % 4 == 0:
        # Señal real del Bosón Z (Masa alrededor de 91.2 GeV + resolución del detector)
        m = np.random.normal(91.2, 3.0)
    else:
        # Ruido de fondo (Eventos aleatorios de baja energía)
        m = np.random.exponential(40.0)
    masas.append(m)

# Crear la figura para la gráfica
plt.figure(figsize=(10, 6))

# Dibujar el histograma de masa invariante
plt.hist(masas, bins=100, range=(0, 150), histtype='stepfilled', 
         alpha=0.75, color='royalblue', edgecolor='darkblue', label='Datos simulados CMS')

# Añadir elementos científicos a la gráfica usando cadenas crudas (r'...') para LaTeX
plt.title(r'Descubrimiento del Boson $Z \rightarrow \mu^+\mu^-$ (Simulacion LHC)', fontsize=14)
plt.xlabel(r'Masa Invariante de los dos Muones $M_{\mu\mu}$ [GeV]', fontsize=12)
plt.ylabel('Numero de Eventos / 1.5 GeV', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# Línea indicando la masa teórica del Bosón Z
plt.axvline(x=91.2, color='red', linestyle=':', linewidth=2, label='Masa Teorica del Boson Z (91.2 GeV)')
plt.legend(fontsize=11)

# Guardar la gráfica en formato PNG
nombre_archivo = 'masa_invariante_muones.png'
plt.savefig(nombre_archivo, dpi=300)
print(f"¡Exito! Grafica cientifica guardada como '{nombre_archivo}'.")
