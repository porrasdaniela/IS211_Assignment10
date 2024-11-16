import sqlite3

def query_pets():
    conn = sqlite3.connect('pets.db')    # Connect to the database
    cur = conn.cursor()

    while True:
        # Ask the user for a person's ID
        person_id = input("Enter a person's ID (or -1 to exit): ")

        if person_id == '-1':
            break

        # Query the person details
        cur.execute('''
            SELECT first_name, last_name, age FROM person WHERE id = ?
        ''', (person_id,))
        person = cur.fetchone()

        if person:
            print(f"{person[0]} {person[1]}, {person[2]} years old")

            # Query the pets for that person
            cur.execute('''
                SELECT pet.name, pet.breed, pet.age FROM pet 
                JOIN person_pet ON person_pet.pet_id = pet.id
                WHERE person_pet.person_id = ?
            ''', (person_id,))
            pets = cur.fetchall()

            if pets:
                for pet in pets:
                    print(f"{person[0]} owned {pet[0]}, a {pet[1]} that was {pet[2]} years old.")
            else:
                print(f"{person[0]} has no pets.")
        else:
            print("Person not found.")


    # Close the connection
    conn.close()

# Run the query function
query_pets()