from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms, models

# Create your views here.
@login_required
def create_note(request):
    if request.method == "POST":
        form = forms.NoteCreationForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect("home")
    else:
        form = forms.NoteCreationForm()
    return render(request, "notes/create_note.html", {'form': form})

@login_required
def update_note(request, nid):
    note = models.Note.objects.get(nid=nid)
    if request.method == "POST":
        form = forms.NoteUpdateForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.NoteUpdateForm(instance=note)
    return render(request, "notes/update_note.html", {'form': form})

@login_required
def get_individual_note(request, nid):
    note = models.Note.objects.get(nid=nid)
    return render(request, "notes/note.html", {'note': note})

@login_required
def delete_note(request, nid):
    note = models.Note.objects.get(nid=nid)
    note.delete()
    return redirect("home")

@login_required
def create_collection(request):
    if request.method == "POST":
        form = forms.NoteCollectionCreationForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.author = request.user
            collection.save()
            return redirect("home")
    else:
        form = forms.NoteCollectionCreationForm()
    return render(request, "notes/create_collection.html", {'form': form})

@login_required
def delete_collection(request, cid):
    collection = models.NoteCollection.objects.get(cid=cid)
    collection.delete()
    return redirect("home")

@login_required
def get_individual_collection(request, cid):
    collection = models.NoteCollection.objects.get(cid=cid)
    return render(request, "notes/collection.html", {'collection': collection})

@login_required
def add_note_to_collection(request, cid, nid):
    collection = models.NoteCollection.objects.get(cid=cid)
    note = models.Note.objects.get(nid=nid)
    collection.notes.add(note)
    messages.success(request, 'Note added to collection - {0}.'.format(collection.title))
    return redirect("home")

@login_required
def remove_note_from_collection(request, cid, nid):
    collection = models.NoteCollection.objects.get(cid=cid)
    note = models.Note.objects.get(nid=nid)
    collection.notes.remove(note)
    messages.success(request, 'Note removed from collection - {0}.'.format(collection.title))
    return redirect("home")

