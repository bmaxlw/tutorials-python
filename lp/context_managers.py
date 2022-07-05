from datetime import datetime

class Logger(object):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
    
    def __enter__(self):
        self.file = open(self.file_name, 'a')
        return self.file

    # __exit__ always takes 4 arguments to handle exceptions ... 
    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type is not None:
            print(exception_type, exception_value, traceback)
        else:
            self.file.close()

with Logger('log.txt') as log:
    log.write(f'... {datetime.now()}: User | Action ...\n')

# with open('log.txt', 'a') as log:
#     log.write(f'... {datetime.now()}: User | Action ...\n')

