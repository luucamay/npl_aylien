from aylienapiclient import textapi

client = textapi.Client("e8236a4b", "b1aa1bfbad32a44841f007d29848213f")

sentiment = client.Sentiment({'text': 'Jhon is a very good football player'})
print sentiment
