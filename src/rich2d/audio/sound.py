from pygame.mixer import Sound as PygameSound

def Sound(file_name=None):
    if file_name is None:
        raise RuntimeError("Sound file_name cannot be None")
    return PygameSound(file_name)