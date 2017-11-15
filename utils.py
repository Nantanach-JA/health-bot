from wit import Wit

access_token = "WMN4JBK2HPW66APORX65EHLLJBYGEPMF"
client = Wit(access_token = access_token)

def wit_response(message_text):
    resp = client.message(message_text)

    entity = None
    value = None

    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']

    except:
        pass

    #if(entity1 == "age_of_person"): return ("อายุ " + value + "แล้วเหรอ")
    #elif (entity1 == "type" & entity2 == "amount"): return ("กิน"+ value1 + "มา " + value2 + " จานเหรอ")

    return (entity,value)