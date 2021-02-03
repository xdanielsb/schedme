# activités proposées: piano, guitare, tennis (for example)

from random import choice, randint, choices
import datetime
from datetime import date


def parse_datetime(date_string, time_string):  # format attendu: "DD/MM/YYYY HH:MM"
    return datetime.datetime.strptime(date_string + " " + time_string, "%d/%m/%Y %H:%M")


def generate_proposal(topic, start, end, number_of_slots):
    return {
        "topic": topic,
        "start": start,
        "end": end,
        "number_of_slots": number_of_slots,
    }


def generate_random_proposals(number):
    activities = [
        "piano",
        "guitar",
        "tennis",
        "cooking",
        "singing",
        "pilates",
        "zumba",
        "art",
    ]
    retured_list = []
    today = date.today()
    for i in range(number):
        topic = choice(activities)
        start_time = randint(8, 17)
        start = datetime.datetime(today.year, today.month, randint(1, 27), start_time)
        end = start + datetime.timedelta(hours=2)
        number_of_slots = randint(5, 10)
        proposal = generate_proposal(topic, start, end, number_of_slots)
        retured_list.append(proposal)
    return retured_list


def generate_random_teacher(id):
    teacher_names = [
        "John",
        "Maria",
        "Sophia",
        "Mia",
        "Peter",
        "Martin",
        "Rick",
        "Ada",
        "Claire",
        "Mark",
        "Daphne",
        "Daniel",
        "Dora",
    ]
    last_names = ["Smith", "Biden", "Jones", "Miller", "Davis"]
    dict_id = "p" + str(id)
    name = choice(teacher_names)
    last_name = choice(last_names)
    email = name.lower() + "." + last_name.lower() + "@scheduled.me"
    proposals = generate_random_proposals(10)
    return {
        "id": dict_id,
        "name": name,
        "email": email,
        "last_name": last_name,
        "url_video_call": "https://meet.google.com/schedme{}-teacher".format(name),
        "proposals": proposals,
    }


def generate_random_teachers(number):
    teacher_list = []
    for i in range(number):
        teacher_list.append(generate_random_teacher(i))
    return teacher_list


# Elèves


def generate_slot(start, end):
    return {"start": start, "end": end}


def generate_random_slots(number):
    retured_list = []
    for i in range(number):
        start_time = randint(8, 17)
        start = datetime.datetime(2021, 1, 19, start_time)
        end = start + datetime.timedelta(hours=3)
        slot = generate_slot(start, end)
        retured_list.append(slot)
    return retured_list


def generate_student(id, name, likings, slots):
    return {"id": "s" + str(id), "name": name, "likings": likings, "slots": slots}


def generate_random_student(id):
    student_names = ["Paul", "Jessy", "Harry", "Joy", "Fatima", "Mickael", "Lucy"]
    activities = ["piano", "guitar", "tennis"]
    dict_id = "s" + str(id)
    name = choice(student_names)
    likings = choices(activities, k=2)
    return {
        "id": dict_id,
        "name": name,
        "likings": likings,
        "slots": generate_random_slots(2),
    }


def generate_random_students(number):
    student_list = []
    for i in range(number):
        student_list.append(generate_random_student(i))
    return student_list


"""def is_free(teacher,student):
    for proposal in teacher["proposals"]:"""


def is_free_time(teacher_proposal, student_slot):
    return (
        student_slot["start"] <= teacher_proposal["start"]
        and student_slot["end"] >= teacher_proposal["end"]
    )


"""
    def is_free_student(teacher_proposal,student):
        for student_slot in student["slots"]:
            return is_free_time(teacher_proposal,student_slot) and teacher_proposal["topic"] in student["likings"]:
"""

# fonctions auxiliaires pour + de lisibilité dans les tests


def slots_to_string(slots):
    total_string = ""
    for slot in slots:
        total_string += str(slot) + "\n"
    return total_string


def print_student(student):
    print(
        "name: "
        + student["name"]
        + "\nlikings: "
        + str(student["likings"])
        + "\nslots: "
        + slots_to_string(student["slots"])
    )


def print_student_list(student_list):
    for student in student_list:
        print_student(student)
        print("\n")


def proposals_to_string(proposals):
    total_string = ""
    for proposal in proposals:
        total_string += str(proposal) + "\n"
    return total_string


def print_teacher(teacher):
    print(
        "name: "
        + teacher["name"]
        + "\nproposals: "
        + proposals_to_string(teacher["proposals"])
    )


def print_teacher_list(teacher_list):
    for teacher in teacher_list:
        print_teacher(teacher)
        print("\n")


def match(teachers, students):
    match_list = []
    for teacher in teachers:
        for proposal in teacher["proposals"]:
            proposal_slots = proposal["number_of_slots"]
            if students != []:
                for student in students:
                    if proposal["topic"] in student["likings"] and proposal_slots > 0:
                        for slot in student["slots"]:
                            if is_free_time(proposal, slot):
                                match_list.append(
                                    (teacher["id"], student["id"], proposal)
                                )
                                student["slots"].remove(slot)
                                if slot["start"] < proposal["start"]:
                                    student["slots"].append(
                                        {
                                            "start": slot["start"],
                                            "end": proposal["start"],
                                        }
                                    )
                                if slot["end"] > proposal["end"]:
                                    student["slots"].append(
                                        {
                                            "start": proposal["end"],
                                            "end": slot["end"],
                                        }
                                    )
                                proposal_slots -= 1
    return match_list


def print_match_list(match_list):
    for match in match_list:
        print(str(match) + "\n")


if __name__ == "__main__":

    start_time = randint(8, 17)
    start = datetime.datetime(2021, 1, 19, start_time)
    end = start + datetime.timedelta(hours=2)

    slot1 = {"start": start, "end": end}

    student_start_time = datetime.datetime(2021, 1, 19, 8)
    student_ending_time = student_start_time + datetime.timedelta(hours=3)

    teacher_start_time_1 = datetime.datetime(2021, 1, 19, 8)
    teacher_ending_time_1 = teacher_start_time_1 + datetime.timedelta(hours=2)

    teacher_start_time_2 = datetime.datetime(2021, 1, 19, 10)
    teacher_ending_time_2 = teacher_start_time_2 + datetime.timedelta(hours=1)

    student_slot = {"start": student_start_time, "end": student_ending_time}
    teacher_proposal_1 = {
        "topic": "tennis",
        "start": teacher_start_time_1,
        "end": teacher_ending_time_1,
        "number_of_slots": 2,
    }
    teacher_proposal_2 = {
        "topic": "tennis",
        "start": teacher_start_time_2,
        "end": teacher_ending_time_2,
        "number_of_slots": 2,
    }
    teacher_proposals = [teacher_proposal_1, teacher_proposal_2]
    teacher = {"id": "p2", "name": "Jane", "proposals": teacher_proposals}
    student = generate_student(2, "Pete", ["tennis"], [student_slot])

    teacher_list = generate_random_teachers(1)
    print(teacher_list)
    student_list = generate_random_students(30)

    # print_student_list(student_list)
    # print_teacher_list(teacher_list)

    matches_one_test = match([teacher], [student])
    matches_test = match(teacher_list, student_list)

    # print("With one teacher and one student:\n")

    # print_match_list(matches_one_test)

    # print("With several of both:\n")

    # print_match_list(matches_test)
