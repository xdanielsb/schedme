# activités proposées: piano, guitare, tennis (for example)

from random import choice, randint
import datetime

activities = ["piano","guitar","tennis"]

def parse_datetime(date_string, time_string): # format attendu: "DD/MM/YYYY HH:MM"
    return datetime.datetime.strptime(date_string+" "+time_string, "%d/%m/%Y %H:%M")

print(parse_datetime("19/01/2021","19:00"))

def generate_proposal(activity, beginning, end, seats):
    return {"activity":activity, "beginning":beginning, "end":end, "seats":10}

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

print(generate_random_proposals(3))

professor1 = {"id":"p0", "name":"Peter", "proposals":generate_random_proposals(2)}
print(professor1)

professor2 = {"id":"p1", "name":"John", "proposals":generate_random_proposals(5)}
print(professor2)



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

student1 = {"id":"s1", "name":"Carole", "likings":["guitar","piano"], "slots":generate_random_slots(2)}
student2 = {"id":"s2", "name":"Marie", "likings":["guitar","tennis"], "slots":generate_random_slots(2)}




student1 = generate_student("0", "John", ["guitar"], [slot1])
print(student1)

