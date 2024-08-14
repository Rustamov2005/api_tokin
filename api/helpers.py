import uuid


class SaveMediaFiles(object):
    def save_artist_image(instance, filename):
        image_path = filename.split('.')[-1]
        return f"artist/{uuid.uuid4()}.{image_path}"

    def save_album_image(instance, filename):
        image_path = filename.split('.')[-1]
        return f"album/{uuid.uuid4()}.{image_path}"

    def save_song_image(instance, filename):
        image_path = filename.split('.')[-1]
        return f"song/{uuid.uuid4()}.{image_path}"