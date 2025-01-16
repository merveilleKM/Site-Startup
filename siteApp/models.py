from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Adresse e-mail")
    phone = models.CharField(max_length=15, verbose_name="Numéro de Téléphone", default="null")
    subject = models.CharField(max_length=255, verbose_name="Objet")
    message = models.TextField(verbose_name="Message")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")

    def __str__(self):
        return f"Message de {self.name} - {self.email}"

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"

class Stage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom et Prénom", default="null")
    email = models.EmailField(verbose_name="Adresse Email", default="null")
    phone = models.CharField(max_length=15, verbose_name="Numéro de Téléphone", default="null")
    cv = models.FileField(upload_to='postulations/cv/', verbose_name="CV", null=True)
    certificat = models.FileField(upload_to='postulations/certificat/', verbose_name="Certificat de Scolarité", null=True)
    message = models.TextField(verbose_name="Message", blank=True, default="null")
    date_submitted = models.DateTimeField(auto_now_add=True, verbose_name="Date de Soumission")

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Stage"
        verbose_name_plural = "Stages"

class Formation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom et Prénom", default="null")
    email = models.EmailField(verbose_name="Adresse Email", default="null")
    phone = models.CharField(max_length=15, verbose_name="Numéro de Téléphone", default="null")
    cv = models.FileField(upload_to='postulations/cv/', verbose_name="CV", null=True)
    certificat = models.FileField(upload_to='postulations/certificat/', verbose_name="Certificat de Scolarité", null=True)
    message = models.TextField(verbose_name="Message", blank=True, default="null")
    date_submitted = models.DateTimeField(auto_now_add=True, verbose_name="Date de Soumission")

    def __str__(self):
        return f"{self.name} - {self.email}"
    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"

class Actualite(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="actualites/")
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
