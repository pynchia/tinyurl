Feature: Homepage
	Scenario: homepage is displayed correctly
		When I go to the homepage
		Then the page shows a form for creating a new short URL
		And the page shows a link to search for URLs
