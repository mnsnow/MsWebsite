from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def home(request):
    """ Home page """
    return render(request, 'ms_pages/home.html')

@login_required
def topics(request):
    """ All topics page"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'ms_pages/topics.html', context)

@login_required
def topic(request, topic_id):
    """ Individual topic page """
    topic = Topic.objects.get(id=topic_id)
    #make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'ms_pages/topic.html', context)

@login_required
def new_topic(request):
    """ Page for user to create new topic """
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('ms_pages:topics'))

    context = {'form': form}
    return render(request, 'ms_pages/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """ Page for user to create new entry """
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        form = EntryForm()                                                
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('ms_pages:topic',
                                                args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'ms_pages/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ Edit an existing entry """
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance = entry)
    else:
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ms_pages:topic',
                                                args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request, 'ms_pages/edit_entry.html', context)






















