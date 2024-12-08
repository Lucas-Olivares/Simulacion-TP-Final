import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

rho = 3.0106738081537108
loc = 0.008255337453217455
scale =  0.0007142788694762647

rho1 = 0.9618524191017109
loc1 = 17.809999999999988
scale1 = 1.6081049079194703

rho2 = 0.6936590930006306
loc2 = 0.27999999999999997
scale2 =  0.305533495938078

rho3 = 0.9591453958445508
loc3 = 9.314539233403671
scale3 =  63.452762988449166

# datos mortalidad
f_verif = stats.dweibull.rvs(rho, loc, scale, size=4000, random_state=None)
# datos natalidad
f1_verif = stats.rel_breitwigner.rvs(rho1, loc1, scale1, size=4000, random_state=None)
# datos casos graves de dengue
f2_verif = stats.weibull_min.rvs(rho2, loc2, scale2, size=4000, random_state=None)
# datos muertes por dengue
f3_verif = stats.weibull_max.rvs(rho3, loc3, scale3, size=4000, random_state=None)

# VARIABLES DE CONTROL
PI = 46000000 # poblacion inicial
TV = 0        # tasa de vacunacion anual


while True:
    try:
        PI = int(input("Poblacion inicial (PI): "))
        TV = int(input("Tasa de vacunacion anual (TV): "))
        break
    except ValueError:
        print("\nError: Solo se permiten números enteros.\n")
        continue

# VARIABLES DE RESULTADO
PCG = 0 # porcentaje de años en los que la tasa de casos graves supera el 0.2%
PM = 0  # porcentaje de las muertes causadas por dengue en relacion con las muertes totales
MM = 0  # maxima cantidad anual de muertes por dengue


T=2014
TF=2114 # 100 años de simulación





def main():
    print("\n\n### Comenzando simulacion ###\n\n")
    simular()
    print("\n ------------ Fin simulación ------------")

if __name__ == "__main__":
    main()