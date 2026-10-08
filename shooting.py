# Shooting system for Space Shooter

score = 0
bullets = 5

print("SHOOTING SYSTEM")

while bullets > 0:
    print("Bullets left:", bullets)
    choice = input("Press S to shoot or Q to quit: ")

    if choice.lower() == "s":
        print("🚀 Bullet fired!")
        score += 10
        bullets -= 1
        print("Score:", score)

    elif choice.lower() == "q":
        break

    else:
        print("Invalid choice")

print("Final Score:", score)