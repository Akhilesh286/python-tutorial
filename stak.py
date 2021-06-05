# back
i = 1
limit = int(input("c:")).lower()
browsing_session =[]
while i <limit:
    browsing_session.append(input(">"))
    i += 1
print (browsing_session)
back = input("c -:")
if back == "back":
    last = browsing_session.pop()
# print(last)
for i in browsing_session :
    print(i)
# print("redirect", browsing_session)
