from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contactform = ContactForm()
    if request.method == "POST":
        contactform = ContactForm(data=request.POST)
        if contactform.is_valid():
            name    = request.POST.get('name','')
            email   = request.POST.get('email','')
            content = request.POST.get('content','')
            ## Suponer que todo esta bien
            email = EmailMessage(
                "El Cafe: Nuevo mensaje de Contacto",
                "de {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["pepeparraga74@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                ##Atodo ok
                return redirect(reverse("contact")+"?ok")
            except:
                ##Algo no va bien
                return redirect(reverse("contact")+"?fail")
        
    return render(request,"contact/contact.html", {'form':contactform})