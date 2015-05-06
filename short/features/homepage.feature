Feature: Homepage
	Scenario: homepage is displayed correctly
		Given I go to the homepage
		Then the homepage shows a form for creating a new short URL
		And the homepage shows a form for searching existing URLs
