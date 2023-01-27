"""
Lost Ark Crafting Profit Calculator
Input the current auction house prices and this will calculate
total cost, total profit, and profit per hour

Author: Jason Koser
"""


def simple_oreha(time_decrease: float, cost_decrease: float) -> None:
    print("What is the price of a Simple Oreha Material?")
    sell_price = int(input())
    total_sell_price = sell_price * 30
    
    print("What is the price of Ancient Relic?")
    ingredient1_price = int(input())
    ingredient1_cost = (ingredient1_price / 100) * 56
    
    print("What is the price of Rare Relic?")
    ingredient2_price = int(input())
    ingredient2_cost = (ingredient2_price / 10) * 28
    
    print("What is the price of Oreha Relic?")
    ingredient3_price = int(input())
    ingredient3_cost = (ingredient3_price / 10) * 7

    total_hours = .5 * (1 - (time_decrease / 100))

    crafting_cost = 203 * (1 - (cost_decrease / 100))
    
    total_cost = ingredient1_cost + ingredient2_cost + ingredient3_cost + crafting_cost
    total_profit = total_sell_price - total_cost
    
    print(f"Total Sell Price is {total_sell_price}g")
    print(f"Ancient Relic cost is {ingredient1_cost}g")
    print(f"Rare Relic cost is {ingredient2_cost}g")
    print(f"Oreha Relic cost is {ingredient3_cost}g")
    print(f"Crafting cost is {crafting_cost}g")
    print(f"For a total cost of {total_cost}g")
    print(f"Leading to a profit of {total_profit}g or {total_profit / total_hours}g an hour")
    
def basic_oreha_excavating(time_decrease: float, cost_decrease: float) -> None:
    print("What is the price of a Basic Oreha Material?")
    sell_price = int(input())
    total_sell_price = sell_price * 30
    
    print("What is the price of Ancient Relic?")
    ingredient1_price = int(input())
    ingredient1_cost = (ingredient1_price / 100) * 64
    
    print("What is the price of Rare Relic?")
    ingredient2_price = int(input())
    ingredient2_cost = (ingredient2_price / 10) * 26
    
    print("What is the price of Oreha Relic?")
    ingredient3_price = int(input())
    ingredient3_cost = (ingredient3_price / 10) * 8

    total_hours = .75 * (1 - (time_decrease / 100))

    crafting_cost = 205 * (1 - (cost_decrease / 100))
    
    total_cost = ingredient1_cost + ingredient2_cost + ingredient3_cost + crafting_cost
    total_profit = (total_sell_price * .95) - total_cost
    
    print(f"Total Sell Price is {total_sell_price}g")
    print(f"Ancient Relic cost is {ingredient1_cost}g")
    print(f"Rare Relic cost is {ingredient2_cost}g")
    print(f"Oreha Relic cost is {ingredient3_cost}g")
    print(f"Crafting cost is {crafting_cost}g")
    print(f"For a total cost of {total_cost}g")
    print(f"Leading to a profit of {total_profit}g or {total_profit / total_hours}g an hour")
    
def basic_oreha_fishing(time_decrease: float, cost_decrease: float) -> None:
    print("What is the price of a Basic Oreha Material?")
    sell_price = int(input())
    total_sell_price = sell_price * 30
    
    print("What is the price of Fish?")
    ingredient1_price = int(input())
    ingredient1_cost = (ingredient1_price / 100) * 80
    
    print("What is the price of Natural Pearls?")
    ingredient2_price = int(input())
    ingredient2_cost = (ingredient2_price / 10) * 40
    
    print("What is the price of Oreha Solar Carp?")
    ingredient3_price = int(input())
    ingredient3_cost = (ingredient3_price / 10) * 10

    total_hours = .75 * (1 - (time_decrease / 100))

    crafting_cost = 205 * (1 - (cost_decrease / 100))
    
    total_cost = ingredient1_cost + ingredient2_cost + ingredient3_cost + crafting_cost
    total_profit = (total_sell_price * .95) - total_cost
    
    print(f"Total Sell Price is {total_sell_price}g")
    print(f"Fish cost is {ingredient1_cost}g")
    print(f"Natural Pearl cost is {ingredient2_cost}g")
    print(f"Oreha Solar Carp cost is {ingredient3_cost}g")
    print(f"Crafting cost is {crafting_cost}g")
    print(f"For a total cost of {total_cost}g")
    print(f"Leading to a profit of {total_profit}g or {total_profit / total_hours}g an hour")
    
