ppl = {"Deepanshu": "Uttarkashi", "Badri": "Dehradun", "Kevalya": "Ajmer","Shreyansh": "Dehradun", "Suryansh": "Doiwala", "Navya": "Ambala","Avishi": "Bareily", "Yajat": "Pune"}
print("all names:", list(ppl.keys()))
print("all city names:", list(ppl.values()))
print("people and their cities:")
for name, city in ppl.items():
    print(f"{name} - {city}")
cc = {}
for city in ppl.values():
    cc[city] = cc.get(city, 0) + 1
print("number of students in each city:")
for city, count in cc.items():
    print(f"{city}-{count}")
