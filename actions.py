from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import smtplib

ZomatoData = pd.read_csv('zomato.csv',encoding = "ISO-8859-1")
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 
             'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 
			 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 
			 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 
			 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 
			 'Gangtok', 'Shimla']

results={}

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
	
	if price == "Low":
		price_data = cuisine_data[(cuisine_data['Average Cost for two'].apply(lambda x: x < 300 ))]
	elif price == "Medium":
		price_data = cuisine_data[(cuisine_data['Average Cost for two'].apply(lambda x: 300 <= x <= 700 ))]
	else:
		price_data = cuisine_data[(cuisine_data['Average Cost for two'].apply(lambda x: x > 700 ))]
		
	if len(price_data) == 0:
		TEMP = ""
	else:
		TEMP = price_data.sort_values(by='Aggregate rating', ascending=False)
		TEMP = TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]
	
	return TEMP

def sendmail(recipient,response):
	server_username = '@outlook.com'
	server_password = ''
	
	# Create Email 
	mail_from = server_username
	mail_to = recipient
	mail_subject = 'Your Restaurant Search Results'
	mail_message_body = response
	
	mail_message = '''\
	From: %s
	To: %s
	Subject: %s
	
	\n\n%s
	''' % (mail_from, mail_to, mail_subject, mail_message_body)
	
	server = smtplib.SMTP('smtp.office365.com', 587)
	server.ehlo()
	server.starttls()
	server.login(server_username, server_password)
	server.sendmail(mail_from, mail_to, mail_message)
	server.close()
		

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')		
		
		global results
		results = RestaurantSearch(loc,cuisine, price)
		
		response=""
		
		#if results.shape[0] == 0:
		if len(results) == 0:
			response= "no results"
		else:
			top10 = results.head(10)
			response = 'Your top results:' + "\n"
			#for index, restaurant in RestaurantSearch(loc,cuisine,price).iloc[:10].iterrows():
			for index, restaurant in top10.iterrows():
				#restaurant = restaurant[1]
				#response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Rating text']} with avg cost {restaurant['Average Cost for two']} \n\n"
				response = response + str(restaurant['Restaurant Name']) + ' in ' + restaurant['Address'] + ' has been rated ' + str(restaurant['Aggregate rating']) + ' with avg cost Rs.' + str(restaurant['Average Cost for two']) + "\n\n"
				
		dispatcher.utter_message(str(response))
		
		if len(results) == 0:
			return [SlotSet("restaurants_found","False")]
		else:
			return [SlotSet('location',loc),SlotSet("restaurants_found","True")]

class Validate_location(Action):
	def name(self):
		return 'action_validate_location'
	
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		
		check = validate_location(loc)
		
		return [SlotSet('location',check['location_new']), SlotSet('location_found',check['location_f'])]

class ActionValidateEmail(Action):
	def name(self):
		return 'action_validate_email'
	
	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('email')
		
		pattern = "[\w.%+-]+@[a-zA-Z]+[.]?[a-zA-Z]*{,2}[.a-zA-Z]{,3}"

class ActionSendMail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('email')
		
		top10 = results.head(10)
		
		try:
			sendmail(MailID,top10)
		except:
			dispatcher.utter_message("Error Sending Email.")
			return [SlotSet('email',MailID),SlotSet('email_sent','False')]
		else:
			dispatcher.utter_message("Email Sent")
			return [SlotSet('email',MailID),SlotSet('email_sent','True')]