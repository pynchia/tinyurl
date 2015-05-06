Feature: Homepage
	Scenario: homepage is displayed correctly
		When I go to the page "http://localhost:8081/"
		Then the page shows a form for creating a new short URL
		And the page shows a form for searching existing URLs
