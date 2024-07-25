from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm



# Create your views here.
def list_student(request):
    student = Student.objects.all()
    return render(request, "list_student.html", {"student": student})



def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect("/")
        else:
            messages.error(request, 'There was an error adding the student.')
    else:
        form = StudentForm()

    return render(request, "add.html", {"form": form})
# Updating studen

def update(request, id):
    student = get_object_or_404(Student, pk=id)  # This will raise a 404 if the student does not exist
    
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect("/")
        else:
            messages.error(request, 'There was an error updating the student.')
    else:
        form = StudentForm(instance=student)

    return render(request, "update.html", {"form": form})

