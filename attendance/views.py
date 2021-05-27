from django.shortcuts import render

# Create your views here.
from attendance.models import Attandance
from employee.models import Employee
from dashboard.views import getProbations


def attendanceview(request):
    employee = Employee.objects.all()
    employeeList = request.POST.getlist('employeeList[]')

    prob = getProbations()
    count = prob.count()

    if request.POST:

        for e in employeeList:
            Asheet = Attandance()

            status_emp = request.POST.get(e)
            # attendance_emp = request.POST.get('emp-att')
            # date_emp = request.POST.get('emp_date')

            emp = Employee.objects.get(id=e)

            print("-----------------")
            print(status_emp)
            Asheet.emp_attandande = emp
            Asheet.status = status_emp
            Asheet.save()

            # Att = Attandance(status=status_emp, emp_attandande=employee[1])
            # Att.save()
            # return attendanceview(request,Asheet.id)

    return render(request, 'attendance/attendance_view.html', {'employee': employee, "prob": prob, 'count': count})
