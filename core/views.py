from django.http import JsonResponse
from django.shortcuts import render
from .models import Contact, Project


# ✅ Home
def home(request):
    return JsonResponse({"message": "Welcome to Kimkosva Backend!"})


# ✅ Contact API (POST only)
def save_contact(request):
    if request.method == "POST":
        data = request.POST
        contact = Contact(
            name=data.get("name"),
            email=data.get("email"),
            message=data.get("message"),
        )
        contact.save()
        return JsonResponse({"status": "success"})
    return JsonResponse({"error": "POST required"}, status=400)


# ✅ Simple browser form (for testing)
def contact_form(request):
    if request.method == "POST":
        data = request.POST
        Contact(
            name=data.get("name"),
            email=data.get("email"),
            message=data.get("message")
        ).save()
        return JsonResponse({"status": "success"})
    return render(request, "contact_form.html")


# ✅ Projects API
def project_list(request):
    projects = Project.objects.all().values(
        "id", "title", "description", "link", "created_at"
    )
    return JsonResponse(list(projects), safe=False)


def project_detail(request, project_id):
    try:
        project = Project.objects.values(
            "id", "title", "description", "link", "created_at"
        ).get(id=project_id)
        return JsonResponse(project, safe=False)
    except Project.DoesNotExist:
        return JsonResponse({"error": "Project not found"}, status=404)

