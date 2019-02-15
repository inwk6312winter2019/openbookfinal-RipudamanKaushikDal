import createticket, requests
import json
tick=createticket.get_ticket()
def getNetworkCount(ticket):
        controller='devnetapi.cisco.com/sandbox/apic_em'

        # URL for network-device REST API call to get list of exisiting devices on the network.
        url = "https://" + controller + "/api/v1/host/count"

        #Content type as well as the ticket must be included in the header 
        header = {"content-type": "application/json", "X-Auth-Token":ticket}
        # this statement performs a GET on the specified network device url
        response = requests.get(url, headers=header, verify=False)

        # json.dumps serializes the json into a string and allows us to
        # print the response in a 'pretty' format with indentation etc.
        print ("Hosts = ")
        print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

        #convert data to json format.
        r_json=response.json()

        print(r_json)

getNetworkCount(tick)
