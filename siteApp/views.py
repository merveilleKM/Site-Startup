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

        # Envoyer un email
        try:
            # Envoyer un email de confirmation à l'utilisateur
            send_mail(
                subject="Confirmation de réception de votre demande de stage",
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

    return render(request, 'stage.html')

def formation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cv = request.FILES.get('cv')
        message = request.POST.get('message')

        # Enregistrement dans la base de données
        postulation = Formation(
            name=name,
            email=email,
            phone=phone,
            cv=cv,
            message=message
        )
        postulation.save()

        # Envoyer un email
        try:
            # Envoyer un email de confirmation à l'utilisateur
            send_mail(
                subject="Confirmation de réception de votre demande de formation",
                message=f"Bonjour {name},\n\n"
                        "Merci de vous etre inscrit a notre formation, nous reviendrons vers vous\n "
                        "avec les prochaines etapes"
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

    return render(request, 'formation.html')

def actualite(request):
    actualites = Actualite.objects.all().order_by('-date_publication')
    return render(request, "actualite.html", {"actualites": actualites})

def actualite_detail(request, id):
    actualite = get_object_or_404(Actualite, id=id)
    return render(request, "actualite_detail.html", {"actualite": actualite})