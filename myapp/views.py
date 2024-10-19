from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.core.paginator import Paginator
from .models import DarkModePreference

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # User will be activated by admin
            user.save()
            return redirect('registration_complete')  # Define this view
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def create_post(request):
    if Post.objects.filter(user=request.user).exists():
        return redirect('post_exists')  # Define a template for this
    if request.method == 'POST':
        form = Post(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_success')  # Define success template
    else:
        form = Post()
    return render(request, 'create_post.html', {'form': form})


@login_required
def toggle_dark_mode(request):
    # Get or create a DarkModePreference for the logged-in user
    preference, created = DarkModePreference.objects.get_or_create(user=request.user)

    # Toggle the dark mode preference
    preference.is_dark_mode = not preference.is_dark_mode
    preference.save()

    # Redirect back to the previous page (or home)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def post_list(request):
    posts = Post.objects.filter(is_approved=True)
    paginator = Paginator(posts, 3)  # 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'page_obj': page_obj})
