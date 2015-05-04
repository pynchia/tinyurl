Feature: Redirect short URL
		As an anonymous user
		I want to be able to use a short URL
		So that I can reach my target (through redirection)

	@web @rest
	Scenario: use an existing short URL
		Given I have obtained a short URL already
		When I use the short URL (e.g. clicking on a link)
		Then I will be redirected to the original URL

	@web
	Scenario: use a missing short URL(web)
		When I access the missing short URL via web
		Then I will be redirected to the home page

	@rest
	Scenario: use a missing short URL(rest)
		When I access the missing short URL via REST
		Then I will receive an error

