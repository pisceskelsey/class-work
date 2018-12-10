def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('kelsey', 'morgan', location='seattle', study='library sciences', age='23')
print(user_profile)

make_car = {'brand', 'make', 'color', 'extras'}
car = make_car('honda', 'crv', color='grey', tow_package=True)