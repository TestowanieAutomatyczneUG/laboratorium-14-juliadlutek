Feature: password validator

  Scenario Outline: check if password is valid
    Given there is password validator
    When we check password <password>
    Then result is <result>
    Examples:
      | password   | result |
      | Password1$ | 1  |
      | P1$        | 0  |
      | Password$  | 0  |
      | pasword$   | 0  |
      | Password1  | 0  |