from os import replace
from django.db import models

# Create your models here.
class PredictIncome(models.Model):
    age = models.IntegerField()

    PRIVATE = 'Private'
    SELFNOTINC = 'Unincorporated self employment'
    SELFINC = 'Incorporated self employment'
    FEDGOV = 'Federal Government'
    LOCGOV = 'Local Government'
    STATEGOV = 'State Government'
    WITHOUTPAY = 'Without Pay'
    NEVER = 'Never Worked'

    WORKCLASS_CHOICES = [
        (PRIVATE, 'Private'),
        (SELFNOTINC, 'Unincorporated self employment'),
        (SELFINC, 'Incorporated self employment'),
        (FEDGOV, 'Federal Government'),
        (LOCGOV, 'Local Government'),
        (STATEGOV, 'State Government'),
        (WITHOUTPAY, 'Without Pay'),
        (NEVER, 'Never Worked'),
    ]
    work_class = models.CharField(
        max_length=50,
        choices=WORKCLASS_CHOICES,
    )

    PRETOTWELVE = 'PreSchool to 12th Grade'
    HSGRAD = 'High School Graduate'
    SOMECOL = 'Some College'
    ASSOCIATE = 'Associate'
    BACHELOR = 'Bachelors'
    MASTERS = 'Masters'
    PROFSCH = 'Professional School'
    DOCTORATE = 'Doctorate'
    EDUCATION_CHOICES = [
        (PRETOTWELVE, 'PreSchool to 12th Grade'),
        (HSGRAD, 'High School Graduate'),
        (SOMECOL, 'Some College'),
        (ASSOCIATE, 'Associate'),
        (BACHELOR, 'Bachelors'),
        (MASTERS, 'Masters'),
        (PROFSCH, 'Professional School'),
        (DOCTORATE, 'Doctorate'),
    ]
    education = models.CharField(
        max_length=50,
        choices=EDUCATION_CHOICES,
    )

    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    NEVMARRIED = 'Never Married'
    SEPARATED = 'Separated'
    WIDOWED = 'Widowed'

    MARRIAGE_CHOICES = [
        (MARRIED, 'Married'),
        (DIVORCED, 'Divorced'),
        (NEVMARRIED, 'Never Married'),
        (SEPARATED, 'Separated'),
        (WIDOWED, 'Widowed'),
    ]
    marital_status = models.CharField(
        max_length=50,
        choices=MARRIAGE_CHOICES,
    )

    TECH = 'Technical Support'
    CRAFT = 'Craft Repair'
    SALES = 'Sales'
    EXEC = 'Executive Manager'
    PROF = 'Professional Specialty'
    HANDCLEAN = 'Handlers or Cleaners'
    MACHINE = 'Machine Operator Inspector'
    ADMIN = 'Administrative Clerks'
    FARMFISH = 'Farming or Fishing'
    TRANSPORT = 'Transport and Moving Services'
    PRIVHSE = 'Private House Services'
    PROTECTIVE = 'Protective Services'
    ARMEDFORCE = 'Armed Forces'
    OTHER = 'Other Services'
    OCCUPATION_CHOICES = [
        (TECH, 'Technical Support'),
        (CRAFT, 'Craft Repair'),
        (SALES, 'Sales'),
        (EXEC, 'Executive Manager'),
        (PROF, 'Professional Specialty'),
        (HANDCLEAN, 'Handlers or Cleaners'),
        (MACHINE, 'Machine Operator Inspector'),
        (ADMIN, 'Administrative Clerks'),
        (FARMFISH, 'Farming or Fishing'),
        (TRANSPORT, 'Transport and Moving Services'),
        (PRIVHSE, 'Private House Services'),
        (PROTECTIVE, 'Protective Services'),
        (ARMEDFORCE, 'Armed Forces'),
        (OTHER, 'Other Services'),
    ]
    occupation = models.CharField(
        max_length=50,
        choices=OCCUPATION_CHOICES,
    )

    WIFE = 'Wife'
    OWNCHILD = 'Own Child'
    HUSBAND = 'Husband'
    OTHEREL = 'Other Relative'
    UNMARRIED = 'Unmarried'
    NOTINFAM = 'Not In Family'

    RELATIONSHIP_CHOICES = [
        (WIFE, 'Wife'),
        (OWNCHILD, 'Own Child'),
        (HUSBAND, 'Husband'),
        (OTHEREL, 'Other Relative'),
        (UNMARRIED, 'Unmarried'),
        (NOTINFAM, 'Not In Family'),
    ]
    relationship = models.CharField(
        max_length=20,
        choices=RELATIONSHIP_CHOICES,
    )

    WHITE = 'White'
    ASIAN = 'Asian/Pacific Islander'
    INDIAN = 'American Indian/Eskimo'
    BLACK = 'Black'
    OTHERRACE = 'Other'

    RACE_CHOICES = [
        (WHITE, 'White'),
        (ASIAN, 'Asian/Pacific Islander'),
        (INDIAN, 'American Indian/Eskimo'),
        (BLACK, 'Black'),
        (OTHERRACE, 'Other'),

    ]
    race = models.CharField(
        max_length=30,
        choices=RACE_CHOICES,
    )

    MALE = 'Male'
    FEMALE = 'Female'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    sex = models.CharField(
        max_length=10,
        choices=SEX_CHOICES,
    )

    capital_gain = models.IntegerField()

    capital_loss = models.IntegerField()

    hours_per_week = models.IntegerField()

    USA = 'United States'
    OTHERCOUNTRY = 'Other Country'

    COUNTRY_CHOICES = [
        (USA, 'United States'),
        (OTHERCOUNTRY, 'Other Country'),
    ]
    native_country = models.CharField(
        max_length=30,
        choices=COUNTRY_CHOICES,
    )

    predicts = models.CharField(
        max_length=50
    )
    
    def __str__(self):
        return self.predicts

    def get_absolute_url(self):
        return "list"













    




