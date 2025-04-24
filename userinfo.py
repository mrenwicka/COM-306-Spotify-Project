from spotifyinfo import spotify

class userinfo():
    def __init__(self):
        self.sp = spotify().get_client()
    
    def get_user_id(self):
        user_profile = self.sp.current_user()
        return user_profile['id']

    def get_username(self, id):
        info = self.sp.user(id)
        return info['display_name']
    
    def get_profile_pic(self, id):
        info = self.sp.user(id)
        profile_pic = info.get('images')
        return profile_pic[0]['url']

if __name__ == "__main__": 
    user_info = userinfo()
    user_id = user_info.get_user_id()
    print(user_info.get_username(user_id))
    print(user_info.get_profile_pic(user_id))