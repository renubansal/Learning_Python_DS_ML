import requests  #install these 2 packages using pip if not already present
import json

access_token = 'the_access_token_goes_here'
def get_page_data(page_id):
        url = 'https://graph.facebook.com/v2.0/'+ str(page_id)+'/feed?limit=70&access_token='+access_token
        data = requests.get(url)
        response = json.loads( data.text )
        for post in response['data']:
                print post['message']
                print "\n\n"
get_page_data(the_page_id_goes_here) # calling the function created above
