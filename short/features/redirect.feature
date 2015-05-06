Feature: Redirect short URL
		As an anonymous user
		I want to be able to use a short URL
		So that I can reach my target (through redirection)

	Scenario: use an existing short URL
		# Given "http://pythonhosted.org/behave/tutorial.html#python-step-implementations" has a short URL
		Given the set of URLs are in the DB
			| url |
			| http://pythonhosted.org/behave/tutorial.html#python-step-implementations |
		When I use the short URL of long URL "http://pythonhosted.org/behave/tutorial.html#python-step-implementations"
		Then I will be redirected to "http://pythonhosted.org/behave/tutorial.html#python-step-implementations"
		And the number of hits of the short URL id "5" will increase

	Scenario: use a missing short URL(web)
		Given the short URL id "666" is missing
		When I go to the page "http://localhost:8081/r/666/"
		Then I will be redirected to the homepage

