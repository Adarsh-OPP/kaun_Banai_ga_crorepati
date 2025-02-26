questions = [
    ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    ["Which planet is known as the Red Planet?", "Mars", "Venus", "Jupiter", "Saturn", 1],
    ["Who wrote the national anthem of India?", "Tagore", "Gandhi", "Nehru", "Tilak", 1],
    ["Which animal is known as the King of the Jungle?", "Lion", "Tiger", "Elephant", "Cheetah", 1],
    ["Which is the largest ocean in the world?", "Atlantic", "Indian", "Arctic", "Pacific", 4],
    ["Which metal is liquid at room temperature?", "Mercury", "Iron", "Silver", "Gold", 1],
    ["How many states are there in India?", "28", "29", "27", "30", 1],
    ["What is the national currency of India?", "Dollar", "Rupee", "Pound", "Yen", 2],
    ["Who invented the telephone?", "Edison", "Bell", "Tesla", "Newton", 2],
    ["Which is the smallest continent?", "Asia", "Africa", "Europe", "Australia", 4],
    ["Which is the longest river in the world?", "Amazon", "Nile", "Ganges", "Yangtze", 2],
    ["Who was the first Prime Minister of India?", "Nehru", "Gandhi", "Patel", "Ambedkar", 1],
    ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
    ["What is the national flower of India?", "Lotus", "Rose", "Sunflower", "Lily", 1],
    ["Which festival is known as the festival of lights?", "Diwali", "Holi", "Eid", "Christmas", 1]
]


levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(question[0])
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    if (i < 4):
        money = 0 
        break
    else:
        money = levels[i-1]
        break

  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")