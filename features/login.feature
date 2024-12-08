Feature: Login Guru99 Demo

    @smoke
    Scenario: Logo presence on Guru99 Demo
      Given user launch chrome browser
      When user navigated to Guru99 Demo Login
      When user login using "test@gmail.com" and "123456"
      Then user was able to navigate to Homepage successfully

      @regression
      Scenario Outline:
        Given user launch chrome browser
        When user navigated to Guru99 Demo Login
        When user login using "<username>" and "<password>"
        Then user was able to navigate to Homepage successfully
        Examples:
          | username       | password |
          | test@gmail.com | 123456 |
          | abdsqwe        | abdsqwe |