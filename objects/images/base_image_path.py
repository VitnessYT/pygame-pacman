class BaseImagePath:

    def __init__(self):
        if not hasattr(self, "multiple_directories"):
            self.multiple_directories: bool = False
        try:
            self.paths = ["data/images/" + self.extra_path + self.directory]
        except AttributeError:
            self.paths = ["data/images/" + self.directory]

        self.path = self.paths[0]

        if self.multiple_directories:
            for additional_directory in self.additional_directories:
                self.paths.append("data/images/" + self.extra_path + additional_directory)
