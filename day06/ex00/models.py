from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Reputation(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	value = models.IntegerField(default=0)


class Upvote(models.Model):
	""" on cree une instance de cette classe pour representer un upvote
		et on la supprime si on enleve le vote """
	voter = models.CharField(max_length=150)


class Downvote(models.Model):
	""" on cree une instance de cette classe pour representer un downvote
		et on la supprime si on enleve le vote """
	voter = models.CharField(max_length=150)

class Tip(models.Model):
	contenu = models.TextField()
	auteur = models.CharField(max_length = 150)
	date = models.DateTimeField(auto_now_add=True) # la date sera inserre automatiquement
	upvote = models.ManyToManyField(Upvote)
	downvote = models.ManyToManyField(Downvote)

	def upvoteForUser(self, user):
		auteur = User.objects.get(username=self.auteur)      
		votes = self.upvote.all()
		# si l'un des votes a pour valeur de champ voter identique au user en cours, le supprimer
		found = False
		for index in votes:
			if index.voter == user.username:
				found = True
				index.delete()
				auteur.reputation.value -= 5
				auteur.reputation.save()
				print("La réputation de " + auteur.username + " a changé et est maintenant a : " + str(auteur.reputation.value))
				break
		# sinon creer le Upvote, le relier au tip et supprimer l'eventuel downvote
		if not found:
			newvote = Upvote(voter=user.username)
			newvote.save()
			auteur.reputation.value += 5
			auteur.reputation.save()
			print("La réputation de " + auteur.username + " a changé et est maintenant a : " + str(auteur.reputation.value))
			self.upvote.add(newvote)
			
			downvotes = self.downvote.all()
			for index in downvotes:
				if index.voter == user.username:
					index.delete()
					auteur.reputation.value += 2
					auteur.reputation.save()
					print("La réputation de " + auteur.username + " a changé et est maintenant a : " + str(auteur.reputation.value))
					break
			self.save()


	def downvoteForUser(self, user):
		auteur = User.objects.get(username=self.auteur)      
		votes = self.downvote.all()
		# si l'un des votes a pour valeur de champ voter identique au user en cours, le supprimer
		found = False
		for index in votes:
			if index.voter == user.username:
				found = True
				index.delete()
				auteur.reputation.value += 2
				auteur.reputation.save()
				print("La réputation de " + auteur.username + " a changé et est maintenant a : " + str(auteur.reputation.value))
				break
		# sinon creer le Downvote, le relier au tip et supprimer l'eventuel Upvote
		if not found:
			newvote = Downvote(voter=user.username)
			newvote.save()
			auteur.reputation.value -= 2
			auteur.reputation.save()
			print("La réputation de " + auteur.username + " a changé et est maintenant a : " + str(auteur.reputation.value))
			self.downvote.add(newvote)
			
			upvotes = self.upvote.all()
			for index in upvotes:
				if index.voter == user.username:
					index.delete()
					auteur.reputation.value -= 5
					auteur.reputation.save()
					print("La réputation de " + auteur.username + " a changé et est maintenant a : " + str(auteur.reputation.value))
					break
			self.save()

	def __str__(self):
		return str(self.date) + ' ' + self.contenu + ' par ' + self.auteur \
			+ ' upvotes : ' + str(len(self.upvote.all())) \
			+ ' downvotes : ' + str(len(self.downvote.all()))