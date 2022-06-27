from multiprocessing.sharedctypes import Value


class TimeList(list):
    def remove_if_exists(self, time):
        # Using try and except to catch error where times already deleted are trying to be deleted again
        try:
            self.remove(time)
        except ValueError:
            pass
