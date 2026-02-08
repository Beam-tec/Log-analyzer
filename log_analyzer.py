from collections import Counter

logfile = "sample.log"
ip_counter = Counter()

with open(logfile, "r", encoding="utf=8") as f:
    for line in f:
        if "Failed password" in line:
            ip = line.split()[5]
            ip_counter[ip] += 1

print("Verdächtige IP Sofortige Überprüfung Nötig!!!! Mehr oder Genau 2 mal Fehlgeschlagener Login versuch :")
for ip, c in ip_counter.items():
    if c >= 2:
        print(ip, c)