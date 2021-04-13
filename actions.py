from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 
             'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 
			 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 
			 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 
			 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 
			 'Gangtok', 'Shimla']

def validate_location(loc,loc_list = WeOperate):
	loc_list = [i.lower() for i in loc_list]
	
	if loc.lower() in loc_list:
		return {'location_f' : 'found', 'location_new' : loc}
	elif loc.lower() not in loc_list:
		return {'location_f' : 'tier3', 'location_new' : None}
	else:
		return {'location_f' : 'notfound', 'location_new' : None}

def RestaurantSearch(loc,cuisine,price):
	#TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	
	location_data = ZomatoData[(ZomatoData['City'].apply(lambda x: loc.lower() in x.lower()))]
	
	cuisine_data = location_data[(location_data['Cuisines'].apply(lambda x: cuisine.lower() in x.lower()))]
	
	if price == "than 300":
		price_data = cuisine_data[(cuisine_data['Average Cost for two'].apply(lambda x: x < 300 ))]
	elif price == "700":
		price_data = cuisine_data[(cuisine_data['Average Cost for two'].apply(lambda x: 300 <= x <= 700 ))]
	else:
		price_data = cuisine_data[(cuisine_data['Average Cost for two'].apply(lambda x: x > 700 ))]
		
	TEMP = price_data.sort_values("Aggregate rating", ascending=False)
	
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]
	

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		
		price = tracker.get_slot('price')	
		
		dispatcher.utter_message(text="-------"+price)
		
		results = RestaurantSearch(loc,cuisine, price)
		
		top5 = results.head(5)
		
		response=""
		if results.shape[0] == 0:
			response= "no results"
		else:
			response = 'Your top five results:' + "\n"
			#for restaurant in RestaurantSearch(loc,cuisine,price).iloc[:5].iterrows():
			for index, restaurant in top5.iterrows():
				#restaurant = restaurant[1]
				#response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Rating text']} with avg cost {restaurant['Average Cost for two']} \n\n"
				response = response + str(restaurant['Restaurant Name']) + ' in ' + restaurant['Address'] + ' has been rated ' + str(restaurant['Aggregate rating']) + ' with avg cost Rs.' + str(restaurant['Average Cost for two']) + "\n"
				
		dispatcher.utter_message(str(response))
		return [SlotSet('location',loc)]

class Validate_location(Action):
	def name(self):
		return 'action_validate_location'
	
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		
		check = validate_location(loc)
		
		return [SlotSet('location',check['location_new']), SlotSet('location_found',check['location_f'])]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('mail_id')
		sendmail(MailID,response)
		return [SlotSet('mail_id',MailID)]