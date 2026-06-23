#Using if-else statements in writing about sumertimes

#Summer months: June, July, August

def summer_activity(temperature):
    if temperature >= 40:
        activity = "Stay indoors and drink lots of water!"
    elif temperature >= 30:
        activity = "Perfect for a swim at the beach!"
    elif temperature >= 20:
        activity = "Great day for picnic in the park!"
    else:
        activity = "Too cold for summer activities!"
    return activity

print("Summer activity Suggestions by Temperature:")
temperatures = [42, 35, 25]
for temp in temperatures:
    activity = summer_activity(temp)
    print(f"{temp} to {activity}")