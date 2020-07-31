from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
import random
from .forms import InscriptionForm, ConnectionForm,TipForm
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Tip, Upvote, Downvote, Reputation


# Create your views here.


def acceuil(request):
	""" Cette fonction traite la page acceuil 
		A noter l'usage de user : c'est un pseudo utilisateur genere
		aleatoirement a partir d'une liste dans les settings, dont la duree de vie 
		et le nom sont stockes dans un cookie pour illustrer l'usage des cookies
	"""

	tips = Tip.objects.all().order_by('date')

	if request.method == 'POST':
		if 'deletetip' in request.POST:
			# on ne passe ici que si l'utilisateur a clique sur un bouton nomme deletetip
			print("demande de suppression d'un tip")
			# # il faut initialiser un form pour la partie TipForm
			# form = TipForm()

			t = Tip.objects.get(id = request.POST['tipid']) # recherche
			auteur = User.objects.get(username=t.auteur)      
			auteur.reputation.value -= (t.upvote.count() * 5 - t.downvote.count() * 2)
			
			auteur.reputation.save()
			t.delete()

		elif 'upvote' in request.POST:
			# on ne passe ici que si l'utilisateur a clique sur un bouton nomme upvote
			print("demande de upvote")
			# # il faut initialiser un form pour la partie TipForm
			# form = TipForm()
			# chercher tous les Upvote relies au Tip :
			ts = Tip.objects.get(id = request.POST['tipid'])
			ts.upvoteForUser(request.user)


		elif 'downvote' in request.POST:
			# on ne passe ici que si l'utilisateur a clique sur un bouton nomme downvote
			print("demande de downvote")
			# # il faut initialiser un form pour la partie TipForm
			# form = TipForm()
			# chercher tous les Upvote relies au Tip :
			ts = Tip.objects.filter(id = request.POST['tipid'])
			if len(ts) > 0:
				t = ts[0] # le premier tip de la liste est le bon (il n'y en a qu'un)
				t.downvoteForUser(request.user)


		else: # cas ou l'on a valide le TipForm
			form = TipForm(request.POST)
			if form.is_valid():
				# creer le Tip
				data = form.cleaned_data
				tip = Tip(contenu = data['contenu'], auteur = request.user.username)
				tip.save()
				print('Nouveau Tip créé',tip)
				#return redirect('/')

		return redirect('ex00:acceuil')
	
	else: # methode 'GET':
		form = TipForm ()

		if request.user.is_authenticated:
			default_user = request.user
			response = render(request, 'ex00/acceuil.html', {'default_user': default_user, 'tips' : tips, 'form': form})
			# request.user.reputation.value = 0
			# request.user.reputation.save()
			print("La reputation de " + str(request.user) + " est de : " + str(request.user.reputation.value))
		elif request.COOKIES.get('mycookie'):
			default_user = request.COOKIES['mycookie']
			response = render(request, 'ex00/acceuil.html', {'default_user': default_user, 'tips' : tips, 'form': form})
			# print("La reputation de " + str(request.user) + "est de : " + str(request.user.reputation.value))
		else:
			# il n'y a pas de cookie ou bien le precedent est arrive a echeance
			default_user = random.choice(settings.USER_NAMES)
			response = render(request, 'ex00/acceuil.html', {'default_user': default_user, 'tips' : tips, 'form': form})
			response.set_cookie('mycookie', default_user, max_age = settings.SESSION_COOKIE_DURATION)

		return response




def connexion(request):
	if request.user.is_authenticated: # si je suis deja authentifie, je vais vers acceuil
		return redirect('ex00:acceuil')
	if request.method == 'POST':
		form = ConnectionForm (request.POST)
		if form.is_valid():
			data = form.cleaned_data
			u = auth.authenticate(username=data['username'], password=data['password'])
			if u and u.is_active:
				auth.login(request, u) # on se loggue
				print('Utilisateur connecté')
				try:
					print("Utilisateur " + str(u) + " connecté. \nRéputation : " + str(u.reputation.value))
				except:
					reputation = Reputation(user=u)
					reputation.save()
					print("Utilisateur " + str(u) + " connecté. \nReputation initialisé.")
				return redirect('ex00:acceuil')
			else:
				print('Utilisateur inconnu ou inactif')
				form._errors['username'] = ['Utilisateur inconnu ou inactif']


	else: # methode 'GET':
		form = ConnectionForm ()

	return render(request, 'ex00/connexion.html', {'user': None, 'form': form, })

def inscription(request):
	if request.user.is_authenticated: # si je suis deja authentifie, je vais vers acceuil
		return redirect('ex00:acceuil')
	if request.method == 'POST':
		form = InscriptionForm (request.POST)
		if form.is_valid():
			# creer le user
			data = form.cleaned_data
			u = User.objects.create_user(data['username'], None, data['password'])
			u.save()
			reputation = Reputation(user=u)
			reputation.save()
			auth.login(request, u) # on se loggue
			print('Utilisateur créé et loggué ',u)

			return redirect('ex00:acceuil')
	else: # methode 'GET':
		form = InscriptionForm ()

	return render(request, 'ex00/inscription.html', {'user': None, 'form': form, })


def logout(request):
	auth.logout(request)
	return redirect('ex00:acceuil')
