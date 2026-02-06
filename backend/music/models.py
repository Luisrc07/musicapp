from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Artist Name")
    bio= models.TextField(blank=True, verbose_name="Biography")
    image= models.ImageField(upload_to='artists/', blank=True, null=True, verbose_name="Artist Image")

    class Meta():
        verbose_name = "Artist"
        verbose_name_plural = "Artists"
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums', verbose_name="Artist")
    title = models.CharField(max_length=100, verbose_name="Album Title")
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name="Album Cover Image")
    release_date = models.DateField(verbose_name="Release Date", auto_now_add=True)
    

    class Meta():
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ['title']
        
    def __str__(self):
        return f"{self.title} {self.artist.name}" 

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', verbose_name="Album")
    tittle = models.CharField(max_length=100, verbose_name="Song Title")
    audio_file = models.FileField(upload_to='songs/', verbose_name="Audio File")
    duration = models.DurationField(verbose_name="Duration")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta():
        verbose_name = "Song"
        verbose_name_plural = "Songs"
        ordering = ['created_at']

    def __str__(self):
        return self.tittle