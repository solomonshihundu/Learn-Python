#f = open("D:\Learn Python\Coursera\Python Automation\Module 1\Project\wordcloud.txt", "r")
#print(f.read())

from ipywidgets import FileUpload

def on_upload_change(change):
    if not change.new:
        return
    up = change.owner
    for filename,data in up.value.items():
        print(f'writing [{filename}] to ./')
        with open(filename, 'wb') as f:
            f.write(data['content'])
    up.value.clear()
    up._counter = 0

upload_btn = FileUpload()
upload_btn.observe(on_upload_change, names='_counter')
upload_btn