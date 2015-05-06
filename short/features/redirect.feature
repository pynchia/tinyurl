Feature: Redirect short URL
		As an anonymous user
		I want to be able to use a short URL
		So that I can reach my target (through redirection)

	Scenario Outline: use an existing short URL
		Given the set of URLs are added to the DB
			| url        |
			| <long_url> | 
		When I use the short URL of long URL "<long_url>"
		Then I will be redirected to "<long_url>"
		And the number of hits of the long URL "<long_url>" will be "1"

		Examples: long URLs
			| long_url |
			| http://pythonhosted.org/behave/tutorial.html#python-step-implementations |

	Scenario: use a missing short URL(web)
		Given the short URL id "666" is missing
		When I go to the page "http://localhost:8081/r/666/"
		Then I will be redirected to the homepage

