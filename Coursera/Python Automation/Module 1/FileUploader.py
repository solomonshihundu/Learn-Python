import io
from IPython.display import display
import fileupload

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    print("Gets Here")

    def _cb(change):
        print("_cb executed")
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

        for i in range (len(file_contents)):
            print(i)

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()