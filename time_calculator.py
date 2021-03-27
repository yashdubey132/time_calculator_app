def add_time(time, add, day = None):

    #initialize weekdays
    days_of_the_week = ["sunday", "monday", "tuesday","wednesday", "thursday", 
    "friday", "saturday"]

    #convert time to 24 hour format and flag noon variable
    noon = time.split()[1]
    if (noon == "PM"):
        #hours with 12 added for 24_hour format
        hours_24 = int(time.split()[0].split(":")[0]) + 12
    else:
        #hours as is
        hours_24 = int(time.split()[0].split(":")[0])
    # minutes as integer
    minutes_24 = int(time.split()[0].split(":")[1])
    # minute component to be added
    add_minutes = int(add.split(":")[1])
    sum_minutes = minutes_24 + add_minutes
    # initialize rollover hour
    rollover_hour = 0
    if sum_minutes >= 60:
        final_minutes = sum_minutes % 60
        #add one hour to final hour tally
        rollover_hour = 1
    else:
        final_minutes = sum_minutes
    # hour component to be added
    add_hours = int(add.split(":")[0])

    #get final total of hours - can exceed 24 hours
    sum_hours = hours_24 + add_hours + rollover_hour
    # final hours to print
    final_hours = sum_hours % 24 
    if final_hours == 0:
        final_hours_str = "12"
    else:
        final_hours_str = str(final_hours)
    
    # get number of days to move ahead by
    n_days = int(sum_hours / 24)
    #toggle AM or PM based on final hours
    if (final_hours < 12):
        final_noon = "AM"
    else:
        final_noon = "PM"
        final_hours = final_hours - 12
        final_hours_str = str(final_hours)
    if final_minutes <  10:
        final_minutes_str = "0" + str(final_minutes)
    else:
        final_minutes_str = str(final_minutes)
    # handle day cycles
    if day != None:
        index = days_of_the_week.index(day.lower())
        final_index = (index + n_days) % 7
        final_day = days_of_the_week[final_index]
    else:
        final_day = ""
    #final return
    if day != None:
        print (final_hours_str +":" + final_minutes_str + " "+ 
        final_noon + " " + final_day + " " + "(" + str(n_days) + " days later)")
    else:
        print( final_hours_str+ ":" + final_minutes_str +" " + final_noon + " " 
        "(" + str(n_days)+ " days later)")
    
        
    
    

    
add_time("4:30 PM", "5:10", "FRIDAY")




