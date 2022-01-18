Feature: password validator

  Scenario Outline: check if password is valid
    Given there is simple class with function for adding 1
    When we add 1 to <number>
    Then result is <result>
    Examples:
      | number   | result |
      | 10       | 11     |
      | 0        | 1      |
      | -5       | -4     |
      | 2.25     | 3.25   |
      | -1.5     | -0.5   |