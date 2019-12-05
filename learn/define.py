# def greet_user(username = 'world'):
#     """显示简单的问候语"""
#     print("Hello, " + username.title() + "!")
#
# greet_user()

# def make_shirt(size, word='I love Python'):
#     print("\nThe shirt size is " + size + ", and word is " + word + "." )
#
# make_shirt(size='40')

# def get_name(first_name, last_name):
#     full_name = first_name + "  " + last_name
#     return full_name.title()
# name = get_name('yang', 'xiaochuan')
# print(name)

def greet_users(names):
    for name in names:
        print("\nHello " + name.title() + "!")

users_list=["alice", "bob", "candy"]
greet_users(users_list)