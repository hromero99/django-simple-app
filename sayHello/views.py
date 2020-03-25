from django.shortcuts import render
import os

def say_hello_view(request):
    hostname = os.environ.get("HOSTNAME")
    if hostname is None:
        with open("/etc/hostname", 'r') as hostname_file:
            hostname = hostname_file.readlines()[0]
    return render(
        request=request,
        template_name="hello.html",
        context = {
            "hostname": hostname
        }
    )