import datetime
months_str_upper_case=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']



def get_date_str():
    date_now=datetime.datetime.now()
    date_formatted=str(date_now.day)+'/'+str(date_now.month)+' '+str(date_now.hour)+':'+str(date_now.minute)+':'+str(date_now.second)
    return date_formatted
