garbage = ["G", "P", "GP", "GG"]
travel = [2, 4, 3]

time = 0

dict = {"Mhouse": [], "Ghouse": [], "Phouse": []}

for i in range(len(garbage)):
    if "G" in garbage[i]:
        dict["Ghouse"].append(i)
        time += garbage[i].count("G")
    if "P" in garbage[i]:
        dict["Phouse"].append(i)
        time += garbage[i].count("P")
    if "M" in garbage[i]:
        dict["Mhouse"].append(i)
        time += garbage[i].count("M")

dict["Ghouse"].insert(0, 0)
dict["Phouse"].insert(0, 0)
dict["Mhouse"].insert(0, 0)

for i in range(len(dict["Ghouse"]) - 1):
    time += sum(travel[dict["Ghouse"][i] : dict["Ghouse"][i + 1]])
for i in range(len(dict["Phouse"]) - 1):
    time += sum(travel[dict["Phouse"][i] : dict["Phouse"][i + 1]])
for i in range(len(dict["Mhouse"]) - 1):
    time += sum(travel[dict["Mhouse"][i] : dict["Mhouse"][i + 1]])

print(time)
