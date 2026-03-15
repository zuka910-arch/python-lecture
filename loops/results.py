results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")


results.append(["Bowser", "Donkey Kong"])
results.remove(["Bowser", "Donkey Kong"])
results.extend(["Bowser", "Donkey Kong"])

print(results)


results.remove("Bowser")  
results.insert(0, "Bowser")
print(results)

print(results.index("Mario"))

results.reverse()
print(results)