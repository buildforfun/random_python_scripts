import qrcode
import validators
from pathlib import Path


def create_qr_code(url):
    '''
    Generates a QR code for the URL and saves it.

    Args:
        url (str): The webpage url
    '''
    if not validators.url(url):
        raise ValueError("Please enter a valid URL")

    # Create the directory if it doesn't exist
    qrcodes_dir = Path("qrcodes")
    qrcodes_dir.mkdir(exist_ok=True)

    # Generates a unique file name based on hash of url
    filename = "image_{}.jpg".format(hash(url))
    file_path = qrcodes_dir / filename

    # Generate QR code and saves it to the file path
    img = qrcode.make(url)
    img.save(file_path)

    return str(file_path)


'''
The if __name__ == "__main__" line allows you to  run certain code
only when the script is executed directly,
and not when it is imported as a module

If you run the script directly, then __name__ is set to "__main__"

If the script is imported as a module into another Python program,
then __name__ is set to the name of the script/module file
'''
if __name__ == "__main__":
    try:
        url = input("Enter url: ")
        file_path_saved = create_qr_code(url)
        print("QR code has been saved: " + file_path_saved)
    except ValueError as e:
        # Catches when the value is of the right type but incorrect value
        print("Error: {}".format(e))
    except Exception as e:
        # Catches any type of exception
        print("Error: {}".format(e))
