from GBP import GBP

print("Data\t\tKurs\t")
print("==========================") 


for x in GBP["rates"]:
    print(x["effectiveDate"],"\t",x["mid"])



