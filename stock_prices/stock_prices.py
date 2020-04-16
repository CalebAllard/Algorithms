#!/usr/bin/python

import argparse

def find_max_profit(prices):
  buy = prices[0]
  p = 0
  largest_sell = 0
  max_profit = 0
  for i in range(0, len(prices) - 1):
    if prices[i] < buy:
      buy = prices[i]
      p = i
      split = prices[i + 1:]
  for i in range(0,len(split)):
    if split[i] > largest_sell:
      largest_sell = split[i]  
  print(largest_sell,buy)
  max_profit = largest_sell - buy
  return max_profit
  #find high and low prices
    #loop through array of prices
    #Keep track of low and high
    #use last high and low
  #Subtract low from high


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))