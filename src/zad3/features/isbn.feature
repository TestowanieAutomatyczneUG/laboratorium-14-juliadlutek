Feature: password validator

  Scenario Outline: check if password is valid
    Given there is ISBN class with function for checking control number
    When we check control number for ISBN <number>
    Then result is <result>
    Examples:
      | number            | result |
      | 978-3-16-148410-0 | 0      |
      | 9780143105428     | 0      |
      | 097-8-01-43105-4  | 8      |
      | 000-0-00-00000-0  | 0      |
      | 100-0-00-00000-0  | 9      |
      | 010-0-00-00000-0  | 7      |
      | 023-2-34-43565-6  | 1      |
      | 012-3-45-67891-0  | 4      |
      | 123-4-56-78910-1  | 9      |
      | 200-1-07-22000-0  | 6      |

