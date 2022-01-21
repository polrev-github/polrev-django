from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from accounts.models import User
from .forms import ContactForm, ProfileEditForm

def index(request):
    return render(request, 'home/index.html', {'posts': posts})

'''
def blog(request):
    posts = Post.objects.filter(last_published_at__lte=timezone.now()).order_by('last_published_at')
    return render(request, 'blog/blog.html', {'posts': posts})
'''

def phonebanking(request):
    return render(request, 'home/phonebanking.html')

def about(request):
    return render(request, 'home/about.html')

def rfo(request):
    return render(request, 'home/rfo.html')

def mission(request):
    return render(request, 'home/mission.html')

def by_laws(request):
    return render(request, 'home/by_laws.html')

def issues(request):
    return render(request, 'home/issues.html')

def transparency(request):
    return render(request, 'home/transparency.html')

def volunteer(request):
    return render(request, 'home/volunteer.html', {'form': ContactForm})

def endorsements(request):
    return render(request, 'home/endorsements.html')

def register(request):
    return render(request, 'home/register.html')

def privacy(request):
    return render(request, 'home/privacy.html')

def contact(request):
    return render(request, 'home/contact.html', {'form': ContactForm})

'''
def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post})
'''

'''
def profile(request, username):
    profile = get_object_or_404(User, username=username)
    posts = Post.objects.filter(owner=profile)
    return render(request, 'home/profile.html', {'profile': profile, 'posts': posts})

def profile_edit(request, username):
    profile = get_object_or_404(User, username=username)
    return render(request, 'home/profile_edit.html', {'profile': profile, 'form': ProfileEditForm})
'''