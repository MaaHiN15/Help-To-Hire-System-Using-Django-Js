from django.shortcuts import render, redirect
from .models import Org, Seeker, Eventlist, Job_application
from uuid import uuid4 


def home(request):
    return render(request, 'index.html')



################ AUTHENTICATION ######################

def job_seeker_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Seeker.objects.filter(email=email, password=password):
            request.session['jemail'] = email
            return redirect('j_home')
        else:
            msg = 'Incorrect Username/Password'
            return render(request, 'job_login.html', {'msg' : msg})
    return render(request, 'job_login.html')

def event_organizer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST['password']
        if Org.objects.filter(email=email, password=password):
            request.session['oemail'] = email
            return redirect('gotopost')
        else:
            msg = 'Incorrect Username/Password'
            return render(request, 'org_login.html', {'msg' : msg})
    return render(request, 'org_login.html')

# ... other views ...
def job_seeker_registration(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        qualification =request.POST.get('qual')
        skills = request.POST.get('skills')
        ph_num = request.POST.get('ph_num')
        alt_num = request.POST.get('alt_num')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        address = request.POST.get('address')
        try:
            obj = Seeker(name, email, gender, qualification, skills, ph_num, alt_num, dob,  password, address)
            obj.save()
            return render(request, 'j_welcome.html')
        except Exception as e:
            print(e)
            return render(request, 'job_registration.html')
    return render(request, 'job_registration.html')

def organizer_registration(request):
    if request.method == 'POST':
        msg = ''
        name = request.POST.get('username')
        gender = request.POST.get('gender')
        ph_num = request.POST.get('ph_num')
        email = request.POST.get('email')
        address = request.POST.get('address')
        company_name = request.POST.get('company_name')
        alt_num = request.POST.get('alt_num')
        password = request.POST.get('password')
        try:
            obj = Org(name, gender, ph_num, email, address, company_name, alt_num, password)
            obj.save()
            return render(request, 'o_welcome.html')
        except Exception as e:
            print(e)
            return redirect('home')
    return render(request, 'org_registration.html')



def aboutus(request):
    return render(request, 'aboutus.html')

def privacypolicy(request):
    return render(request, 'privacypolicy.html')

def terms(request):
    return render(request, 'terms.html')

def cultural(request):
    return render(request, 'events/cultural.html')

def education(request):
    return render(request, 'events/education.html')

def fashion(request):
    return render(request, 'events/fashion.html')

def health(request):
    return render(request, 'events/health.html')

def music(request):
    return render(request, 'events/music.html')

def network(request):
    return render(request, 'events/network.html')

def outdoor(request):
    return render(request, 'events/outdoor.html')

def parties(request):
    return render(request, 'events/parties.html')

def product(request):
    return render(request, 'events/product.html')

def sports(request):
    return render(request, 'events/sports.html')

def tech(request):
    return render(request, 'events/tech.html')

def wedding(request):
    return render(request, 'events/wedding.html')

def gotopost(request):
    if 'oemail' in request.session:
        return render(request, 'o_gotopost.html')
    return redirect('home')


################ EVENT ORGANIZER #######################


def postjob(request):
    if 'oemail' in request.session:
        if request.method == 'POST':
            event_id = uuid4().hex
            org_email = request.session.get('oemail')
            company_name = request.POST.get('company')
            event_title = request.POST.get('event')
            skills = request.POST.get('skills')
            city = request.POST.get('city')
            vacancies = request.POST.get('vacancies')
            salary = request.POST.get('salary')
            venue = request.POST.get('venue')
            date = request.POST.get('date')
            time = request.POST.get('time')
            description = request.POST.get('description')
            try:
                post = Eventlist(event_id, org_email, company_name, event_title, skills, city, vacancies, salary, venue, date, time, description)
                post.save()
                return redirect('gotopost')
            except Exception as e:
                print(e)
        return render(request, 'postjob.html')
    return redirect('home')

def org_logout(request):
    del request.session['oemail']
    return redirect('home')



######## JOB SEEEKER #########


def j_home(request):
    if 'jemail' in request.session:
        user = Seeker.objects.get(email=request.session.get('jemail'))
        jobs = Eventlist.objects.filter(skills=user.skills)
        return render(request, 'j_home.html', {'job_posts' : jobs})
    return redirect('home')

def apply_job(request):
    if 'jemail' in request.session:
        id = request.GET.get('id')
        email = request.GET.get('email')
        try:
            application = Job_application(event_id=id, j_email=request.session.get('jemail'), org_email=email)
            application.save()
            event = Eventlist.objects.get(event_id=id)
            event.delete()
            return redirect('j_home')
        except Exception as e:
            print(e)
            return redirect('j_home')
    return redirect('home')

def get_applications(request):
    if 'oemail' in request.session:
        applications = Job_application.objects.filter(org_email = request.session.get('oemail'))
        total_applications = []
        for i in applications:
            user = Seeker.objects.get(email=i.j_email)
            item = {
                'name' : user.name,
                'email' : user.email,
                'gender' : user.gender,
                'qualification' : user.qualification,
                'skills' : user.skills,
                'ph_num' : user.ph_num,
                'alt_num' : user.alt_num,
                'dob' : user.dob,
                'address' : user.address
            }
            total_applications.append(item)

        return render(request, 'o_applications.html', {'applications' : total_applications })
    return redirect('home') 

def j_logout(request):
    del request.session['jemail']
    return redirect('home')