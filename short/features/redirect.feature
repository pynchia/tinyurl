Feature: Redirect short URL
		As an anonymous user
		I want to be able to use a short URL
		So that I can reach my target (through redirection)

		Scenario: using the short URL
				Given I have obtained a short URL already
				When I use the short URL (e.g. clicking on a link)
				Then I will be redirected to the original URL

