numbers = [3, 1, 4, 2, 5, 2]

seen = set()

for number in numbers:
    if number in seen:
        print(f"{number} upprepas – loopen avslutas")
        break
    print(number)
    seen.add(number)
      
print("Found a duplicate:", number)