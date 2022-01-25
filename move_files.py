import os
import datetime as dt


def move_specified_files(file_name_pattern, src_dir, tgt_dir):
    count_files = 0
    try:
        while True:
            for roots, folders, files in os.walk(src_dir):
                for file in files:
                    if file.endswith(file_name_pattern):
                        os.replace(f'{src_dir}/{file}', f'{tgt_dir}/{file}')
                        count_files += 1
                    else:
                        pass
                with open(f'{src_dir}/log.txt', 'a') as log_file:
                    log_file.write(f'\n{count_files} files uploaded: {dt.datetime.now()}')
                input('Done...')
    except FileNotFoundError:
        pass


move_specified_files(input('File pattern: '), input('Source directory: '), input('Target directory: '))