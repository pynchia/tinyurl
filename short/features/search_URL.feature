Feature: Searching for URLs
		As an anonymous user
		I want to search for a URL
		So that I can find out what is in the archive and their stats

	Scenario: search for a URL substring
		Given I go to the homepage
		When I post "https://docs.djangoproject.com/en/dev/topics/testing/tools/" in the homepage form
		Then the page will show the short URL for "https://docs.djangoproject.com/en/dev/topics/testing/tools/"

