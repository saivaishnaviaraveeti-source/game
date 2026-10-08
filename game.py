import random

print("🚀 SPACE SHOOTER GAME 🚀")
print("Defeat the enemy ships!")

player_health = 3
score = 0

while player_health > 0:
    print("\n1. Shoot")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        enemy = random.randint(1, 3)

        if enemy == 1:
            print("🎯 Enemy defeated!")
            score += 10
        else:
            print("💥 Enemy attacked you!")
            player_health -= 1

        print("Health:", player_health)
        print("Score:", score)

    elif choice == "2":
        print("Game ended.")
        break

    else:
        print("Invalid choice. Try again.")

if player_health == 0:
    print("\nGame Over!")
    print("Final Score:", score)
else:
    print("\nFinal Score:", score)
