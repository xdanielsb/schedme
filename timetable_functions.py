# activités proposées: piano, guitare, tennis (for example)

from random import choice, randint, choices
import datetime

activities = ["piano","guitar","tennis"]
teacher_names = ["John","Maria","Peter","Martin","Rick"]
student_names = ["Paul","Jessy","Harry","Joy","Fatima","Mickael","Lucy"]

def parse_datetime(date_string, time_string): # format attendu: "DD/MM/YYYY HH:MM"
    return datetime.datetime.strptime(date_string+" "+time_string, "%d/%m/%Y %H:%M")

def generate_proposal(activity, beginning, end):
    return {"activity":activity, "beginning":beginning, "end":end}

def generate_random_proposals(number):
    retured_list = []
    for i in range(number):
        activity = choice(activities)
        beginning_time = randint(8,17)
        beginning = datetime.datetime(2021,1,19,beginning_time)
        end = beginning+datetime.timedelta(hours=2)
        proposal = generate_proposal(activity, beginning, end)
        retured_list.append(proposal)
    return retured_list

def generate_random_teacher(id):
    dict_id = "p"+str(id)
    name = choice(teacher_names)
    proposals = generate_random_proposals(3)
    return {"id":dict_id, "name":name, "proposals":proposals}

def generate_random_teachers(number):
    teacher_list = []
    for i in range(number):
        teacher_list.append(generate_random_teacher(i))
    return teacher_list

#Elèves

beginning_time = randint(8,17)
beginning = datetime.datetime(2021,1,19,beginning_time)
end = beginning+datetime.timedelta(hours=2)

slot1 = {"beginning":beginning, "end":end}

def generate_slot(beginning, end):
    return {"beginning":beginning, "end":end}

def generate_random_slots(number):
    retured_list = []
    for i in range(number):
        beginning_time = randint(8,17)
        beginning = datetime.datetime(2021,1,19,beginning_time)
        end = beginning+datetime.timedelta(hours=2)
        slot = generate_slot(beginning, end)
        retured_list.append(slot)
    return retured_list

def generate_student(id, name, likings, slots):
    return {"id":id, "name": name, "likings":likings, "slots":slots}

def generate_random_student(id):
    dict_id = "s"+str(id)
    name = choice(student_names)
    likings = choices(activities, k=2)
    return {"id":dict_id, "name":name, "likings":likings, "slots":generate_random_slots(2)}

def generate_random_students(number):
    student_list = []
    for i in range(number):
        student_list.append(generate_random_student(i))
    return student_list

"""def is_free(teacher,student):
    for proposal in teacher["proposals"]:"""

def is_free_time(teacher_proposal,student_slot):
    return student_slot["beginning"] <= teacher_proposal["beginning"] and student_slot["end"] >= teacher_proposal["end"]

"""def is_free_student(teacher_proposal,student):
    for student_slot in student["slots"]:
        if is_free_time(teacher_proposal,student_slot) and teacher_proposal["activity"] in student["likings"]:
            return True
    return False"""

# fonctions auxiliaires pour + de lisibilité dans les tests

def slots_to_string(slots):
    total_string = ""
    for slot in slots:
        total_string+=str(slot)+"\n"
    return total_string

def print_student(student):
    print("name: "+student["name"]+"\nlikings: "+str(student["likings"])+"\nslots: "+slots_to_string(student["slots"]))

def print_student_list(student_list):
    for student in student_list:
        print_student(student)
        print("\n")

def proposals_to_string(proposals):
    total_string = ""
    for proposal in proposals:
        total_string+=str(proposal)+"\n"
    return total_string

def print_teacher(teacher):
    print("name: "+teacher["name"]+"\nproposals: "+proposals_to_string(teacher["proposals"]))

def print_teacher_list(teacher_list):
    for teacher in teacher_list:
        print_teacher(teacher)
        print("\n")

student_beginning_time = datetime.datetime(2021,1,19,8)
student_ending_time = student_beginning_time+datetime.timedelta(hours=2)

teacher_beginning_time = datetime.datetime(2021,1,19,8)
teacher_ending_time = student_beginning_time+datetime.timedelta(hours=3)

student_slot = {"beginning":student_beginning_time, "end":student_ending_time}
teacher_proposal = {"activity":"tennis", "beginning":teacher_beginning_time, "end":teacher_ending_time}
student=generate_student(2,"Pete",["golf"],[student_slot])

teacher_list = generate_random_teachers(5)
student_list = generate_random_students(5)

print("TEACHER LIST\n\n",teacher_list)

print_teacher_list(teacher_list)

print("STUDENT LIST\n\n")

print_student_list(student_list)

def match(teachers,students):
    match_list = []
    for teacher in teachers:
        for proposal in teacher["proposals"]:
            already_attributed=False
            if students != []:
                for student in students:
                    if proposal["activity"] in student["likings"] and not already_attributed:
                        for slot in student["slots"]:
                            if is_free_time(proposal,slot):
                                match_list.append((teacher["id"],proposal,student["id"],slot))
                                student["slots"].remove(slot)
                                already_attributed=True
    return match_list

matches = match(teacher_list,student_list)

def print_match_list(match_list):
    for match in match_list:
        print(str(match)+"\n")

print_match_list(matches)




# print(is_free_student(teacher_proposal,student))


# def match_teachers_students(teacher_list,student_list):
