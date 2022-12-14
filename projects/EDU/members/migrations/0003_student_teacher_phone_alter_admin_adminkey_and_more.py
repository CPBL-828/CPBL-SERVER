# Generated by Django 4.0.3 on 2022-10-21 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentKey', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='학생키')),
                ('name', models.CharField(max_length=50, verbose_name='강사명')),
                ('birth', models.DateField()),
                ('sex', models.CharField(max_length=1)),
                ('phone', models.CharField(max_length=11)),
                ('school', models.CharField(max_length=10)),
                ('grade', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('remark', models.TextField()),
                ('delState', models.CharField(max_length=1)),
                ('profileImg', models.CharField(max_length=50)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('editDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone',
            field=models.CharField(default='01035352424', max_length=11, verbose_name='연락처'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admin',
            name='adminKey',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='관리자키'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='createDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='editDate',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.CharField(max_length=50, verbose_name='관리자id'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='type',
            field=models.CharField(max_length=10, verbose_name='관리자유형'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='createDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='editDate',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.CharField(max_length=50, verbose_name='강사id'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='joinDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='입사일'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='leaveDate',
            field=models.DateTimeField(auto_now=True, verbose_name='퇴사일'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=10, verbose_name='강사명'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='part',
            field=models.CharField(max_length=10, verbose_name='담당'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='profileImg',
            field=models.CharField(max_length=50, verbose_name='프로필사진링크'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='resSubject',
            field=models.CharField(max_length=10, verbose_name='담당과목'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='resume',
            field=models.CharField(max_length=50, verbose_name='이력서링크'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacherKey',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='강사키'),
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('parentKey', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('editDate', models.DateTimeField(auto_now=True)),
                ('studentKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.student')),
            ],
        ),
    ]
