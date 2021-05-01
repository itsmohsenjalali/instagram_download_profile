import instaloader
from instaloader import RateController

L = instaloader.Instaloader()
UserName = "startuplink_isf"
posts = instaloader.Profile.from_username(L.context, UserName).get_posts()
controller = RateController(L.context)
L.login('UserName', 'Password')
controller.handle_429('iphone')
for post in posts:
    print(post.date)
    L.dirname_pattern = f'{UserName}/{str(post.date).replace(":", "-")}/'
    L.download_post(post, UserName)
