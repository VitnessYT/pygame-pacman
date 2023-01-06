import pygame
import os


class ResourceNotFoundException(Exception):
    pass


class Resource:
    IMAGE = 0
    SOUND = 1
    def __init__(self, res_type: int, path: str):
        if not os.path.exists(path):
            raise ResourceNotFoundException(f"Resource is required and missing: {path}")

        self.type = res_type
        self.path = path
        if self.type == Resource.IMAGE:
            self.resource = pygame.image.load(path)
        elif self.type == Resource.SOUND:
            self.resource = pygame.mixer.Sound(path)


class ResourceLoader:
    resources = None
    loaded = None
    resources_to_load = None

    @staticmethod
    def setup(resources):
        ResourceLoader.resources_to_load = resources

    @staticmethod
    def load():
        ResourceLoader.resources = []
        for path, res_type in ResourceLoader.resources_to_load.items():
            ResourceLoader.resources.append(Resource(res_type, path))
        ResourceLoader.loaded = {
            ResourceLoader.resources[i].path: ResourceLoader.resources[i]
            for i in range(len(ResourceLoader.resources))
        }

    @staticmethod
    def load_image(path) -> Resource:
        if path in ResourceLoader.loaded:
            return ResourceLoader.loaded[path]
        else:
            ResourceLoader.loaded[path] = Resource(Resource.IMAGE, path)
            return ResourceLoader.loaded[path]

    @staticmethod
    def load_sound(path) -> Resource:
        if path in ResourceLoader.loaded:
            return ResourceLoader.loaded[path]
        else:
            ResourceLoader.loaded[path] = Resource(Resource.SOUND, path)
            return ResourceLoader.loaded[path]

    @staticmethod
    def generate_raw_resource_dict(root) -> dict[str, int]:
        res = {}
        for path, subdirs, files in os.walk(root):
            for name in files:
                p = os.path.join(path, name).removeprefix("./")
                if p.endswith(".png"):
                    res[p] = Resource.IMAGE
                elif p.endswith(".wav"):
                    res[p] = Resource.SOUND
        return res
