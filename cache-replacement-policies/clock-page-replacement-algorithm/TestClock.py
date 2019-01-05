import ClockPageHandler

MEMORY = {
    "Apple": 2,
    "Grape": 5,
    "Pea": 1,
    "Mango": 6,
    "Kiwi": 4,
    "Starfruit": 3,
    "Peach": 4,
    "Fish": 0,
    "Potato": 1,
    "Orange": 5
}

clock = ClockPageHandler.Clock(MEMORY, 3, True)

# Page hit on a partially filled clock
clock.get("Apple")
clock.get("Apple")

# Page misses on a partially filled clock
clock.get("Grape")
clock.get("Pea")

# Page hit on full clock
clock.get("Apple")

# Page miss on a full clock
clock.get("Mango")

# Page hit on a full clock hand not pointing to hit item
clock.get("Pea")

# Page hits on a full clock
clock.get("Apple")
clock.get("Mango")

# Page miss on a full clock (all Referenced are true)
clock.get("Fish")

# Page miss
clock.get("Pea")

print("Final clock state: ", clock.print_clock())
