## Generated Story -430479576157305121
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "< 300"}
    - slot{"budget": "< 300"}
    - action_validate_budget
	- slot{"budget": "low"}
    - utter_top_restaurant
    - action_restaurant
    - utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "duttagoutam@hotmail.com"}
    - slot{"email": "duttagoutam@hotmail.com"}
    - action_validate_email
    - slot{"email": "duttagoutam@hotmail.com"}	
    - action_email
    - utter_goodbye
    - action_restart

## Generated Story -9135816461166457680
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "< 300"}
    - slot{"budget": "< 300"}
    - action_validate_budget
    - slot{"budget": "low"}
    - utter_top_restaurant
    - action_restaurant
    - utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "duttagoutam@hotmail.com"}
    - slot{"email": "duttagoutam@hotmail.com"}
    - action_validate_email
    - slot{"email": "duttagoutam@hotmail.com"}
    - action_email
    - utter_goodbye
    - action_restart

## Generated Story -1028867403149453728
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "< 300"}
    - slot{"budget": "< 300"}
    - action_validate_budget
    - slot{"budget": "low"}
    - utter_top_restaurant
    - action_restaurant
    - utter_ask_about_emailing
* greet
    - utter_goodbye
    - action_restart

## Generated Story -1726634712765027217
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_validate_location
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_validate_budget
    - slot{"budget": "high"}
    - utter_top_restaurant
    - action_restaurant
    - slot{"budget": "average cost for two > 700"}
    - utter_ask_about_emailing
* send_email{"email": "duttagoutam@hotmail.com"}
    - slot{"email": "duttagoutam@hotmail.com"}
    - utter_goodbye
    - action_restart

## Generated Story 7810953844218958905
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_validate_cuisine
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"budget": "300 - 700"}
    - slot{"budget": "300 - 700"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_restaurant
    - utter_ask_about_emailing
* send_email{"email": "duttagoutam@hotmail.com"}
    - slot{"email": "duttagoutam@hotmail.com"}
    - utter_goodbye
    - action_restart

## Generated Story -1115327033583795088
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
	- slot{"cuisine": "thai"}
    - action_validate_cuisine
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"budget": "300 - 700", "location": "range"}
    - slot{"budget": "300 - 700"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_restaurant
    - utter_ask_about_emailing
* send_email{"email": "duttagoutam@hotmail.com"}
    - slot{"email": "duttagoutam@hotmail.com"}
    - utter_goodbye
    - action_restart

## Generated Story 2182004289715809328
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_validate_location
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "> 700"}
    - slot{"budget": "> 700"}
	- action_validate_budget
	- slot{"budget": "high"}
    - utter_top_restaurant
    - action_restaurant
    - slot{"budget": "average cost for two > 700"}
    - utter_ask_about_emailing
* send_email{"email": "boomba.dutta@gmail.com"}
    - slot{"email": "boomba.dutta@gmail.com"}
    - action_validate_email
    - slot{"email": "boomba.dutta@gmail.com"}
    - action_email
    - utter_goodbye
    - action_restarted

## Generated Story -2892949591761075718
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
    - utter_top_restaurant
    - action_restaurant
    - slot{"budget": "average cost for two more than 300"}
    - utter_ask_about_emailing
* send_email{"email": "@kp.com"}
    - slot{"email": "@kp.com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_email_id
* send_email{"email": "boomba.dutta@gmail.com"}
    - slot{"email": "boomba.dutta@gmail.com"}
    - action_validate_email
    - slot{"email": "boomba.dutta@gmail.com"}
    - action_email
    - slot{"email": "boomba.dutta@gmail.com"}
    - utter_goodbye
    - action_restarted

## greet and 3 stage dialog with email - city  ->budget-> cuisine
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - action_validate_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
	- action_validate_cuisine
	- slot{"cuisine": "Thai"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "duttagoutam@hotmail.com"}
	- action_validate_email
	- slot{"email": "duttagoutam@hotmail.com"}
	- action_email
	- utter_goodbye
    - action_restarted

## greet and 3 stage dialog with email - city -> cuisine ->budget
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.in"}
	- action_validate_email
	- slot{"email": "xyz@test.in"}
	- action_email
	- utter_goodbye
    - action_restarted

## 3 stage dialog with email - city  ->budget-> cuisine
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - action_validate_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
	- action_validate_cuisine
	- slot{"cuisine": "Thai"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.edu"}
	- action_validate_email
	- slot{"email": "xyz@test.edu"}
	- action_email
	- utter_goodbye
    - action_restarted

## greet and 2 stage dialog with email - budget last
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "Italian"}
    - action_validate_location
	- slot{"location": "Mumbai"}
    - action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.gov"}
	- action_validate_email
	- slot{"email": "xyz@test.gov"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## greet and 2 stage dialog with email - cuisine last
* greet
    - utter_greet
* restaurant_search{"location": "New Delhi", "budget": "less than 700"}
    - action_validate_location
	- slot{"location": "New Delhi"}
	- slot{"budget": "less than 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.co.in"}
	- action_validate_email
	- slot{"email": "xyz@test.co.in"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## greet 2 stage dialog with email - city last
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "budget": "more than 700"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Bhopal"}
    - action_validate_location
	- slot{"location": "Bhopal"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## greet and 2 stage dialog with email - budget last
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## greet and 2 satage dialog without email - budget last
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "Italian"}
    - action_validate_location
	- slot{"location": "Mumbai"}
    - action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## greet and 2 stage dialog without email - cuisine last
* greet
    - utter_greet
* restaurant_search{"location": "New Delhi", "budget": "less than 300"}
    - action_validate_location
	- slot{"location": "New Delhi"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## greet 2 stage dialog without email - city last
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "budget": "more than 700"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Bhopal"}
    - action_validate_location
	- slot{"location": "Bhopal"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## greet and 2 stage dialog without email - budget last
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted		

## Generated Story -4292104932419660849
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restarted

## Generated Story -7873005728251281476
* greet
    - utter_greet
* out_of_scope
    - utter_default
    - utter_goodbye
    - action_restarted

