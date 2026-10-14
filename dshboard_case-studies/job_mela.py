def eligible(p):
    return p>=60

candidates = [
    ("Ahmed",86),
    ("Sara",72),
    ("Rahul",58),
    ("Ayesha",91),
    ("Sameer",67)
]

selected = [
    {
        "name": n,
        "percentage":p
    }
    for n, p in candidates if eligible(p)
]

selected = sorted(selected,key=lambda x:x["percentage"],reverse=True)

print("\n========================================")
print("          JOB MELA DASHBOARD")
print("========================================")
print("Total Candidates:", len(candidates))
print("Eligible:", len(selected))
for i,c in enumerate(selected,1):
    print(i,c["name"],"-",c["percentage"],"%")
print("========================================")