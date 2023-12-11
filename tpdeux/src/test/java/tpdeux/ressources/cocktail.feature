Feature: Cocktail Ordering

  As Romeo, I want to offer a drink to Juliette so that we can discuss together (and maybe more).

    Scenario Outline: Creating an empty order
      Given "<owner>" who wants to buy a drink
      When an order is declared for "<target>"
      Then there is <nbCocktails> cocktails in the order

      Examples:
        | owner | target   | nbCocktails |
        | Romeo | Juliette |           0 |
        | Tom   | Jerry    |           0 |