import csv

titles = set()      # to store only unique value
storage1 = list()

with open("creditRisk.csv", "r") as file:
	reader = csv.DictReader(file)
	for row in reader:
		storage1.append(row["Property_Area"])
i = 0
a = 0
b = 0
c = 0		
for title in storage1:
	i += 1
	if title == 'Urban':
		a+=1
	elif title == 'Rural':
		b+=1
	else:
		c+=1

print("Urban: " + str(a)+ "   (" + str((a/i)*100) + "%)")
print("Semiurban: " + str(c) + "   (" + str((c/i)*100) + "%)")
print("Rural: " + str(b) + "   (" + str((b/i)*100) + "%)")
print("Total: " + str(i) + "   (100%)")
