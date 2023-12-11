# language: sv
Egenskap: Är det redan fredag?
  Alla vill veta när det är fredag

  Scenario: Söndag är inte fredag
    Givet att idag är söndag
    När jag frågar om det redan är fredag
    Så bör jag få svaret "Nej"
    Exempel:
      | day            | answer |
      | fredag         | Ja     |
      | söndag         | Nej    |
      | anything else! | Nej    |
