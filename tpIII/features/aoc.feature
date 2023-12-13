Feature: Every solution should run quickly and not throw any error

    Scenario Outline: A solution should not last longer than 1 second
        Given a <day> solution
        When I run the solution
        Then the solution should not last longer than <max_time> second

        Examples:
            | day | max_time |
            | 01  | 1        |
            | 02  | 1        |
            | 03  | 1        |
            | 04  | 1        |
            | 05  | 1        |
            | 06  | 1        |
            | 07  | 1        |
            | 08  | 1        |
            | 09  | 1        |
            | 10  | 5        |
            | 11  | 1        |

    Scenario Outline: A solution should not throw any error
        Given a <day> solution running
        When I run the solution with the input
        Then the solution should not throw any error

        Examples:
            | day |
            | 01  |
            | 02  |
            | 03  |
            | 04  |
            | 05  |
            | 06  |
            | 07  |
            | 08  |
            | 09  |
            | 10  |
            | 11  |