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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            # Enregistrer les données dans la base
            ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, "Votre message a été envoyé avec succès.")

            # Envoyer un email de notification
            send_mail(
                subject='Votre message a été reçu !',
                message=f"Bonjour {name},\n\n"
                    f"Merci de nous avoir contactés ! Votre message a bien été reçu par TrueSite Technologie. "
                    f"Nous vous répondrons dès que possible.\n\n"
                    f"Voici un résumé de votre message :\n\n"
                    f"Objet : {subject}\n"
                    f"Message : {message}\n\n"
                    f"Cordialement,\nL'équipe TrueSite Technologie.",
                from_email=None,  # Utilise DEFAULT_FROM_EMAIL
                recipient_list=[email],
            )

            return JsonResponse({'success': True, 'message': 'Message envoyé avec succès !'})
        else:
            messages.error(request, "Veuillez remplir tous les champs.")
        
        return redirect('contact')  # Redirige vers la même page ou une autre

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