from datetime import datetime
import sys
#---------------------------------------
#File will get time about short stress test and return the exact GB to run
#the next stress test.
hours_stress = sys.argv[2]
#variables
file_stress = sys.argv[1]
file_short_stress = file_stress
with open(file_stress, "r") as file:
    first_line = file.readline()
    for last_line in file:
        pass

date_short_stress_ini = first_line[11:19]
date_short_stress_fin = last_line[11:19]

#--------------------------------------
#start of stress test
ini_shortstresstime = datetime.strptime(date_short_stress_ini, "%H:%M:%S")
#end of stress test
fin_shortstresstime = datetime.strptime(date_short_stress_fin, "%H:%M:%S")
#Gb ran short stress test
short_test_gb=15
#hours to large stress
large_test = int(hours_stress)
#---------------------------------------------
short_total_time = (fin_shortstresstime - ini_shortstresstime)

time_seconds_large = (large_test * 60) * 60

calculate_large_stress = time_seconds_large / short_total_time.total_seconds()

total = int(calculate_large_stress * short_test_gb)

print(f"{total}")


# print(f"\n {bcolors.WARNING}¿Deseas ejecutar el stress largo? {bcolors.ENDC}")
# opcion = input()
# if opcion == 'y' or opcion == 'yes' or opcion == 'YES' or opcion == 'Yes':
#     print("Corriendo stress...")

