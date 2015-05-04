Feature: Redirect short URL
		As an anonymous user
		I want to be able to use a short URL
		So that I can reach my target (through redirection)

	Scenario: use an existing short URL
		Given "http://stackoverflow.com/questions/tagged/python" has a short URL
		When I use the short URL "http://localhost:8081/r/5/"
		Then I will be redirected to "http://stackoverflow.com/questions/tagged/python"
		And the number of hits of the short URL id "5" will increase

	Scenario: use a missing short URL(web)
		Given the short URL id "666" is missing
		When I use the short URL "http://localhost:8081/r/666/"
		Then I will be redirected to the home page

