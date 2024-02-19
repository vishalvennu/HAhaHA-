def format_duration(seconds):
    if seconds == 0 : return "now"
    temp = {}
    temp["years"], rem = divmod(seconds, 3600*365*24)
    temp["days"], rem = divmod(rem, 3600*24)
    temp["hours"], rem = divmod(rem, 3600)
    temp["minutes"], temp["seconds"] = divmod(rem, 60)
    
    # format_output(years = years, days = days, hours = hours, minutes = minutes, seconds = secs)
    # print(f"{years} years {days} days {hours} hours {minutes} minutes and {secs} seconds",)
    
    temp = {key:value for key,value in temp.items() if value != 0}
    print(temp)
    
    l = None
    if len(temp.keys()) > 1:
        l = list(temp.keys())[-2]
    output = ""    
    for key,value in temp.items():
        if value == 1:
            output += str(value)+" "+key[:-1]+" "
        else:
            output += str(value)+" "+key+" "
        if key == l:
            output += "and "
    print(output[:-1])
format_duration(341201)