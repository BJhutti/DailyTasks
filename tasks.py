#
import requests
import webbrowser
import json
def getLc() -> str:
    query = '''
        query questionOfToday {
    activeDailyCodingChallengeQuestion {
        date
        userStatus
        link
        question {
        acRate
        difficulty
        freqBar
        frontendQuestionId: questionFrontendId
        isFavor
        paidOnly: isPaidOnly
        status
        title
        titleSlug
        hasVideoSolution
        hasSolution
        topicTags {
            name
            id
            slug
        }
        }
    }
    }
    '''

    payload = {'query' : query}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'  # Add this line if the API requires an access token
    }


    url = 'https://leetcode.com/graphql'

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return(data['data']['activeDailyCodingChallengeQuestion']['link'])
        
    else:
        print(f"Query failed with status code {response.status_code}")
        print(response.text)
        raise ValueError

urls = []
lcUrl = "https://leetcode.com" + getLc()
urls.append(lcUrl)

jsonData = open("urls.json")
d = (json.load(jsonData))
for urlPair in d["urls"]:
    urls.append(urlPair["url"])

for url in urls:

    webbrowser.open(url, new = 0, autoraise = True)