with open('your file path','r', encoding='utf-8') as files:
    
    client_currency = None



    for line in files:
        
        if '"client_currency":'in line :
            client_currency_start_index = line.find('"client_currency":') + len('"client_currency":')
            client_currency_end_index = line.find(',', client_currency_start_index)
            if client_currency_end_index == -1:
                client_currency_end_index = line.find('}', client_currency_start_index)
            client_currency = line[client_currency_start_index:client_currency_end_index].strip().strip('"')


        if client_currency:
            print(f"{client_currency}")
            client_currency = None
