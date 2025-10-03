from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Project, Contact

# Homepage
def home(request):
    return JsonResponse({"message": "Welcome to Kimkosva Backend!"})

# Contact form submission
def save_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(name=name, email=email, message=message)

        return JsonResponse({"status": "success", "message": "Contact saved!"})
    return JsonResponse({"error": "Invalid request"}, status=400)

# List all projects
def project_list(request):
    projects = Project.objects.all().values("id", "title", "description", "link")
    return JsonResponse(list(projects), safe=False)

# Single project details
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    data = {
        "id": project.id,
        "title": project.title,
        "description": project.description,
        "link": project.link,
    }
    return JsonResponse(data)
