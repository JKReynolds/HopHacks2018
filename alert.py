from twilio.rest import Client

account_sid = "AC7fd163ad726a3cefc43efbd697653daa"
auth_token  = "2d938a87cc03628186c9449bae9abbb6"

locationString = "https://www.google.com/maps/search/google+maps/@38.9260783,-77.328723"
name = "John Smith"


client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+13024634692", 
    from_="++16104865014",
    body="ALERT: Your loved one, " + name + " seems to be a little off course from their normal routine. They are currently at " + locationString)

print(message.sid)
