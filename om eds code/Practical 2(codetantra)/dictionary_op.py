# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}


print("Original Dictionary:",student)

key = int(input())
value = input()
student[key] = value
print("After Insertion:",student)

update_key = int(input())
new_value= input()
if update_key in student:
	student[update_key] = new_value
print("After Update:",student)

delete_key = int(input())
if delete_key in student:
	del student[delete_key]
print("After Deletion:",student)

print("Traversing Dictionary:")
for k, v in student.items():
	print(f"{k} : {v}")