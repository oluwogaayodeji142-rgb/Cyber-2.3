while True:
    print("\nChoose a physics operation:")
    print("1. Calculate Velocity")
    print("2. Calculate Kinetic Energy")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        print("\n--- Velocity (v = d / t) ---")
        distance = float(input("Enter distance (meters): "))
        time = float(input("Enter time (seconds): "))

        if time == 0:
            print("Time cannot be zero.")
        elif time < 0:
            print("Time cannot be negative.")
        else:
            velocity = distance / time
            print(f"Velocity = {velocity:.2f} m/s")

    elif choice == "2":
        print("\n--- Kinetic Energy (KE = 0.5 * m * v^2) ---")
        mass = float(input("Enter mass (kg): "))
        velocity = float(input("Enter velocity (m/s): "))

        if mass < 0:
            print("Mass cannot be negative.")
        else:
            ke = 0.5 * mass * velocity ** 2
            print(f"Kinetic Energy = {ke:.2f} Joules")

    else:
        print("Invalid choice. Please select 1 or 2.")

    cont = input("\nContinue? (y/n): ").strip().lower()
    if cont != "y" and cont != "yes":
        print("Exiting program. Goodbye!")
        break