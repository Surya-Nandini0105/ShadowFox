justice_league = [
    "Wonder Woman",
    "Batman",
    "Superman",
    "Flash",
    "Aquaman",
    "Green Lantern",
    "Batgirl",
    "Nightwing"
]
justice_league.remove("Superman")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index, "Superman")
print("After separating Aquaman and Flash:", justice_league)
