from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
# Construct a dictionary to pass to the template engine as its context.
# Note the key boldmessage matches to {{ boldmessage }} in the template! 
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier. # Note that the first parameter is the template we wish to use. 
    return render(request, 'rango/index.html', context=context_dict)


def about (request):
    context_dict = {'boldmessage': 'here is the about page.'}
    return render(request, 'rango/about.html', context=context_dict)  





def services(request):
    services_data = {
        'page_title': 'Our Services',
        'services_list': [
            'Web Development',
            'Mobile App Development',
            'Data Analysis',
            'Graphic Design',
            'Digital Marketing'
        ]
    }
    return HttpResponse("This is the services page.")
