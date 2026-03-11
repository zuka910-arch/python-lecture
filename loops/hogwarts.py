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



for student in students:

     # ვერსია 1
    #print(student, ",", " ",  students[student], sep="")

        # ვერსია 2 იგივეა როგოც ვერსია 1 მაგრამ უფრო მარტივი   
    print(student, students[student], sep=", ")