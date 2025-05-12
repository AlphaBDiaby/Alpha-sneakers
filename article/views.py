from django.shortcuts import render  # Pour renvoyer une page HTML avec du contexte (des données)
from .models import Sneaker  # On importe notre modèle Sneaker


def search_view(request):  # Cette fonction sera appelée quand un utilisateur fait une recherche
    query = request.GET.get('q', '')  # On récupère ce que l’utilisateur a tapé dans l’input name="q"

    # Si une recherche a été faite, on filtre les sneakers dont le nom contient le texte tapé (insensible à la casse)
    results = Sneaker.objects.filter(name__icontains=query) if query else []

    # On affiche la page search_results.html avec les résultats et la recherche tapée
    return render(request, 'article/search_results.html', {
        'query': query,
        'results': results
    })

