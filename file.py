
# ==================================================
#              BINGHAM UNIVERSITY
#                COS 101 ASSIGNMENT
#              PHYSICS CALCULATOR
# ==================================================

# Student Name: OLUWOGA OLUFEMI
# Matric Number: BHU/26/04/09/0072
# Course: COS 101

print("=" * 50)
print("             PHYSICS CALCULATOR")
print("=" * 50)

while True:

    print("\nSELECT A FORMULA TO CALCULATE")
    print("1. Speed")
    print("2. Force")
    print("3. Weight")
    print("4. Acceleration")
    print("5. Kinetic Energy")
    print("0. Exit Calculator")

    choice = input("\nEnter your choice (0-5): ")

    if choice == "1":
        print("\n--- SPEED CALCULATION ---")

        distance = float(input("Enter distance (metres): "))
        time = float(input("Enter time (seconds): "))

        if time <= 0:
            print("Error: Time must be greater than zero.")
        else:
            speed = distance / time
            print("Speed =", speed, "m/s")

    elif choice == "2":
        print("\n--- FORCE CALCULATION ---")

        mass = float(input("Enter mass (kg): "))
        acceleration = float(input("Enter acceleration (m/s^2): "))

        force = mass * acceleration
        print("Force =", force, "N")

    elif choice == "3":
        print("\n--- WEIGHT CALCULATION ---")

        mass = float(input("Enter mass (kg): "))
        gravity = float(input("Enter gravity (m/s^2): "))

        weight = mass * gravity
        print("Weight =", weight, "N")

    elif choice == "4":
        print("\n--- ACCELERATION CALCULATION ---")

        final_velocity = float(input("Enter final velocity (m/s): "))
        initial_velocity = float(input("Enter initial velocity (m/s): "))
        time = float(input("Enter time (seconds): "))

        if time <= 0:
            print("Error: Time must be greater than zero.")
        else:
            acceleration = (final_velocity - initial_velocity) / time
            print("Acceleration =", acceleration, "m/s^2")

    elif choice == "5":
        print("\n--- KINETIC ENERGY CALCULATION ---")

        mass = float(input("Enter mass (kg): "))
        velocity = float(input("Enter velocity (m/s): "))

        kinetic_energy = 0.5 * mass * velocity ** 2
        print("Kinetic Energy =", kinetic_energy, "J")

    elif choice == "0":
        print("\nThank you for using the Physics Calculator!")
        print("End of Assignment.")
        break

    else:
        print("\nInvalid choice! Please select a number from 0 to 5.")

    print("\n" + "=" * 50)
