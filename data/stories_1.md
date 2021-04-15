## complete path 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
	- slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_pricerange
* restaurant_search{"price": "High"}
	- slot{"price": "High"}
	- action_search_restaurants
	- utter_ask_email
* restaurant_search{"email": "xyz@yahoo.com"}	
	- slot{"email": "xyz@yahoo.com"}
	- action_send_email
	- utter_email_sent
* goodbye
	- utter_goodbye
	- action_restart

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bokhanok"}
    - slot{"location": "bokhanok"}
	- action_validate_location
	- slot{"location": null}
	- slot{"location_found": "notfound"}
    - utter_location_not_found
* restaurant_search{"location": "mumbai"}
	- slot{"location": "mumbai"}
	- utter_ask_cuisine	
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_pricerange
* restaurant_search{"price": "High"}
	- slot{"price": "High"}
	- action_search_restaurants
	- utter_ask_email
	- utter_email_sent
* goodbye
	- utter_goodbye
	- action_restart

