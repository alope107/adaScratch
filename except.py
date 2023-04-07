from datetime import datetime
from dateutil.relativedelta import relativedelta

def main():
    finished = False
    people = []

    while not finished:
        name = input("Enter person name or 'Finished': ")
        
        if name == 'Finished':
            finished = True
            break

        birthdate = input("Enter birthdate (mm/dd/yy): ")
        try:
            person = create_person(name, birthdate)
        except ValueError:
            print(f"Invalid date: {birthdate}")
            continue
        people.append(person)

    print("These are the people you entered")
    print(people)
    

def create_person(name, birthdate):
    parsed_date = datetime.strptime(birthdate, '%m/%d/%Y')
    current_time = datetime.now()
    age = relativedelta(current_time, parsed_date).years
    return {"name": name, "age": age}

main()