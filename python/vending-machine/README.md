# Vending Machine

## Problem statement
Program a vending machine internals to accept and return cash coins.

## High-level design
- we are focussing on the internals so we really only care about the coin inventory here
- class for vending machine
  - initialize with some coins
  - add method for accepting cash coins
    - this method should update the inventory and track a running inserted total
  - add method for calculating change to return
    - should take the total inserted, the price of item and find the difference in coins
  - add method for dispensing cash
    - once calculated, this method is responsible for finding the exact coins needed
