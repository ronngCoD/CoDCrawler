import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("JPTDYUTk5FFA22yDXUwWqNA4F", "r8ySz1orfQTNNmT3TP7UULxuRTF4KMWHFKXqYZ7XXxD2077H3F")
auth.set_access_token("1420930922401042433-OiqKEN7MPbagVBVTb8bREvFCEesq3Y", "4Cm7LikMZ502ZBrCQvrPDAjz42ioFCfTpwXm8uLH"
                                                                            "LsiOD")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
