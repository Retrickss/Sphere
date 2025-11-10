"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView,OrganizationUpdateView, OrganizationDeleteView
from studentorg import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePageView.as_view(), name="home"),
    path("accounts/", include("allauth.urls")), # allauth routes
    path('', include('pwa.urls')),

    # Organization
    path("organization_list", views.OrganizationList.as_view(), name="organization-list"),
    path("organization_list/add", views.OrganizationCreateView.as_view(), name="organization_add"),
    path("organization_list/<pk>", views.OrganizationUpdateView.as_view(), name="organization_update"),
    path("organization_list/<pk>/delete", views.OrganizationDeleteView.as_view(), name="organization_delete"),

    # College
    path("college_list", views.CollegeList.as_view(), name="college-list"),
    path("college_list/add", views.CollegeCreateView.as_view(), name="college-add"),
    path("college_list/<pk>", views.CollegeUpdateView.as_view(), name="college-update"),
    path("college_list/<pk>/delete", views.CollegeDeleteView.as_view(), name="college-delete"),

    # Student
    path("student_list", views.StudentList.as_view(), name="student-list"),
    path("student_list/add", views.StudentCreateView.as_view(), name="student-add"),
    path("student_list/<pk>", views.StudentUpdateView.as_view(), name="student-update"),
    path("student_list/<pk>/delete", views.StudentDeleteView.as_view(), name="student-delete"),

    # OrgMember
    path("orgmember_list", views.OrgMemberList.as_view(), name="orgmember-list"),
    path("orgmember_list/add", views.OrgMemberCreateView.as_view(), name="orgmember-add"),
    path("orgmember_list/<pk>", views.OrgMemberUpdateView.as_view(), name="orgmember-update"),
    path("orgmember_list/<pk>/delete", views.OrgMemberDeleteView.as_view(), name="orgmember-delete"),

    # Programs
    path("programs_list", views.ProgramList.as_view(), name="program-list"),
    path("programs_list/add", views.ProgramCreateView.as_view(), name="program-add"),
    path("programs_list/<int:pk>/edit", views.ProgramUpdateView.as_view(), name="program-update"),
    path("programs_list/<int:pk>/delete", views.ProgramDeleteView.as_view(), name="program-delete"),

]
