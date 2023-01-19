import requests

# 15374f013b29c45f162439cd618f65572f4b3e52
# 7d65a6ac19c21cef946f3483f8d32e044a60a609
# 7d65a6ac19c21cef946f3483f8d32e044a60a609
# 7d65a6ac19c21cef946f3483f8d32e044a60a609
# a48008203dbb807579e7ec5f56e0881116d32f93
# a48008203dbb807579e7ec5f56e0881116d32f93 firefox
# 7d65a6ac19c21cef946f3483f8d32e044a60a609
# 7d65a6ac19c21cef946f3483f8d32e044a60a609 

# google 30b32b0cbf89ee9d94929294ff19ea330b2e5ec8
# firefo b8c230fc7afa0b296976b08ff1d64d85b8f62241
# ?????? 7d65a6ac19c21cef946f3483f8d32e044a60a609
import requests

cookies = {
    'guest_id_marketing': 'v1%3A166313837055525235',
    'guest_id_ads': 'v1%3A166313837055525235',
    'dnt': '1',
    '_ga_BYKEBDM7DS': 'GS1.1.1669708614.1.0.1669708620.0.0.0',
    'kdt': 'fAK9ZitLQ2EAG1hs4sUD54Zw8QZFk5ft6XbtaUS9',
    'des_opt_in': 'Y',
    '_gcl_au': '1.1.1506057942.1669722822',
    '_gid': 'GA1.2.482679539.1673871943',
    'mbox': 'PC#05f7baf784ac4ffb9de628bd2afbbe17.32_0#1737271029|session#7056c40a8bd04010a69434978a3d7dea#1674028089',
    '_ga_34PHSZMC42': 'GS1.1.1674021575.13.1.1674026247.0.0.0',
    '_ga': 'GA1.2.1325482072.1669123323',
    'personalization_id': '"v1_Yz5jw4CNKOtvsysZSxe4yQ=="',
    'guest_id': 'v1%3A167404840376943552',
    'ct0': 'e0698b82bf5ce6c36b5996329593c426',
    'external_referer': 'padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D',
    'att': '1-Y754D5cY8qUt7GrzIKLbKKbacJrDHfJJnPkOgQnH',
    '_twitter_sess': 'BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCLdGHMiFAToMY3NyZl9p%250AZCIlMzJhMGExYjQ3ZDYwNWUzOWNhNjQ3OGQ1MmEyOWMzNDY6B2lkIiUyNWI4%250AYmM0YmUxNTc4ZGM2MDM2MGJmN2QyNWNkMDNiYw%253D%253D--5a9ba6ddf763e5d31748048663af3e43f474fe0a',
    'gt': '1615916841410625538',
}

headers = {
    'authority': 'api.twitter.com',
    'accept': '*/*',
    'accept-language': 'ko',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    # 'cookie': 'guest_id_marketing=v1%3A166313837055525235; guest_id_ads=v1%3A166313837055525235; dnt=1; _ga_BYKEBDM7DS=GS1.1.1669708614.1.0.1669708620.0.0.0; kdt=fAK9ZitLQ2EAG1hs4sUD54Zw8QZFk5ft6XbtaUS9; des_opt_in=Y; _gcl_au=1.1.1506057942.1669722822; _gid=GA1.2.482679539.1673871943; mbox=PC#05f7baf784ac4ffb9de628bd2afbbe17.32_0#1737271029|session#7056c40a8bd04010a69434978a3d7dea#1674028089; _ga_34PHSZMC42=GS1.1.1674021575.13.1.1674026247.0.0.0; _ga=GA1.2.1325482072.1669123323; personalization_id="v1_Yz5jw4CNKOtvsysZSxe4yQ=="; guest_id=v1%3A167404840376943552; ct0=e0698b82bf5ce6c36b5996329593c426; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; att=1-Y754D5cY8qUt7GrzIKLbKKbacJrDHfJJnPkOgQnH; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCLdGHMiFAToMY3NyZl9p%250AZCIlMzJhMGExYjQ3ZDYwNWUzOWNhNjQ3OGQ1MmEyOWMzNDY6B2lkIiUyNWI4%250AYmM0YmUxNTc4ZGM2MDM2MGJmN2QyNWNkMDNiYw%253D%253D--5a9ba6ddf763e5d31748048663af3e43f474fe0a; gt=1615916841410625538',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    #'x-csrf-token': 'e0698b82bf5ce6c36b5996329593c426',
    'x-guest-token': '1615916841410625538',
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ko',
}

params = {
    'include_profile_interstitial_type': '1',
    'include_blocking': '1',
    'include_blocked_by': '1',
    'include_followed_by': '1',
    'include_want_retweets': '1',
    'include_mute_edge': '1',
    'include_can_dm': '1',
    'include_can_media_tag': '1',
    'include_ext_has_nft_avatar': '1',
    'include_ext_is_blue_verified': '1',
    'include_ext_verified_type': '1',
    'skip_status': '1',
    'cards_platform': 'Web-12',
    'include_cards': '1',
    'include_ext_alt_text': 'true',
    'include_ext_limited_action_results': 'false',
    'include_quote_count': 'true',
    'include_reply_count': '1',
    'tweet_mode': 'extended',
    'include_ext_collab_control': 'true',
    'include_ext_views': 'true',
    'include_entities': 'true',
    'include_user_entities': 'true',
    'include_ext_media_color': 'true',
    'include_ext_media_availability': 'true',
    'include_ext_sensitive_media_warning': 'true',
    'include_ext_trusted_friends_metadata': 'true',
    'send_error_codes': 'true',
    'simple_quoted_tweet': 'true',
    'q': 'russia',
    'tweet_search_mode': 'live',
    'count': '20',
    'query_source': 'typed_query',
    'pc': '1',
    'spelling_corrections': '1',
    'include_ext_edit_control': 'true',
    'ext': 'mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,enrichments,superFollowMetadata,unmentionInfo,editControl,collab_control,vibe',
}

response = requests.get('https://api.twitter.com/2/search/adaptive.json', params=params,  headers=headers)
response_json = response.json()

print("response_json",response_json)

"""print("response",response)
print("response.text",response.text)
print("headers",response.headers)
print("cookies",response.cookies)
print("status_code",response.status_code)
print("elapsed",response.elapsed)
print("history",response.history)
print("reason",response.reason)
print("request",response.request)
print("url",response.url)"""