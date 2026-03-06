#Creat Dict of 2025 movies

movises_db={}

cast_Chhaava=["Vicky Kaushal","Rashmika Mandanna","Akshaye Khanna","Ashutosh Rana","Divya Dutta"]
cast_Dhurandhar=["Ranveer Singh","Akshaye Khanna","R. Madhavan","Sanjay Dutt","Arjun Rampal","Sara Arjun"]
cast_Animal=["Ranbir Kapoor","Rashmika Mandanna","Anil Kapoor","Bobby Deol","Triptii Dimri"]
cast_Pushpa1=["Allu Arjun","Rashmika Mandanna","Fahadh Faasil"]
cast_Pushpa2=["Allu Arjun","Rashmika Mandanna","Fahadh Faasil"]

movises_db["Chhaava"]=cast_Chhaava
movises_db["Dhurandhar"]=cast_Dhurandhar
movises_db["Animal"]=cast_Animal
movises_db["Pushpa1"]=cast_Pushpa1
movises_db["Pushpa2"]=cast_Pushpa2

for i in movises_db.keys():
    print(i)
'''
Chhaava
Dhurandhar
Animal
Pushpa1
Pushpa2'''


for i in movises_db.values():
    print(i)
    
'''
['Vicky Kaushal', 'Rashmika Mandanna', 'Akshaye Khanna', 'Ashutosh Rana', 'Divya Dutta']
['Ranveer Singh', 'Akshaye Khanna', 'R. Madhavan', 'Sanjay Dutt', 'Arjun Rampal', 'Sara Arjun']
['Ranbir Kapoor', 'Rashmika Mandanna', 'Anil Kapoor', 'Bobby Deol', 'Triptii Dimri']
['Allu Arjun', 'Rashmika Mandanna', 'Fahadh Faasil']
['Allu Arjun', 'Rashmika Mandanna', 'Fahadh Faasil']
'''

count=0
for k,v in movises_db.items():
    for n in v:
        if n=="Rashmika Mandanna":
            count=count+1
            print(k)
print(count)
'''
Chhaava
Animal
Pushpa1
Pushpa2
4'''