def basic_oreha_hunting(time_decrease: float, cost_decrease: float) -> None:
    print("What is the price of a Basic Oreha Material?")
    sell_price = int(input())
    total_sell_price = sell_price * 30
    
    print("What is the price of Raw Meat?")
    ingredient1_price = int(input())
    ingredient1_cost = (ingredient1_price / 100) * 80
    
    print("What is the price of Tough Leather?")
    ingredient2_price = int(input())
    ingredient2_cost = (ingredient2_price / 10) * 40
    
    print("What is the price of Oreha Meat?")
    ingredient3_price = int(input())
    ingredient3_cost = (ingredient3_price / 10) * 10

    total_hours = .75 * (1 - (time_decrease / 100))

    crafting_cost = 205 * (1 - (cost_decrease / 100))
    
    total_cost = ingredient1_cost + ingredient2_cost + ingredient3_cost + crafting_cost
    total_profit = (total_sell_price * .95) - total_cost
    
    print(f"Total Sell Price is {total_sell_price}g")
    print(f"Raw Meat cost is {ingredient1_cost}g")
    print(f"Tough Leather cost is {ingredient2_cost}g")
    print(f"Oreha Meat cost is {ingredient3_cost}g")
    print(f"Crafting cost is {crafting_cost}g")
    print(f"For a total cost of {total_cost}g")
    print(f"Leading to a profit of {total_profit}g or {total_profit / total_hours}g an hour")
    
def sprinter_robe(time_decrease: float, cost_decrease: float) -> None:
    print("What is the price of a Sprinter's Robe?")
    sell_price = int(input())
    total_sell_price = sell_price * 3
    
    print("What is the price of Tough Leather?")
    ingredient1_price = int(input())
    ingredient1_cost = (ingredient1_price / 10) * 17
    
    print("What is the price of Shy Wild Flower?")
    ingredient2_price = int(input())
    ingredient2_cost = (ingredient2_price / 10) * 17
    
    print("What is the price of Wild Flower?")
    ingredient3_price = int(input())
    ingredient3_cost = (ingredient3_price / 100) * 27

    total_hours = .5 * (1 - (time_decrease / 100))

    crafting_cost = 15 * (1 - (cost_decrease / 100))
    
    total_cost = ingredient1_cost + ingredient2_cost + ingredient3_cost + crafting_cost
    total_profit = total_sell_price - total_cost
    
    print(f"Total Sell Price is {total_sell_price}g")
    print(f"Wild Flower cost is {ingredient1_cost}g")
    print(f"Shy Wild Flower cost is {ingredient2_cost}g")
    print(f"Tough Leather cost is {ingredient3_cost}g")
    print(f"Crafting cost is {crafting_cost}g")
    print(f"For a total cost of {total_cost}g")
    print(f"Leading to a profit of {total_profit}g or {total_profit / total_hours}g an hour")
    
def tool_part(time_decrease: float, cost_decrease: float) -> None:
    print("What is the price of a Tool Crafting Part?")
    sell_price = int(input())
    total_sell_price = sell_price * 30
    
    print("What is the price of Strong Iron Ore?")
    ingredient1_price = int(input())
    ingredient1_cost = (ingredient1_price / 10) * 22
    
    print("What is the price of Sturdy Timber?")
    ingredient2_price = int(input())
    ingredient2_cost = (ingredient2_price / 10) * 22
    
    print("What is the price of Heavy Iron Ore?")
    ingredient3_price = int(input())
    ingredient3_cost = (ingredient3_price / 10) * 88
    
    print("What is the price of Tender Timber?")
    ingredient4_price = int(input())
    ingredient4_cost = (ingredient4_price / 10) * 88

    total_hours = 1 * (1 - (time_decrease / 100))

    crafting_cost = 20 * (1 - (cost_decrease / 100))
    
    total_cost = ingredient1_cost + ingredient2_cost + ingredient3_cost + ingredient4_cost + crafting_cost
    total_profit = total_sell_price - total_cost
    
    print(f"Total Sell Price is {total_sell_price}g")
    print(f"Strong Iron Ore cost is {ingredient1_cost}g")
    print(f"Sturdy Timber cost is {ingredient2_cost}g")
    print(f"Heavy Iron Ore cost is {ingredient3_cost}g")
    print(f"Tender Timber cost is {ingredient4_cost}g")
    print(f"Crafting cost is {crafting_cost}g")
    print(f"For a total cost of {total_cost}g")
    print(f"Leading to a profit of {total_profit}g or {total_profit / total_hours}g an hour")

def main() -> None:
    print("What is your time decrease %?")
    time_decrease = float(input())
    
    print("What is your crafting cost decrease %?")
    cost_decrease = float(input())
    
    print("Select which item you want to craft")
    print("(1) Simple Oreha Material Fusion excavating")
    print("(2) Basic Oreha Fusion Material excavating")
    print("(3) Basic Oreha Fusion Material fishing")
    print("(4) Basic Oreha Fusion Material hunting")
    print("(5) Sprinter's Robe")
    print("(6) Tool Crafting Part")
    
    match int(input()):
        case 1:
            simple_oreha(time_decrease, cost_decrease)
        case 2:
            basic_oreha_excavating(time_decrease, cost_decrease)
        case 3:
            basic_oreha_fishing(time_decrease, cost_decrease)
        case 4:
            basic_oreha_hunting(time_decrease, cost_decrease)
        case 4:
            sprinter_robe(time_decrease, cost_decrease)
        case 5:
            tool_part(time_decrease, cost_decrease)
        case _:
            print("Please enter a number according to the material you want to craft")
            
    
    

if __name__ == "__main__":
    main()
