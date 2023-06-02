def handle_uploaded_file(f):
    with open('my_app_upload/static/js/upload/' +f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)