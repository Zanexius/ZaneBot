dragon = {
    "type": "fire",
    "dmg": 5,
    "hp": 100
}
dragon["hp"] = dragon["hp"]-5
dragonhp = "Dragon's hp: {0}"
print(dragonhp.format(dragon["hp"]))

