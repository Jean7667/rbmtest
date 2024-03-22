from django.shortcuts import render, redirect, get_object_or_404
from .models import Expert
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CustomUserCreationForm
from django.views import View
from .models import Expert, Skill


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html' 
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_customer =True 
        user.save()
        return super().form_valid(form)
    
    
    # template_name = 'base.html' start on base html 
 
 #Making sure the user created from the interface is idendify as a customer
  
# Create, but don't save the new author instance.
## >>> new_author = f.save(commit=False)  
#https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/

""" render page
def list (request):
    return render (request,'')
"""

## access about page
def about(request):
    return render(request, 'about.html')

class LogoutView(View):
     def post(self, request):
         logout(request)
         return redirect("about") #review that later

#intermediate page to logout    
def ConfirmLogout(request):
    return render (request,'registration/logout.html')
    

""" 
def cxprofile (request):
    return render (request,'customer/cxprofile.html')
 """
#view for customer profile CRUD class based view
class CxProfileView(View):
    cx_profile_template = 'customer/cxprofile.html'

    def get(self, request):
        # find the current user
        user = request.user
        if user.is_authenticated and user.is_customer:
            return render(request, self.cx_profile_template, {'user': user, 'edit_mode':True})
        else:
            return redirect('home')
        
    def post(self, request):
        user = request.user
        if user.is_authenticated and user.is_customer:
            user.first_name = request.POST.get('firstname', user.first_name)
            user.last_name = request.POST.get('lastname', user.last_name)
            user.location = request.POST.get('location', user.location)
            user.email = request.POST.get('email', user.email)
            
            user.save()
            return redirect('customer_profile')  
        else:
            return redirect('login')
                
class DeleteCxProfileView(View):
    def post(self, request):
        user = request.user
        if user.is_authenticated and user.is_customer:
            user.delete()
            return redirect('home')
        else:
            return redirect('unauthorized')
        
        

"""     def delete(self, request):
        user = request.user
        if user.is_authenticated and user.is_customer:
            if request.method == 'DELETE':
                #print (delete received)
                #user = User.objects.get(pk=user.pk)    
                user.delete()
                #print("User profile deleted")
                return redirect('home')
            else:
                return redirect('login')  """

#Read        

#Display in cxprofileview
#fct to show last Customer since created_date 
#fct last connection 

#Generic based view
# views for displaying a list of experts
class ExpertListView(ListView):
    model = Expert
    template_name = 'customer/listexpert.html'
    context_object_name = 'experts'
    paginate_by = 5
   
  # list of objects to display.  
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(skills__category=category)
            queryset = queryset.order_by('updated_at')
        return queryset
    
 #add mising information from gen view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Skill.objects.values_list('category', flat=True).distinct()
        return context


""" def ExpertBooking (request):
    return render(request, 'customer/expertbooking.html') """

def expert_booking(request):
    experts = Expert.objects.all()
    return render(request, 'customer/expertbooking.html', {'experts': experts})


from django.shortcuts import render, get_object_or_404
from .models import Expert

def expert_detail(request, expert_id):
    expert = get_object_or_404(Expert, id=expert_id)
    return render(request, 'customer/expertdetail.html', {'expert': expert})
