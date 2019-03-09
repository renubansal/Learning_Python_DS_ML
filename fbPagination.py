import requests
import json

access_token = 'the_access_token_goes_here'
def get_page_data(page_id):
        url = 'https://graph.facebook.com/'+ str(page_id)+'/feed?limit=25&access_token='+access_token  # the limit attribute specifies the limit of entries in one page
        data = requests.get(url)
        response = json.loads( data.text )
next_page = response['paging']['next']
       while next_page:
               print "Found next page"
               response = json.loads(requests.get(next_page).text)
               if 'paging' in response:
                       if 'next' in response['paging']:
                               next_page = response['paging']['next']
                       else:
                               print "next not found"
                               next_page = None
               else:
                       print "Paging not found\n"
                       next_page = None
get_page_data(the_page_id_goes_here)
