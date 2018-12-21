def contact_list(request):
    contacts = Contact.objects.all().order_by("phone_number")
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def save_contact_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            contacts = Contact.objects.all().order_by("phone_number")
            data['html_contact_list'] = render_to_string('contacts/includes/partial_contact_list.html', {
            'contacts': contacts
        })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return save_contact_form(request, form, 'contacts/includes/partial_contact_create.html')

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        else:
        form = ContactForm(instance=contact)
    return save_contact_form(request, form, 'contacts/includes/partial_contact_update.html')

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    data = dict()
    if request.method == 'POST':
        contact.delete()
        data['form_is_valid'] = True
        contacts = Contact.objects.all()
        data['html_book_list'] = render_to_string('contacts/includes/partial_contact_list.html', {
        'contacts': contacts
    })
    else:
        context = {'contact': contact}
        data['html_form'] = render_to_string('contacts/includes/partial_contact_delete.html', context, request=request)
    return JsonResponse(data)