import requests

cookies = {
    'guest_id_marketing': 'v1%3A166313837055525235',
    'guest_id_ads': 'v1%3A166313837055525235',
    'dnt': '1',
    '_ga_BYKEBDM7DS': 'GS1.1.1669708614.1.0.1669708620.0.0.0',
    'kdt': 'fAK9ZitLQ2EAG1hs4sUD54Zw8QZFk5ft6XbtaUS9',
    'des_opt_in': 'Y',
    '_gcl_au': '1.1.1506057942.1669722822',
    'mbox': 'PC#05f7baf784ac4ffb9de628bd2afbbe17.32_0#1736228989|session#dbbb3fb16daf4cec8ea575d4890f016a#1672986049',
    '_ga_34PHSZMC42': 'GS1.1.1672984193.10.0.1672984193.0.0.0',
    '_ga': 'GA1.2.1325482072.1669123323',
    '_gid': 'GA1.2.482679539.1673871943',
    'gt': '1615257563607748610',
    'lang': 'en',
    'att': '1-KnbHgrMRc7csO8tBNJPkNfiGz3zXcKRqZJ96AQzv',
    'personalization_id': '"v1_JJ+z186K1ah09968irRfZw=="',
    'guest_id': 'v1%3A167394466258733916',
    'ct0': 'ba6836d7712b18f04220b8b3e475adc2',
    '_twitter_sess': 'BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCC%252FR4L6FAToMY3NyZl9p%250AZCIlN2U4NzA2M2ZhNDQxMzA1MGUzOTBhMmRhNWQ3ZmViYjM6B2lkIiU4YWFm%250AOWM4Y2U0NmU0ODgzNmNiYjlkMjQ5NTIwMzg0OA%253D%253D--82f25d01c6b4ad9a5a22ee2c71afb970d05be835',
}

headers = {
    'authority': 'api.twitter.com',
    'accept': '*/*',
    'accept-language': 'ko',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    # 'cookie': 'guest_id_marketing=v1%3A166313837055525235; guest_id_ads=v1%3A166313837055525235; dnt=1; _ga_BYKEBDM7DS=GS1.1.1669708614.1.0.1669708620.0.0.0; kdt=fAK9ZitLQ2EAG1hs4sUD54Zw8QZFk5ft6XbtaUS9; des_opt_in=Y; _gcl_au=1.1.1506057942.1669722822; mbox=PC#05f7baf784ac4ffb9de628bd2afbbe17.32_0#1736228989|session#dbbb3fb16daf4cec8ea575d4890f016a#1672986049; _ga_34PHSZMC42=GS1.1.1672984193.10.0.1672984193.0.0.0; _ga=GA1.2.1325482072.1669123323; _gid=GA1.2.482679539.1673871943; gt=1615257563607748610; lang=en; att=1-KnbHgrMRc7csO8tBNJPkNfiGz3zXcKRqZJ96AQzv; personalization_id="v1_JJ+z186K1ah09968irRfZw=="; guest_id=v1%3A167394466258733916; ct0=ba6836d7712b18f04220b8b3e475adc2; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCC%252FR4L6FAToMY3NyZl9p%250AZCIlN2U4NzA2M2ZhNDQxMzA1MGUzOTBhMmRhNWQ3ZmViYjM6B2lkIiU4YWFm%250AOWM4Y2U0NmU0ODgzNmNiYjlkMjQ5NTIwMzg0OA%253D%253D--82f25d01c6b4ad9a5a22ee2c71afb970d05be835',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-csrf-token': 'ba6836d7712b18f04220b8b3e475adc2',
    'x-guest-token': '1615257563607748610',
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ko',
}

json_data = {
    'flow_token': 'g;167394466258733916:-1673944687747:RltpsEjaL0jc5mKziSNJo2UV:0',
    'subtask_inputs': [
        {
            'subtask_id': 'AccountDuplicationCheck',
            'check_logged_in_account': {
                'link': 'AccountDuplicationCheck_false',
            },
        },
    ],
}

response = requests.post('https://api.twitter.com/1.1/onboarding/task.json', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"flow_token":"g;167394466258733916:-1673944687747:RltpsEjaL0jc5mKziSNJo2UV:0","subtask_inputs":[{"subtask_id":"AccountDuplicationCheck","check_logged_in_account":{"link":"AccountDuplicationCheck_false"}}]}'
#response = requests.post('https://api.twitter.com/1.1/onboarding/task.json', cookies=cookies, headers=headers, data=data)
print(response.text)
print("headers",response.headers)
print("cookies",response.cookies)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"flow_token":"g;167394466258733916:-1673944687747:RltpsEjaL0jc5mKziSNJo2UV:0","subtask_inputs":[{"subtask_id":"AccountDuplicationCheck","check_logged_in_account":{"link":"AccountDuplicationCheck_false"}}]}'
#response = requests.post('https://api.twitter.com/1.1/onboarding/task.json', cookies=cookies, headers=headers, data=data)