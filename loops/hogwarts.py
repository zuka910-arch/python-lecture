#students = ["Hermione", "Harry", "Ron", "draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#for i in range(len(students)):
#    print(f"{students[i]} is in {houses[i]}")




students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

#print(students["Hermione"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])



#for student in students:

     # ვერსია 1
    #print(student, ",", " ",  students[student], sep="")

        # ვერსია 2 იგივეა როგოც ვერსია 1 მაგრამ უფრო მარტივი   
    #print(student, students[student], sep=", ")




#for k, v in students.items():
#    print(k,v, sep=", ")



"""

| #      |  name        |  house      | patronus  |
---------------------------------------------------
| 0      | Hermione     | Gryffindor  | Otter     |
| 1      | Harry        | Gryffindor  | Stag      |

"""



students = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor" , "patronus" : "Jack Russell Terrier"},
    {"name" : "Draco","house" : "Slytherin", "patronus" : "None"}
]

#for student in students:
#    print(student["name"], student["house"], student["patronus"], sep=", ")

for student in students:
    if student["house"] == "Gryffindor":
        print(student["name"], student["house"], student["patronus"], sep=", ")

        