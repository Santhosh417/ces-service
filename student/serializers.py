from rest_framework import serializers
from .models import Student, Enrollment, Course
import datetime


class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(many=False, queryset=Student.objects.all())
    course = serializers.PrimaryKeyRelatedField(many=False, queryset=Course.objects.all())

    def create(self, validated_data):
        enrollment = Enrollment.objects.create(
            course=validated_data['course'],
            student=validated_data['student'],
            semester_name=validated_data['semester_name'],
            status=validated_data['status']
        )
        semester = enrollment.semester_name.split(' ')
        print(semester)
        if(semester[0] == 'Summer'):
            print(datetime.datetime(int(semester[1]), 5, 17).date())
            enrollment.start_date = datetime.datetime(int(semester[1]), 5, 17).date()
            enrollment.end_date = datetime.datetime(int(semester[1]), 7, 1).date()

        elif(semester[0] == 'Fall'):
            enrollment.start_date = datetime.datetime(int(semester[1]), 8, 24).date()
            enrollment.end_date = datetime.datetime(int(semester[1]), 12, 17).date()

        else:
            enrollment.start_date = datetime.datetime(int(semester[1]), 1 , 15).date()
            enrollment.end_date = datetime.datetime(int(semester[1]), 5, 7).date()
        enrollment.save()
        return enrollment

    def update(self, enrollment, validated_data):
        enrollment.semester_name = validated_data['semester_name']
        enrollment.status = validated_data['status']
        enrollment.grade = validated_data['grade']
        semester = validated_data['semester_name'].split(' ')
        print(semester)
        if (semester[0] == 'Summer'):
            print(datetime.datetime(int(semester[1]), 5, 17).date())
            enrollment.start_date = datetime.datetime(int(semester[1]), 5, 17).date()
            enrollment.end_date = datetime.datetime(int(semester[1]), 7, 1).date()

        elif (semester[0] == 'Fall'):
            enrollment.start_date = datetime.datetime(int(semester[1]), 8, 24).date()
            enrollment.end_date = datetime.datetime(int(semester[1]), 12, 17).date()

        else:
            enrollment.start_date = datetime.datetime(int(semester[1]), 1, 15).date()
            enrollment.end_date = datetime.datetime(int(semester[1]), 5, 7).date()
        enrollment.save()
        return enrollment


    class Meta:
        model = Enrollment
        fields = ('pk', 'course', 'student', 'semester_name', 'start_date', 'end_date', 'status', 'grade')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('pk', 'course_id', 'course_name', 'professor', 'credits', 'course_type', 'program')


class StudentSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True)
    enrollments = serializers.SerializerMethodField('get_enrollments')

    def get_enrollments(self, student):
        enrollments = Enrollment.objects.filter(student=student).values()
        for enrollemnt in enrollments:
            courseid =  Course.objects.filter(id = enrollemnt['course_id']).values('course_id', 'course_name')
            for c in courseid:
                enrollemnt['course_id'] = c['course_id'] + '-' + c['course_name']
        return enrollments

    class Meta:
        model = Student
        fields = ('pk', 'name', 'nuid',  'email', 'cell_phone', 'start_date', 'graduation_date', 'enrollments')
