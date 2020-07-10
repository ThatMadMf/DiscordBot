class CustomMember:

    def __init__(self, user_id, name=None):
        self.id = user_id
        self.name = name


def create_user(user_id, name):
    return CustomMember(user_id, name)
