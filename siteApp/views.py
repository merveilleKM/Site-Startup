from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import ContactMessage, Actualite, Formation, Stage
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def apropos(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

from django.shortcuts import render
from django.core.mail import send_mail
from .models import ContactMessage
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message_content = request.POST.get('message')

        # Enregistrer dans la base de données
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message_content
        )
        contact_message.save()

        # Envoyer un email
        try:
            # Envoyer un email de confirmation à l'utilisateur
            send_mail(
                subject="Confirmation de réception de votre message",
                message=f"Bonjour {name},\n\n"
                        "Merci de nous avoir contactés ! Nous avons bien reçu votre message et vous "
                        "répondrons dans les plus brefs délais.\n\n"
                        "Cordialement,\nL'équipe TrueSite Technology",
                from_email=None,  # Utilise DEFAULT_FROM_EMAIL dans settings.py
                recipient_list=[email],
                fail_silently=False,
            )

            # Afficher un message de succès
            messages.success(request, "Votre message a été envoyé avec succès. Un email de confirmation vous a été envoyé.")
        except Exception as e:
            # Afficher un message d'erreur si l'envoi d'email échoue
            messages.error(request, f"Une erreur est survenue lors de l'envoi du message : {str(e)}")

        # return render(request, 'contact.html')
        #     send_mail(
        #         subject="Votre message a été reçu !",
        #         message=f"Merci pour votre message, nous vous répondrons dans les plus brefs délais.\n \n \n"
        #         f"Contenu du message : {message_content}",
        #         from_email=None,  # Utilise DEFAULT_FROM_EMAIL
        #         recipient_list=[email],
        #         fail_silently=False,
        #     )
        #     messages.success(request, "Votre message a été envoyé et enregistré avec succès.")
        # except Exception as e:
        #     messages.error(request, f"Une erreur est survenue lors de l'envoi du message : {str(e)}")

        return render(request, 'contact.html')

    return render(request, 'contact.html')

def stage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cv = request.FILES.get('cv')
        certificat = request.FILES.get('certificat')
        message = request.POST.get('message')

        # Enregistrement dans la base de données
        postulation = Stage(
            name=name,
            email=email,
            phone=phone,
            cv=cv,
            certificat=certificat,
            message=message
        )
        postulation.save()

        messages.success(request, "Votre candidature a été soumise avec succès.")
        return redirect('stage')  # Redirige après soumission
    return render(request, 'stage.html')

def formation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cv = request.FILES.get('cv')
        certificat = request.FILES.get('certificat')
        message = request.POST.get('message')

        # Enregistrement dans la base de données
        postulation = Formation(
            name=name,
            email=email,
            phone=phone,
            cv=cv,
            certificat=certificat,
            message=message
        )
        postulation.save()

        messages.success(request, "Votre candidature a été soumise avec succès.")
        return redirect('formation')  # Redirige après soumission
    return render(request, 'formation.html')

def actualite(request):
    actualites = Actualite.objects.all().order_by('-date_publication')
    return render(request, "actualite.html", {"actualites": actualites})

def actualite_detail(request, id):
    actualite = get_object_or_404(Actualite, id=id)
    return render(request, "actualite_detail.html", {"actualite": actualite})