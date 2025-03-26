import cv2
import face_recognition
import json
import numpy as np

def add_new_user(name, bio, file_name, users, database):
    img = cv2.imread(file_name)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    embedding = face_recognition.face_encodings(img_rgb)[0].tolist()

    users.append({
        'name': name,
        'bio': bio,
        'embedding': embedding
    })

    data = {
        'users': users
    }

    with open(database, 'w') as file:
        json.dump(data, file, indent=4)
    
    return "\nUser successfully created"

def verify_user(file_name, database):
    img = cv2.imread(file_name)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    embedding = face_recognition.face_encodings(img_rgb)[0]

    users = fetch_user(database)

    if len(users) > 0:
        for user in users:
            result = face_recognition.compare_faces([np.array(user['embedding'])], embedding)
            if result[0]:
                return f"\nUser found!\nName: {user['name']}\nBio: {user['bio']}\n"
        return "\nUser not found!\n"

    else:
        return "No user in the database"

def fetch_user(database):
    try:
        with open(database, 'r') as file:
            data = json.load(file)
        return data['users']
    
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def print_menu():
    print("\nWhat would you like to do?\n")
    print("1. Verify a User")
    print("2. Add new User")
    print("3. End the program")

def main():
    print("Welcome to X Face Recognition")
    

    database = "database.json"

    users = fetch_user(database)

    while True:
        print_menu()

        choice = input("Enter your choice (1, 2 or 3): ")

        if choice == '1':
            file_name = input('Enter image: ')
            response = verify_user(file_name, database)
            print(response)
        elif choice == '2':
            name = input('Enter name: ')
            bio = input('Enter Bio details: ')
            file_name = input('Enter image: ')

            response = add_new_user(name, bio, file_name, users, database)
            print(response)
        elif choice == '3':
            break
        else:
            print('Invalid input. Provide numerical value')


if __name__ == '__main__':
    main()