#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
  # check recipe vs ingredientst
  can_make = True
  batches = 0
  if len(ingredients) < len(recipe):
    return batches
  while can_make:
    for key in recipe:
      if recipe[key] == None:
        can_make = False
        
      
      elif ingredients[key] < recipe[key]:
        can_make = False
        
      
      elif ingredients[key] >= recipe[key]:
        ingredients[key] = ingredients[key] - recipe[key]
    
    if can_make == True:
      batches += 1
  
  return batches
  
  
  
  # if not enough ingredients end
  # take recipe away from ingredients
  # pluse one recipe made
  # repeat


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))