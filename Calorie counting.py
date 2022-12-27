
elf1_1 = int(input("elf 1 1st item calories: "))
elf1_2 = int(input("elf 1 2nd item calories: "))
elf1_3 = int(input("elf 1 3rd item calories: "))

elf1 = elf1_1 + elf1_2  + elf1_3
       
        
elf2 = int(input("elf2 item calories: "))
elf2 = elf2
        
elf3_1 = int(input("elf3 1st item calories: "))
elf3_2 = int(input("elf3 2nd item calories: "))
elf3 = elf3_1 + elf3_2
        
       
elf4_1 = int(input("elf4 1st item calories: "))
elf4_2 = int(input("elf4 2nd item calories: "))
elf4_3 = int(input("elf4 3rd item calories: "))
elf4 = elf4_1 + elf4_2 + elf4_3
        
        
elf5 = int(input("elf5 item calories: "))
sum_elf5 = elf5

print(elf1_1)
print(elf1_2)
print(elf1_3)
print("\n")
print(elf2)
print("\n")
print(elf3_1)
print(elf3_2)
print("\n")
print(elf4_1)
print(elf4_2)
print(elf4_3)
print("\n")
print(elf5)
print("\n")

        
#elf carrying the most calories
max_calories = (max(elf1, elf2, elf3, elf4, elf5))

string = ("Elf carrying the most calories has: ")
print (string , max_calories, )
