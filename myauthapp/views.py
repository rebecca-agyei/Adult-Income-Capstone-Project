from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import PredictIncome
from .forms import PredictCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import pickle

# Create your views here.


class SignUp(CreateView):
  form_class = UserCreationForm 
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

def logout_view(request):
  logout(request)
  return redirect("home")

def PredictCreate(request):
  form = PredictCreateForm()

  context = {'result': ""}
  if request.method == 'POST':
    age = int(request.POST.get('age'))
    work_class = request.POST.get('work_class')
    education = request.POST.get('education')
    marital_status = request.POST.get('marital_status')
    occupation = request.POST.get('occupation')
    relationship = request.POST.get('relationship')
    race = request.POST.get('race')
    sex = request.POST.get('sex')
    capital_gain = int(request.POST.get('capital_gain'))
    capital_loss = int(request.POST.get('capital_loss'))
    hours_per_week = int(request.POST.get('hours_per_week'))
    native_country = request.POST.get('native_country')

    wclass = pickle.load(open('myauthapp/work_class_label.pkl', 'rb'))
    edu = pickle.load(open('myauthapp/education_label.pkl', 'rb'))
    marital = pickle.load(open('myauthapp/marital_status_label.pkl', 'rb'))
    occup = pickle.load(open('myauthapp/occupation_label.pkl', 'rb'))
    relation = pickle.load(open('myauthapp/relationship_label.pkl', 'rb'))
    rc = pickle.load(open('myauthapp/race_label.pkl', 'rb'))
    sx = pickle.load(open('myauthapp/sex_label.pkl', 'rb'))
    native = pickle.load(open('myauthapp/native_country_label.pkl', 'rb'))

    wclass_val = wclass.transform([work_class])
    edu_val = edu.transform([education])
    marital_val = marital.transform([marital_status])
    occup_val = occup.transform([occupation])
    relation_val = relation.transform([relationship])
    rc_val = rc.transform([race])
    sx_val = sx.transform([sex])
    native_val = native.transform([native_country])

    model = pickle.load(open('myauthapp/income_model.sav', 'rb'))
    scaled = pickle.load(open('myauthapp/scaling.pkl', 'rb'))
    predicts = model.predict(scaled.transform([[
      age, 
      wclass_val, 
      edu_val, 
      marital_val, 
      occup_val, 
      relation_val, 
      rc_val, 
      sx_val, 
      capital_gain, 
      capital_loss, 
      hours_per_week, 
      native_val]]))
   
    new = PredictIncome(
      age=age, 
      work_class=work_class, 
      education=education, 
      marital_status=marital_status, 
      occupation=occupation, 
      relationship=relationship, 
      race=race, 
      sex=sex, 
      capital_gain=capital_gain, 
      capital_loss=capital_loss, 
      hours_per_week=hours_per_week, 
      native_country=native_country,
      predicts=predicts,
      )
    new.save()

    if predicts == 0:
      context =  "Your income is less than or equal to $50,000"
    elif predicts == 1:
      context =  "Your income is greater than $50,000"
    return render(request, "result.html", {'form':form, 'result': context})

  return render(request, "home.html", {'form':form})


class PredictList(LoginRequiredMixin, ListView):
   model = PredictIncome
   template_name = 'predict_list.html'


