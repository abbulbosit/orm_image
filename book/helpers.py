import uuid


class Change_name(object):
    def change(instanse, filename):
        image_ = filename.split('.')[-1]
        return f'book/{uuid.uuid4()}.{image_}'