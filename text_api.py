from aylienapiclient import textapi
import api_access

client = textapi.Client(api_access.id, api_access.key)

sentiment = client.Sentiment({'text': 'Jhon is a very good football player'})
print sentiment
