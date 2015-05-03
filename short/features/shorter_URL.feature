Feature: Shorter URL
		As an anonymous user
		I want to be able to obtain a uri shorter than the one I give
		So that I can save typing/space and use it on twitter

		Scenario: through a webpage, obtain a shorter URL
				Given I go the the homepage
				When I post the URL in the form
				Then I will see the resulting shorter URL

		Scenario: through a RESTful API, obtain a shorter URL
				Given I call the api properly
				When I post the URL to the server
				Then I will receive the resulting shorter URL

