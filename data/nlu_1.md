## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thanks bye
- send
- send details at xyz@yahoo.com

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hello!
- hola

## intent:help
- I need a help
- I need help
- Can you help me?
- I need suggestions

## intent:restaurant_search
- find restaurant
- restaurant
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Mexican](cuisine)
- [American](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- lesser than Rs. 300(price)
- [less than Rs. 300](price:lesser than 300)
- [<300](price:lesser than 300)
- [< 300](price:lesser than 300)
- [less than 300 rupees](price:lesser than 300)
- [not more than 300](price:lesser than 300)
- [>300](price:between 300 to 700)
- between 300 to 700(price)
- [no limit](price:more than 700)
- range 300-700(price)
- more than 700(price)
- lesser than 300(price)

## intent:deny
- no
- dont send
- donot send
- no thanks
- no mail
- no email
- no email please

intent:send_mail
 - abc@yahoo.com
 - abc@gmail.com
 - abc@outlook.com

## synonym:4
- four

## synonym:New Delhi
- Delhi
- delli
- delhi

## synonym:Bangalore
- Bengaluru
- bglr
- bangalore
- bengaluru

## synonym:Baroda
- Vadodara
- baroda
- vadodara

## synonym:Calcutta
- Kolkata
- kolkata
- calutta

## synonym:Chennai
- Madras
- madras
- chennai

## synonym:Cochin
- Kochi

## synonym:Gurgaon
- Gurugram

## synonym:Mumbai
- Bombay

## synonym:Mysore
- Mysuru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:email
- [A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,64}