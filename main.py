from game_data import data
import random
import art

def pick_random_person():
    reandomIndex = random.randint(0,len(data)-1)
    return data[reandomIndex]
run = True

def verify_guess(num, guess):
    if num[0] > num[1]:
        correct_index = 0
    elif num[1] > num[0]:
        correct_index = 1
    else:
        return False
    if guess == "a":
        gussed_index = 0
    elif guess == "b":
        gussed_index = 1
    return gussed_index == correct_index
print(art.logo)
def play(run):
    score = 0
    person1 = pick_random_person()
    while run:
        person2 = pick_random_person()
        follower = [person1["follower_count"], person2["follower_count"]]
        persons = [person1, person2]
        winnerindex = follower.index(max(follower))
        print(f"Compare A: {person1["name"]}, {person1["description"]}, {person1["country"]}")
        print(art.vs)
        print(f"Compare B: {person2["name"]}, {person2["description"]}, {person2["country"]}")
        cohice = input("Who has more followers? A/B : \n").lower()
        if verify_guess(follower, cohice):
            score += 1
            print(f"score : {score}")
            person1 = persons[winnerindex]
        else:
            print(art.logo)
            print(f"you lose, final score : {score}")
            play_again = (input("do you want to play again? y/n :"))
            if play_again == 'y':
                play(run)
            else:
                print("thanks for playing!!")
                run = False
play(run)