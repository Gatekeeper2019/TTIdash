# Generated by Django 2.2.4 on 2019-11-23 09:35

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paulapplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_joined', models.DateField()),
                ('title', models.CharField(choices=[('Paul', 'Paul'), ('Timothy', 'Timothy')], max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='media/profile_pic/')),
                ('summary', models.TextField(blank=True)),
                ('country_of_Citizenship', django_countries.fields.CountryField(max_length=2)),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=200)),
                ('district', models.CharField(choices=[('Nicobar', 'Nicobar'), ('North Middle Andaman', 'North Middle Andaman'), ('South Andaman', 'South Andaman'), ('Anantapur', 'Anantapur'), ('Chittoor', 'Chittoor'), ('East Godavari', 'East Godavari')], max_length=200)),
                ('pin_code', models.IntegerField()),
                ('ID_Proof', models.CharField(choices=[('Aadhaar', 'Aadhaar'), ('Driving license', 'Driving license')], max_length=200)),
                ('Attach_ID_Proof', models.FileField(blank=True, null=True, upload_to='media/Attach_ID_Proof/')),
                ('Marital_Status', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], max_length=200)),
                ('Name_of_Spouse', models.CharField(blank=True, max_length=100, null=True)),
                ('Years_of_Marriage', models.IntegerField()),
                ('Is_Spouse_Christian', models.CharField(choices=[('True', 'Yes'), ('False', 'No'), ('NA', 'NA')], max_length=200)),
                ('No_of_Children', models.IntegerField()),
                ('General_Physical_Health', models.CharField(choices=[('Good', 'Good'), ('Poor', 'Poor')], max_length=200)),
                ('If_Poor_please_explain', models.TextField(blank=True)),
                ('education_qualification_training', models.CharField(choices=[('Regular', 'Regular'), ('correspondence', 'correspondence')], max_length=200)),
                ('theological_qualification', models.CharField(choices=[('Regular', 'Regular'), ('correspondence', 'correspondence'), ('NA', 'NA')], max_length=200)),
                ('Name_of_the_college_Seminary', models.CharField(blank=True, max_length=100, null=True)),
                ('Place', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField()),
                ('Do_you_use_email', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=200)),
                ('Do_you_have_regular_access_to_internet', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=200)),
                ('in_what_language_do_you_like_to_run_the_TTI_training', models.CharField(blank=True, max_length=100, null=True)),
                ('are_you_already_engaged_in_any_other_training_program', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=200)),
                ('are_you_involved_in_any_church_and_or_ministry_activity', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=200)),
                ('are_you_ordained_or_licensed_pastor', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=200)),
                ('by_whom', models.CharField(blank=True, max_length=100, null=True)),
                ('disqualification_based_on_1Timothy3_1_to_7_and_Titus_1_6_to_9', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=200)),
                ('If_yes_please_explain', models.TextField(blank=True)),
                ('Church_or_Denominational_Membership', models.CharField(blank=True, max_length=100, null=True)),
                ('Name_of_the_church', models.CharField(blank=True, max_length=100, null=True)),
                ('Denomination', models.CharField(blank=True, max_length=100, null=True)),
                ('Head_of_your_denomination_Mentor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Briefly_describe_your_Salvation_experience', models.TextField(blank=True)),
                ('Mention_the_languages_you_speak_Read_Write', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timothyapplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_joined', models.DateField()),
                ('title', models.CharField(choices=[('Paul', 'Paul'), ('Timothy', 'Timothy')], max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='media/profile_pic/')),
                ('country_of_Citizenship', django_countries.fields.CountryField(max_length=2)),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=200)),
                ('district', models.CharField(choices=[('Nicobar', 'Nicobar'), ('North Middle Andaman', 'North Middle Andaman'), ('South Andaman', 'South Andaman'), ('Anantapur', 'Anantapur'), ('Chittoor', 'Chittoor'), ('East Godavari', 'East Godavari')], max_length=200)),
                ('pin_code', models.IntegerField()),
                ('Mention_the_languages_you_speak_Read_Write', models.CharField(blank=True, max_length=100, null=True)),
                ('Name_of_the_local_church', models.CharField(blank=True, max_length=100, null=True)),
                ('do_have_approval_of_your_Pastor_to_join_TTI_training', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=200)),
                ('have_you_received_Jesus_Christ_as_your_Saviour_and_Lord', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=200)),
                ('Is_your_family_in_agreement_with_this_application', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=200)),
                ('do_you_understand_you_must_plant_church_before_graduation', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=200)),
                ('are_you_committed_to_also_training_others_to_plant_Churches', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], max_length=200)),
            ],
        ),
    ]