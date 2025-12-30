# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FactoryCalculator.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marykman <marykman@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 03:13:05 by marykman          #+#    #+#              #
#    Updated: 2025/12/30 03:13:05 by marykman         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from enum import Enum, auto

class Item:
	def __init__(self, name, quantity=1, *args):
		self.name = name
		self.quantity = quantity
		self.recipe = args
		self.hasRecipe = False if len(self.recipe) == 0 else True

class Items(Enum):
	# === BASE MATERIAL ===
	# IRON
	IRON_ORE = Item("Iron ore")
	IRON_INGOT = Item("Iron ingot", 30, [30, IRON_ORE])
	# COPPER
	COPPER_ORE = Item("Copper ore")
	COPPER_INGOT = Item("Copper ingot", 30, [30, COPPER_ORE])
	# COAL
	COAL = Item("Coal")
	# LIMESTONE
	LIMESTONE = Item("Limestone")
	# STEEL
	STEEL_INGOT = Item("Steel ingot", 45, [45, IRON_ORE], [45, COAL])

	# === BASE PRODUCT ===
	# IRON
	IRON_PLATE = Item("Iron plate", 20, [30, IRON_INGOT])
	IRON_ROD = Item("Iron rod", 15, [15, IRON_INGOT])
	SCREW = Item("Screw", 50, [12.5, IRON_INGOT])
	# COPPER
	WIRE = Item("Wire", 30, [15, COPPER_INGOT])
	# LIMESTONE
	CONCRETE = Item("Concrete", 15, [45, LIMESTONE])
	# STEEL
	STEEL_BEAM = Item("Steel beam", 15, [60, STEEL_INGOT])
	STEEL_PIPE = Item("Steel pipe", 20, [30, STEEL_INGOT])

	# === TIER 2 PRODUCT ===
	REINFORCED_IRON_PLATE = Item("Reinforced iron plate", 5, [30, IRON_PLATE], [60, SCREW])
	ROTOR = Item("Rotor", 4, [20, IRON_ROD], [100, SCREW])
	STATOR = Item("Stator", 5, [15, STEEL_PIPE], [40, WIRE])
	ENCASED_INDUSTRIAL_BEAM = Item("Encased industrial beam", 6, [18, STEEL_BEAM], [36, CONCRETE])

	# === TIER 3 PRODUCT ===
	MODULAR_FRAME = Item("Modular frame", 5, [7.5, REINFORCED_IRON_PLATE], [140, SCREW])
	MOTOR = Item("Motor", 5, [10, ROTOR], [10, STATOR])



totalItems = {}

def addItem(name, quantity):
	if name in totalItems:
		totalItems[name] += quantity
	else:
		totalItems[name] = quantity

def produceItem(item, quantity):
	ratio = quantity / item.quantity
	addItem(item.name, quantity)
	for i in item.recipe:
		produceItem(i[1], i[0] * ratio)



def printItem(item):
	if item.value.name in totalItems:
		print(f"{item.value.name:30s}:\t{totalItems[item.value.name]}")
	else:
		print(f"{item.value.name:30s}:")

def prettyPrint():
	printItem(Items.IRON_INGOT)
	print()
	printItem(Items.IRON_PLATE)
	printItem(Items.IRON_ROD)
	printItem(Items.SCREW)
	print()
	printItem(Items.REINFORCED_IRON_PLATE)
	printItem(Items.ROTOR)
	print()
	printItem(Items.MODULAR_FRAME)

def loopPrint():
	for item in Items:
		printItem(item)



def baseMaterialFactory():
	produceItem(Items.IRON_PLATE.value, 20)
	produceItem(Items.IRON_ROD.value, 15)
	produceItem(Items.IRON_ROD.value, 12.5)
	produceItem(Items.SCREW.value, 50)
	produceItem(Items.REINFORCED_IRON_PLATE.value, 5)
	produceItem(Items.ROTOR.value, 4)
	produceItem(Items.MODULAR_FRAME.value, 5)

def motorFactory():
	produceItem(Items.MOTOR.value, 5)
	produceItem(Items.ENCASED_INDUSTRIAL_BEAM.value, 11.875)

if __name__ == '__main__':
	motorFactory()
	loopPrint()