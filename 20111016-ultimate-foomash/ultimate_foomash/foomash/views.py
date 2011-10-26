from foomash.models import Foo, Category
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.http import HttpResponseForbidden

class VoteForm(forms.Form):
	vote = forms.IntegerField(widget=forms.HiddenInput)


def mash(request, category):
	category = get_object_or_404(Category, pk=category)
	foos = category.foo_set.all().order_by('-score')
	left, right = Foo.objects.order_by('?').filter(categor=category)[:2]
	request.session['allowed_votes'] = [left.id, right.id]

	return render(request, 'foomash/mash.html',
		{'left': left,
		'right':right,
		'left_form':VoteForm(data={'vote':left.id}),
		'right_form':VoteForm(data={'vote':right.id}),
		'category': category,
		'foos':foos})

def vote(request):
	if request.method == 'POST':
		form = VoteForm(request.POST)
		if form.is_valid():
			if not form.cleaned_data['vote'] in request.session['allowed_votes']:
				return HttpResponseForbidden('Nope. Chuck Testa. ROFL')
			foo = Foo.objects.get(id=form.cleaned_data['vote'])
			foo.score += 1
			foo.save()
	return redirect(mash, foo.categor.id)
	