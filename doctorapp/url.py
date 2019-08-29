from django.urls import path
from . import views
import django.conf.urls
from django.views.generic import TemplateView 
urlpatterns=[
	path('',views.home,name='doctor first page'),
	path('signup/',views.signup,name="doctor signup"),
	path('ajaxlogin/',views.ajaxlogin,name="ajaxlogin"),
	path('signup/ajaxsignup/',views.ajaxsignup,name="ajaxsignup"),
	path('doctorhomepage/',views.doctorhomepage,name="doctorhomepage"),
	path('addpatient/',views.addpatient,name="addpatient"),
	path('addpatient/ajaxaddpatient/',views.ajaxaddpatient,name="ajaxaddpatient"),
	path('viewpatient/',views.viewpatient,name="viewpatient"),
	path('viewpatient/ajaxviewpatient/',views.ajaxviewpatient,name="ajaxviewpatient"),
	path('searchpatient/',views.searchpatient,name="searchpatient"),
	path('searchpatient/ajaxview/',views.ajaxview,name="ajaxview"),
	path('searchpatient/ajaxseachpatient/',views.ajaxseachpatient,name="ajaxseachpatient"),
	path('addmulcondition/',views.addmulcondition,name="addmulcondition"),
	path('addmulcondition/ajaxpaview/',views.ajaxpaview,name="ajaxpaview"),
	path('addmulcondition/ajaxaddserach/',views.ajaxaddserach,name="ajaxaddserach"),
	path('addmulcondition/ajaxupdate/',views.ajaxupdate,name="ajaxupdate"),
	path('doctorlogout/',views.doctorlogout,name="doctorlogout"),
]
