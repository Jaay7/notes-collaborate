from django.db import models

AUTH_USER_MODEL = "users.User"
# Create your models here.
class Note(models.Model):
    nid = models.AutoField(primary_key=True,serialize = False,verbose_name ='ID')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notescollab",
    )
    collaborators = models.ManyToManyField(AUTH_USER_MODEL, related_name="notescollaborator")
    collection = models.ManyToManyField("writenotes.NoteCollection", related_name="collection")

    def __str__(self):
        return self.title
    
class NoteCollection(models.Model):
    cid = models.AutoField(primary_key=True,serialize = False,verbose_name ='ID')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="collectioncollab",
    )
    collaborators = models.ManyToManyField(AUTH_USER_MODEL, related_name="collaborator")
    notes = models.ManyToManyField(Note, related_name="notes")

    def __str__(self):
        return self.title
