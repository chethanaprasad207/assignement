class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=60)
    email_address = models.EmailField()