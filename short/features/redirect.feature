Feature: Redirect short URL
		As an anonymous user
		I want to be able to use a short URL
		So that I can reach my target (through redirection)

		Scenario: through a webpage, obtain a shorter URL
				Given I go the the homepage
				When I post a URL in the form
				Then I will see the resulting shorter URL

		Scenario: through a RESTful API, obtain a shorter URL
				Given I call the api properly
				When I post a URL to the server
				Then I will receive the resulting shorter URL

