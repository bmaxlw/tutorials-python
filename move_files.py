import os
import datetime as dt


def move_specified_files(file_name_pattern, src_dir, tgt_dir):
    count_files = 0
    try:
        while True:
            for roots, folders, files in os.walk(src_dir):
                for file in files:
                    if file.endswith(file_name_pattern):
                        if os.path.exists(f'{tgt_dir}/{file}'):
                            continue
                        else:
                            os.replace(f'{src_dir}/{file}', f'{tgt_dir}/{file}')
                            count_files += 1
                    else:
                        pass
            with open(f'{src_dir}/log.txt', 'a') as log_file:
                log_file.write(f'\n************************************************'
                               f'\n{count_files} file(s) uploaded: '
                               f'\nDate:    {dt.datetime.now()}'
                               f'\nFrom:    {src_dir}'
                               f'\nTo:      {tgt_dir}'
                               f'\nPattern: {file_name_pattern}'
                               f'\n************************************************')
                input('Done...')
                break
    except FileNotFoundError:
        pass


move_specified_files(input('File pattern: '), input('Source directory: '), input('Target directory: '))