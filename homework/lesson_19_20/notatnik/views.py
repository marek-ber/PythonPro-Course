from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .models import Note


def all_notes(request):
    notes = Note.objects.all().order_by('id')
    paginator = Paginator(notes, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'notes.html', {'page_obj': page_obj})


def one_note(request, note_id):
    note = Note.objects.get(id=note_id)
    return HttpResponse(f"{note.title} <br> {note.content}")
