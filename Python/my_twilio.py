from twilio.rest import TwilioRestClient

accountSid = "AC4ab83753af8ca5f47a1f40b7d009337c"
authToken = "1fb2c00931d94e54fb6090fb172805d6"
twilioClient = TwilioRestClient(accountSid, authToken)
myTwilioNumber = "+13346974772"
destCellPhone = "+919833805193"
myMessage = twilioClient.messages.create(body = "hello, my name is deepak dewani", from_=myTwilioNumber, to=destCellPhone)
