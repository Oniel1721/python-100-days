import random

welcome_message = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/  
"""

vs_message = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

print(welcome_message)

influencers = [
    {
        "name": "Kylie Jenner",
        "follower_count": 223,
        "description": "Reality TV personality and entrepreneur",
        "country": "United States",
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 333,
        "description": "Football player",
        "country": "Portugal",
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 250,
        "description": "Actor and former wrestler",
        "country": "United States",
    },
    {
        "name": "Selena Gomez",
        "follower_count": 200,
        "description": "Singer and actress",
        "country": "United States",
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 213,
        "description": "Reality TV personality and entrepreneur",
        "country": "United States",
    },
    {
        "name": "Lionel Messi",
        "follower_count": 220,
        "description": "Football player",
        "country": "Argentina",
    },
    {
        "name": "Beyoncé",
        "follower_count": 170,
        "description": "Singer and actress",
        "country": "United States",
    },
    {
        "name": "Neymar Jr",
        "follower_count": 150,
        "description": "Football player",
        "country": "Brazil",
    },
    {
        "name": "Taylor Swift",
        "follower_count": 170,
        "description": "Singer and songwriter",
        "country": "United States",
    },
    {
        "name": "Justin Bieber",
        "follower_count": 150,
        "description": "Singer",
        "country": "Canada",
    }
]

def ask_user_answer():
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if(answer != "A" and answer != "B"):
        print("Invalid answer. Please try again.")
        return ask_user_answer()
    return answer

score = 0
game_over = False

influencer_a = random.choice(influencers)
influencer_b = random.choice(influencers)
while not game_over:
    if influencer_a["follower_count"] > influencer_b["follower_count"]:
        correct_answer = "A"
    elif influencer_a["follower_count"] < influencer_b["follower_count"]:
        correct_answer = "B"
    else:
        influencer_a = random.choice(influencers)
        influencer_b = random.choice(influencers)
        
    print(f"Compare A: {influencer_a['name']}, a {influencer_a['description']}, from {influencer_a['country']}")
    print(vs_message)
    print(f"Against B: {influencer_b['name']}, a {influencer_b['description']}, from {influencer_b['country']}")
    answer = ask_user_answer()
    
    if answer == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}")
        influencer_a = influencer_b
        influencer_b = random.choice(influencers)
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")
        