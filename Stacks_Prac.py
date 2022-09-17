#Stacks 
# LIFO - Last in first out

browsing = []
browsing.append(1)
browsing.append(2)
browsing.append(3)
print(browsing)
last = browsing.pop()
print(last)
print(browsing)
if not browsing:
    print(browsing[-1])