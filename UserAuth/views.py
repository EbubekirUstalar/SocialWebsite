from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Post
from django.utils import timezone
# Create your views here.

def index(request):
    # latest_post_list = Post.objects.order_by('-created_time')[:20]
    # context = {'latest_question_list': latest_question_list}
    # emptyList = range(10)
    # context = {'emptyList': emptyList}
    return render(request, 'UserAuth/index.html', {'postList': Post.objects.order_by('-created_time')[:20]})


def loginPage(request):
    return render(request, 'UserAuth/login.html', {})

def register(request):
    return render(request, 'UserAuth/register.html', {})


def userregister(request):
    if request.method == 'POST':
        try:
            print(request.POST['terms'])
            if request.POST['inputPassword1'] == request.POST['inputPassword2']:
                username = request.POST['inputUserName']
                name = request.POST['inputName']
                surname = request.POST['inputSurname']
                email = request.POST['inputEmail']
                password = request.POST['inputPassword1']
                user = User.objects.create_user(username, email, password)
                user.first_name = name
                user.last_name = surname
                user.save()
                return render(request, 'UserAuth/register.html', {'alert_message': 'Success', 'alertColor': 'success'})
            else:
                return render(request, 'UserAuth/register.html', {'alert_message': 'Passwords are not matching', 'alertColor': 'danger'})
        except:
            return render(request, 'UserAuth/register.html', {'alert_message': 'Terms is not checked', 'alertColor': 'danger'})
    else:
        return render(request, 'UserAuth/register.html', {'alert_message': 'Not a post request', 'alertColor': 'danger'})


def userlogin(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['inputUserName'], password=request.POST['inputPassword'])
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return render(request, 'UserAuth/index.html', {'alert_message': 'Logged in successfully', 'alertColor': 'success', 'postList': Post.objects.order_by('-created_time')[:20]})

        else:
            # No backend authenticated the credentials    
            return render(request, 'UserAuth/login.html', {'alert_message': 'Failed Try Again', 'alertColor': 'danger'})


def userlogout(request):
    logout(request)
    return render(request, 'UserAuth/index.html', {'alert_message': 'Logged out in successfully', 'alertColor': 'success', 'postList': Post.objects.order_by('-created_time')[:20]})
    

def createpost(request):

    if request.method == 'POST':
        textField = request.POST['textField']
        created_time = timezone.now()
        is_edited = False
        likes = 0
        newPost = Post(text=textField, created_time=created_time, is_edited=is_edited, likes=likes, owner=request.user)
        newPost.save()
        return render(request, 'UserAuth/index.html', {'alert_message': 'Created new Post successfully', 'alertColor': 'success', 'postList': Post.objects.order_by('-created_time')[:20]})
    return render(request, 'UserAuth/index.html', {'alert_message': 'Failed Try Again', 'alertColor': 'danger', 'postList': Post.objects.order_by('-created_time')[:20]})
    
def deletepost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    try:
        postText = post.text
        post.delete()
        return render(request, 'UserAuth/index.html', {'alert_message': 'Following Post Deleted ' + postText, 'alertColor': 'success', 'postList': Post.objects.order_by('-created_time')[:20]})
    except:
        return render(request, 'UserAuth/index.html', {'alert_message': 'Failed Try Again', 'alertColor': 'danger', 'postList': Post.objects.order_by('-created_time')[:20]})




def profile(request):
    return render(request, 'UserAuth/profile.html', {})

