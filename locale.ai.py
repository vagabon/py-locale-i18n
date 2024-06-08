from utils.file_utils import check_file_exists, content_file, write_content
from utils.http_utils import api_json_correction, api_json_translate
import sys

if __name__ == "__main__":
    directory = sys.argv[1]
    filename = sys.argv[2]

    directory_fr = f"{directory}/fr"

    file_exists = check_file_exists(directory_fr, filename)
    print(f"\nFile exists: {file_exists}")

    # if the file exists into the directory...
    if (file_exists):
        # ...write the correction into the json
        content = content_file(directory_fr, filename)
        content_corrected = api_json_correction(content)
        write_content(directory_fr, filename, "", content_corrected)
        
        # and translate it into english on the /en directory
        content_translated = api_json_translate(content_corrected)
        write_content(f"{directory}/en", filename, "", content_translated)
